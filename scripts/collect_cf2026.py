#!/usr/bin/env python3
"""Collect and post-process Combustion and Flame 2026 mechanism supplements.

Browser automation writes article metadata and downloaded files into the output
tree. This script handles the local, reproducible parts: folder layout,
supplement extraction, mechanism detection, ckinterp execution, summaries, and
indexes.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import datetime as dt
import difflib
import json
import os
import re
import shutil
import subprocess
import tarfile
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable


WORKSPACE = Path(r"E:\mech_collection")
ROOT = WORKSPACE / "combustion_and_flame_2026_mechanisms"
RAW = ROOT / "_raw"
DOWNLOADS = RAW / "downloads"
EXTRACTED = RAW / "extracted"
METADATA_JSON = RAW / "article_metadata.json"
CKDIR = Path(r"D:\BaiduSyncdisk\soft\CoFlame_yang")
CKEXE = CKDIR / "ckinterp.exe"
CK_FILES = ["chem.inp", "therm.dat", "chem.out"]
MMC_EXTENSIONS = [
    "zip",
    "txt",
    "docx",
    "pdf",
    "xlsx",
    "xls",
    "rar",
    "7z",
    "dat",
    "inp",
    "yaml",
    "yml",
    "cti",
    "xml",
]

KINETIC_TERMS = [
    "kinetic",
    "kinetics",
    "mechanism",
    "mechanisms",
    "modeling",
    "modelling",
    "oxidation",
    "pyrolysis",
    "autoignition",
    "auto-ignition",
    "ignition delay",
    "laminar burning velocity",
    "laminar flame speed",
]

REACTOR_TERMS = [
    ("shock tube", ["shock tube", "behind shock waves"]),
    ("rapid compression machine", ["rapid compression machine", "rcm"]),
    ("jet-stirred reactor", ["jet-stirred reactor", "jet stirred reactor", "jsr"]),
    ("flow reactor", ["flow reactor", "plug flow reactor"]),
    ("laminar flame speed", ["laminar flame speed", "laminar burning velocity"]),
    ("burner/flame structure", ["burner", "flame structure", "premixed flame", "diffusion flame"]),
    ("counterflow flame", ["counterflow"]),
    ("stirred reactor", ["stirred reactor"]),
]

FUEL_PATTERNS = [
    (r"NH\s*3|ammonia", "ammonia"),
    (r"H\s*2|hydrogen", "hydrogen"),
    (r"n\s*-?\s*decane|decane", "n_decane"),
    (r"methane|CH\s*4", "methane"),
    (r"ethylene|C\s*2\s*H\s*4", "ethylene"),
    (r"acetone", "acetone"),
    (r"furan", "furan"),
    (r"tetrahydrofuran", "tetrahydrofuran"),
    (r"2-?methylfuran", "2_methylfuran"),
    (r"pyridine", "pyridine"),
    (r"methylamine", "methylamine"),
    (r"pentane", "pentane"),
    (r"RP-?3", "rp3"),
    (r"norbornane", "norbornane"),
    (r"propane", "propane"),
    (r"acetylene", "acetylene"),
    (r"dimethyl carbonate", "dimethyl_carbonate"),
    (r"1,?2-?dimethoxyethane", "dimethoxyethane"),
    (r"coal", "coal"),
    (r"sustainable aviation fuel|SAF", "saf"),
    (r"naphtha", "naphtha"),
    (r"iron", "iron"),
]


def slugify(value: str, max_len: int = 80) -> str:
    value = re.sub(r"<[^>]+>", "", value or "")
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return (value[:max_len].strip("_") or "unknown")


def ensure_dirs() -> None:
    for path in [ROOT, RAW, DOWNLOADS, EXTRACTED]:
        path.mkdir(parents=True, exist_ok=True)


def read_metadata() -> list[dict]:
    if not METADATA_JSON.exists():
        return []
    return json.loads(METADATA_JSON.read_text(encoding="utf-8"))


def write_metadata(records: list[dict]) -> None:
    ensure_dirs()
    METADATA_JSON.write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def normalize_doi(doi: str) -> str:
    doi = (doi or "").strip()
    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
    return doi.lower()


def article_id(record: dict) -> str:
    if record.get("articleNumber"):
        return str(record["articleNumber"])
    doi = normalize_doi(record.get("doi", ""))
    match = re.search(r"(114\d+)", doi)
    if match:
        return match.group(1)
    pii = record.get("pii") or ""
    return pii[-8:] if pii else "article"


def detect_fuel(record: dict) -> str:
    text = " ".join(
        [
            str(record.get("title", "")),
            str(record.get("abstract", "")),
            str(record.get("keywords", "")),
        ]
    )
    found: list[str] = []
    for pattern, label in FUEL_PATTERNS:
        if re.search(pattern, text, flags=re.I):
            if label not in found:
                found.append(label)
    if not found:
        return "unknown_fuel"
    return "_".join(found[:4])


def is_candidate(record: dict) -> bool:
    text = (str(record.get("title", "")) + " " + str(record.get("abstract", ""))).lower()
    return any(term in text for term in KINETIC_TERMS)


def record_folder(record: dict) -> Path:
    fuel = record.get("fuelType") or detect_fuel(record)
    authors = record.get("authors") or []
    if isinstance(authors, str):
        first_author = authors.split(",")[0].strip()
    elif authors:
        first_author = str(authors[0]).strip()
    else:
        first_author = "unknown"
    short = slugify(record.get("title", ""), 45)
    name = f"{slugify(first_author, 20)}_2026_{article_id(record)}_{short}"
    return ROOT / slugify(fuel, 60) / name


def looks_like_text(path: Path) -> bool:
    try:
        chunk = path.read_bytes()[:4096]
    except OSError:
        return False
    if not chunk:
        return False
    return b"\x00" not in chunk


def read_text_limited(path: Path, limit: int = 2_000_000) -> str:
    try:
        data = path.read_bytes()[:limit]
    except OSError:
        return ""
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            return data.decode(enc, errors="ignore")
        except UnicodeDecodeError:
            continue
    return data.decode("latin-1", errors="ignore")


def classify_file(path: Path) -> set[str]:
    if not path.is_file() or not looks_like_text(path):
        return set()
    text = read_text_limited(path)
    upper = text.upper()
    labels: set[str] = set()
    if re.search(r"(^|\n)\s*ELEMENTS\b", upper) and re.search(r"(^|\n)\s*SPECIES\b", upper):
        labels.add("chemkin_mechanism")
    if re.search(r"(^|\n)\s*REACTIONS\b", upper):
        labels.add("reactions")
        labels.add("chemkin_mechanism")
    if re.search(r"(^|\n)\s*THERMO\b", upper):
        labels.add("thermo")
    if re.search(r"(^|\n)\s*TRANSPORT\b", upper):
        labels.add("transport")
    if "UNITS:" in upper and "PHASES:" in upper and ("REACTIONS:" in upper or "SPECIES:" in upper):
        labels.add("cantera")
    return labels


def safe_extract_zip(path: Path, dest: Path) -> None:
    with zipfile.ZipFile(path) as zf:
        for member in zf.infolist():
            target = dest / member.filename
            resolved = target.resolve()
            if not str(resolved).startswith(str(dest.resolve())):
                continue
            if member.is_dir():
                resolved.mkdir(parents=True, exist_ok=True)
            else:
                resolved.parent.mkdir(parents=True, exist_ok=True)
                with zf.open(member) as src, resolved.open("wb") as out:
                    shutil.copyfileobj(src, out)


def safe_extract_tar(path: Path, dest: Path) -> None:
    with tarfile.open(path) as tf:
        for member in tf.getmembers():
            target = dest / member.name
            resolved = target.resolve()
            if str(resolved).startswith(str(dest.resolve())):
                tf.extract(member, dest)


def extract_archives(files: Iterable[Path], dest: Path) -> list[str]:
    notes: list[str] = []
    dest.mkdir(parents=True, exist_ok=True)
    for path in files:
        suffix = path.suffix.lower()
        out = dest / slugify(path.stem, 80)
        try:
            if suffix in {".zip", ".docx"}:
                out.mkdir(parents=True, exist_ok=True)
                safe_extract_zip(path, out)
                notes.append(f"extracted {path.name}")
            elif suffix in {".tar", ".gz", ".tgz", ".bz2", ".xz"}:
                out.mkdir(parents=True, exist_ok=True)
                safe_extract_tar(path, out)
                notes.append(f"extracted {path.name}")
            elif suffix in {".rar", ".7z"}:
                notes.append(f"unsupported archive without 7z: {path.name}")
        except Exception as exc:  # noqa: BLE001 - keep batch processing alive
            notes.append(f"extract failed {path.name}: {exc}")
    return notes


def find_thermo_for(mech: Path, candidates: list[Path]) -> Path | None:
    labels = classify_file(mech)
    if "thermo" in labels:
        return mech
    scored: list[tuple[int, Path]] = []
    for path in candidates:
        cls = classify_file(path)
        if "thermo" in cls:
            score = 10
            name = path.name.lower()
            if "therm" in name:
                score += 5
            if path.parent == mech.parent:
                score += 3
            scored.append((score, path))
    if not scored:
        return None
    return sorted(scored, reverse=True)[0][1]


@dataclass
class CkResult:
    status: str
    species: str = ""
    reactions: str = ""
    message: str = ""
    chem_out: Path | None = None


def backup_ck_files() -> dict[str, Path | None]:
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    backups: dict[str, Path | None] = {}
    for name in CK_FILES:
        path = CKDIR / name
        if path.exists():
            backup = CKDIR / f"{name}.codex_backup_{stamp}"
            shutil.copy2(path, backup)
            backups[name] = backup
        else:
            backups[name] = None
    return backups


def restore_ck_files(backups: dict[str, Path | None]) -> list[str]:
    notes: list[str] = []
    for name in CK_FILES:
        path = CKDIR / name
        backup = backups.get(name)
        if backup is None:
            if path.exists():
                for attempt in range(8):
                    try:
                        path.unlink()
                        break
                    except PermissionError:
                        time.sleep(0.25 * (attempt + 1))
                else:
                    notes.append(f"could not remove generated {path}")
        elif backup.exists():
            restored = False
            for attempt in range(8):
                try:
                    shutil.copy2(backup, path)
                    backup.unlink()
                    restored = True
                    break
                except PermissionError:
                    time.sleep(0.25 * (attempt + 1))
            if not restored:
                notes.append(f"could not restore {path}; backup kept at {backup}")
    return notes


def parse_chem_out(path: Path) -> tuple[str, str]:
    text = read_text_limited(path, 1_000_000)
    species = ""
    reactions = ""
    patterns = [
        (r"(\d+)\s+SPECIES", "species"),
        (r"SPECIES\s*[:=]\s*(\d+)", "species"),
        (r"(\d+)\s+REACTIONS", "reactions"),
        (r"REACTIONS\s*[:=]\s*(\d+)", "reactions"),
        (r"NO\.\s*OF\s*SPECIES\s*=?\s*(\d+)", "species"),
        (r"NO\.\s*OF\s*REACTIONS\s*=?\s*(\d+)", "reactions"),
    ]
    for pattern, kind in patterns:
        match = re.search(pattern, text, flags=re.I)
        if match and kind == "species" and not species:
            species = match.group(1)
        if match and kind == "reactions" and not reactions:
            reactions = match.group(1)
    if not species:
        match = re.search(r"SPECIES\s+CONSIDERED[\s\S]+?(?=REACTIONS\s+CONSIDERED|$)", text, flags=re.I)
        if match:
            nums = [int(n) for n in re.findall(r"^\s*(\d+)\.\s+\S+", match.group(0), flags=re.M)]
            if nums:
                species = str(max(nums))
    if not reactions:
        match = re.search(r"REACTIONS\s+CONSIDERED[\s\S]+", text, flags=re.I)
        if match:
            nums = [int(n) for n in re.findall(r"^\s*(\d+)\.\s+\S", match.group(0), flags=re.M)]
            if nums:
                reactions = str(max(nums))
    return species, reactions


def strip_inline_comment(line: str) -> str:
    return line.split("!", 1)[0].strip()


def section_between(text: str, start: str) -> str:
    match = re.search(rf"(^|\n)\s*{start}\b(.*?)(^|\n)\s*END\b", text, flags=re.I | re.S)
    return match.group(2) if match else ""


def parse_chemkin_source_counts(path: Path) -> tuple[str, str]:
    text = read_text_limited(path, 5_000_000)
    species_block = section_between(text, "SPECIES")
    species_tokens: list[str] = []
    for raw in species_block.splitlines():
        line = strip_inline_comment(raw)
        if line:
            species_tokens.extend(line.split())
    reaction_block = section_between(text, "REACTIONS")
    reaction_count = 0
    aux_prefixes = (
        "LOW",
        "TROE",
        "SRI",
        "PLOG",
        "DUP",
        "DUPLICATE",
        "REV",
        "FORD",
        "HV",
        "CHEB",
        "TCHEB",
        "PCHEB",
    )
    for raw in reaction_block.splitlines():
        line = strip_inline_comment(raw)
        if not line:
            continue
        upper = line.upper().lstrip()
        if upper.startswith(aux_prefixes):
            continue
        if "=" in line or "<=>" in line or "=>" in line:
            reaction_count += 1
    return (str(len(species_tokens)) if species_tokens else "", str(reaction_count) if reaction_count else "")


def run_ckinterp(mech: Path, thermo: Path | None, dest: Path) -> CkResult:
    warning_file = dest / "ckinterp_restore_warnings.txt"
    if warning_file.exists():
        warning_file.unlink()
    if not CKEXE.exists():
        return CkResult("failed", message=f"missing {CKEXE}")
    if thermo is None:
        return CkResult("failed", message="missing therm.dat or embedded THERMO block")
    backups = backup_ck_files()
    try:
        shutil.copy2(mech, CKDIR / "chem.inp")
        shutil.copy2(thermo, CKDIR / "therm.dat")
        completed = subprocess.run(
            [str(CKEXE)],
            cwd=str(CKDIR),
            text=True,
            input="\n",
            capture_output=True,
            timeout=120,
        )
        chem_out = CKDIR / "chem.out"
        dest.mkdir(parents=True, exist_ok=True)
        copied = dest / "ckinterp_chem.out"
        if chem_out.exists():
            shutil.copy2(chem_out, copied)
        else:
            copied.write_text(
                completed.stdout + "\n" + completed.stderr,
                encoding="utf-8",
                errors="ignore",
            )
        species, reactions = parse_chem_out(copied)
        if not species or not reactions:
            source_species, source_reactions = parse_chemkin_source_counts(mech)
            species = species or source_species
            reactions = reactions or source_reactions
        has_errors = "Error..." in read_text_limited(copied, 2_000_000)
        status = "ok_with_ck_warnings" if (species or reactions) and has_errors else ("ok" if species or reactions else "failed")
        return CkResult(
            status=status,
            species=species,
            reactions=reactions,
            message=f"returncode={completed.returncode}",
            chem_out=copied,
        )
    except Exception as exc:  # noqa: BLE001
        return CkResult("failed", message=str(exc))
    finally:
        restore_notes = restore_ck_files(backups)
        if restore_notes:
            warning_file.write_text("\n".join(restore_notes) + "\n", encoding="utf-8")


def detect_reactors(record: dict) -> str:
    text = (str(record.get("title", "")) + " " + str(record.get("abstract", ""))).lower()
    found = [label for label, terms in REACTOR_TERMS if any(term in text for term in terms)]
    return ", ".join(dict.fromkeys(found)) if found else "not clear from abstract"


def gb_t_7714(record: dict) -> str:
    authors = record.get("authors") or []
    if isinstance(authors, list):
        author_text = ", ".join(str(a) for a in authors[:6])
        if len(authors) > 6:
            author_text += ", 等"
    else:
        author_text = str(authors)
    title = record.get("title", "").rstrip(".")
    volume = record.get("volume", "")
    month = record.get("month", "")
    article = article_id(record)
    doi = normalize_doi(record.get("doi", ""))
    year = "2026"
    tail = f"Combustion and Flame, {year}"
    if volume:
        tail += f", {volume}"
    if article:
        tail += f": {article}"
    if doi:
        tail += f". DOI: {doi}"
    return f"{author_text}. {title}[J]. {tail}."


def copy_downloads_for_record(record: dict, dest: Path) -> list[Path]:
    dest.mkdir(parents=True, exist_ok=True)
    keys = {normalize_doi(record.get("doi", "")), str(record.get("pii", "")).lower(), article_id(record).lower()}
    copied: list[Path] = []
    for file in DOWNLOADS.glob("*"):
        if not file.is_file():
            continue
        low = file.name.lower()
        if any(key and key.replace("/", "_").replace(".", "_") in low for key in keys) or any(
            key and key in low for key in keys
        ):
            target = dest / file.name
            if not target.exists() or target.stat().st_size != file.stat().st_size:
                shutil.copy2(file, target)
            copied.append(target)
    return copied


def url_head(url: str) -> tuple[int, str, int]:
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req, timeout=25) as response:
        length = response.headers.get("content-length") or "0"
        return response.status, response.headers.get("content-type") or "", int(length)


def url_download(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=90) as response, dest.open("wb") as out:
        shutil.copyfileobj(response, out)


def probe_supplements(max_mmc: int = 8) -> None:
    ensure_dirs()
    records = read_metadata()
    for record in records:
        if not record.get("candidate"):
            continue
        pii = record.get("pii") or ""
        if not pii:
            continue
        found = record.get("probedSupplementLinks") or []
        found_urls = {item.get("url") for item in found if isinstance(item, dict)}
        changed = False
        for idx in range(1, max_mmc + 1):
            existing = sorted(DOWNLOADS.glob(f"{pii}_mmc{idx}.*"))
            if existing:
                for target in existing:
                    url = f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}-mmc{idx}{target.suffix}"
                    if url not in found_urls:
                        found.append(
                            {
                                "url": url,
                                "file": str(target),
                                "content_type": "",
                                "content_length": target.stat().st_size,
                            }
                        )
                        found_urls.add(url)
                        changed = True
                continue
            if any(f"-mmc{idx}." in (url or "") for url in found_urls):
                continue
            urls = [(ext, f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}-mmc{idx}.{ext}") for ext in MMC_EXTENSIONS]
            head_results: list[tuple[str, str, int, str]] = []
            with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
                future_map = {executor.submit(url_head, url): (ext, url) for ext, url in urls}
                for future in concurrent.futures.as_completed(future_map):
                    ext, url = future_map[future]
                    try:
                        status, content_type, length = future.result()
                    except urllib.error.HTTPError as exc:
                        if exc.code != 404:
                            record.setdefault("probeErrors", []).append({"url": url, "error": f"HTTP {exc.code}"})
                        continue
                    except Exception as exc:  # noqa: BLE001
                        record.setdefault("probeErrors", []).append({"url": url, "error": str(exc)})
                        continue
                    if status == 200:
                        head_results.append((ext, url, length, content_type))
            if not head_results:
                break
            hit = False
            for ext, url, length, content_type in sorted(head_results, key=lambda item: MMC_EXTENSIONS.index(item[0])):
                url = f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}-mmc{idx}.{ext}"
                target = DOWNLOADS / f"{pii}_mmc{idx}.{ext}"
                if not target.exists() or target.stat().st_size != length:
                    url_download(url, target)
                found.append(
                    {
                        "url": url,
                        "file": str(target),
                        "content_type": content_type,
                        "content_length": length,
                    }
                )
                found_urls.add(url)
                changed = True
                hit = True
                break
            if not hit:
                break
        if found:
            record["probedSupplementLinks"] = found
            changed = True
        if changed:
            write_metadata(records)


def crossref_json(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Codex combustion mechanism collection (mailto:none@example.com)"},
    )
    with urllib.request.urlopen(req, timeout=12) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def clean_title(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value or "")
    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def title_similarity(left: str, right: str) -> float:
    return difflib.SequenceMatcher(None, clean_title(left), clean_title(right)).ratio()


def enrich_crossref() -> None:
    ensure_dirs()
    records = read_metadata()
    for record in records:
        if not record.get("candidate"):
            continue
        if record.get("doi"):
            continue
        title = record.get("title") or ""
        if not title:
            continue
        url = (
            "https://api.crossref.org/works?rows=5&filter=type:journal-article&query.title="
            + urllib.parse.quote(title)
        )
        try:
            data = crossref_json(url)
        except Exception as exc:  # noqa: BLE001
            record["crossrefError"] = str(exc)
            continue
        best = None
        best_score = 0.0
        for item in data.get("message", {}).get("items", []):
            item_title = (item.get("title") or [""])[0]
            venue = " ".join(item.get("container-title") or [])
            if "combustion and flame" not in venue.lower():
                continue
            score = title_similarity(title, item_title)
            if score > best_score:
                best = item
                best_score = score
        if not best or best_score < 0.86:
            continue
        record["doi"] = best.get("DOI", record.get("doi", ""))
        record["crossrefScore"] = round(best_score, 3)
        if best.get("article-number") and not record.get("articleNumber"):
            record["articleNumber"] = str(best["article-number"])
        if best.get("volume") and not record.get("volume"):
            record["volume"] = str(best["volume"])
        if not record.get("authors") and best.get("author"):
            authors = []
            for author in best["author"]:
                given = author.get("given", "")
                family = author.get("family", "")
                name = f"{given} {family}".strip()
                if name:
                    authors.append(name)
            record["authors"] = authors
        write_metadata(records)
        time.sleep(0.1)


def scan_files(paths: list[Path]) -> tuple[list[Path], list[Path], list[Path], list[Path]]:
    all_files: list[Path] = []
    for base in paths:
        if base.is_file():
            all_files.append(base)
        elif base.is_dir():
            all_files.extend([p for p in base.rglob("*") if p.is_file()])
    mechanisms: list[Path] = []
    thermos: list[Path] = []
    transports: list[Path] = []
    cantera: list[Path] = []
    for path in all_files:
        labels = classify_file(path)
        if "chemkin_mechanism" in labels:
            mechanisms.append(path)
        if "thermo" in labels:
            thermos.append(path)
        if "transport" in labels:
            transports.append(path)
        if "cantera" in labels:
            cantera.append(path)
    return mechanisms, thermos, transports, cantera


def write_summary(
    record: dict,
    dest: Path,
    mechanism_files: list[Path],
    thermo_files: list[Path],
    transport_files: list[Path],
    ck_results: list[CkResult],
    extraction_notes: list[str],
) -> None:
    rel = lambda p: str(p.relative_to(dest)) if p and str(p).startswith(str(dest)) else str(p)
    lines = [
        f"# {record.get('title', 'Untitled')}",
        "",
        "## Bibliography",
        "",
        gb_t_7714(record),
        "",
        "## Metadata",
        "",
        f"- Journal: Combustion and Flame",
        f"- Volume/issue month: {record.get('volume', '')} / {record.get('month', '')}",
        f"- Article number: {article_id(record)}",
        f"- DOI: {record.get('doi', '')}",
        f"- ScienceDirect URL: {record.get('url', '')}",
        f"- Paper PDF: {record.get('paperPdfStatus', 'pending manual download')}",
        f"- Paper PDF link: {record.get('issuePdfLink', '')}",
        f"- Fuel type: {record.get('fuelType') or detect_fuel(record)}",
        f"- Validation reactor/type from abstract: {detect_reactors(record)}",
        "",
        "## Mechanism Files",
        "",
        f"- Mechanism files: {', '.join(rel(p) for p in mechanism_files) if mechanism_files else 'not found'}",
        f"- Thermodynamic files: {', '.join(rel(p) for p in thermo_files) if thermo_files else 'not found'}",
        f"- Transport files: {', '.join(rel(p) for p in transport_files) if transport_files else 'not found'}",
        "",
        "## ckinterp Results",
        "",
    ]
    if ck_results:
        for idx, result in enumerate(ck_results, 1):
            lines.extend(
                [
                    f"### Mechanism {idx}",
                    "",
                    f"- Status: {result.status}",
                    f"- Species count: {result.species or 'not parsed'}",
                    f"- Reaction count: {result.reactions or 'not parsed'}",
                    f"- Message: {result.message}",
                    f"- chem.out copy: {rel(result.chem_out) if result.chem_out else 'not available'}",
                    "",
                ]
            )
    else:
        lines.extend(["- Status: not run", "- Species count: not available", "- Reaction count: not available", ""])
    lines.extend(
        [
            "## Abstract",
            "",
            record.get("abstract") or "not available",
            "",
            "## Processing Notes",
            "",
        ]
    )
    if extraction_notes:
        lines.extend([f"- {note}" for note in extraction_notes])
    else:
        lines.append("- none")
    dest.joinpath("mechanism_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def process() -> None:
    ensure_dirs()
    records = read_metadata()
    rows: list[dict] = []
    handoff: list[str] = [
        "# Manual Download Handoff",
        "",
        "Items below need user-side ScienceDirect/Elsevier download or review.",
        "",
    ]
    seen_dois: set[str] = set()
    for record in records:
        doi_key = normalize_doi(record.get("doi", "")) or record.get("url", "")
        if doi_key in seen_dois:
            continue
        seen_dois.add(doi_key)
        record["fuelType"] = record.get("fuelType") or detect_fuel(record)
        candidate = record.get("candidate")
        if candidate is None:
            candidate = is_candidate(record)
        folder = record_folder(record)
        local_downloads = copy_downloads_for_record(record, folder / "raw_downloads")
        extracted_dest = folder / "extracted"
        extraction_notes = extract_archives(local_downloads, extracted_dest)
        scan_roots = [folder / "raw_downloads", extracted_dest]
        mechanisms, thermos, transports, cantera = scan_files(scan_roots)
        ck_results: list[CkResult] = []
        if mechanisms:
            if not record.get("paperPdfStatus"):
                record["paperPdfStatus"] = "pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed"
            for mech in mechanisms:
                thermo = find_thermo_for(mech, thermos + mechanisms)
                ck_results.append(run_ckinterp(mech, thermo, folder))
            write_summary(record, folder, mechanisms, thermos, transports, ck_results, extraction_notes)
        elif cantera:
            folder.mkdir(parents=True, exist_ok=True)
            if not record.get("paperPdfStatus"):
                record["paperPdfStatus"] = "pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed"
            write_summary(record, folder, cantera, thermos, transports, [], extraction_notes + ["Cantera file detected; ckinterp skipped"])
        elif candidate:
            handoff.extend(
                [
                    f"## {record.get('title', 'Untitled')}",
                    "",
                    f"- DOI: {record.get('doi', '')}",
                    f"- URL: {record.get('url', '')}",
                    f"- Reason: no local downloadable mechanism supplement detected yet",
                    f"- Suggested folder: {folder}",
                    "",
                ]
            )
        status = "included" if mechanisms or cantera else ("pending_download" if candidate else "excluded_no_mechanism_signal")
        if status == "included" and not record.get("paperPdfLocal"):
            handoff.extend(
                [
                    f"## Paper PDF pending: {record.get('title', 'Untitled')}",
                    "",
                    f"- DOI: {record.get('doi', '')}",
                    f"- URL: {record.get('url', '')}",
                    f"- PDF link from issue page: {record.get('issuePdfLink', '')}",
                    "- Reason: automated Chrome PDF access reached ScienceDirect CAPTCHA or no exact PDF link was exposed",
                    f"- Target folder: {folder}",
                    "",
                ]
            )
        rows.append(
            {
                "title": record.get("title", ""),
                "authors": "; ".join(record.get("authors", [])) if isinstance(record.get("authors"), list) else record.get("authors", ""),
                "doi": record.get("doi", ""),
                "pii": record.get("pii", ""),
                "volume": record.get("volume", ""),
                "month": record.get("month", ""),
                "article_number": article_id(record),
                "fuel_type": record.get("fuelType", ""),
                "url": record.get("url", ""),
                "paper_pdf_link": record.get("issuePdfLink", ""),
                "paper_pdf_status": record.get("paperPdfStatus", ""),
                "candidate": str(bool(candidate)),
                "status": status,
                "folder": str(folder if (mechanisms or cantera) else ""),
                "mechanism_files": "; ".join(str(p) for p in mechanisms + cantera),
                "thermo_files": "; ".join(str(p) for p in thermos),
                "transport_files": "; ".join(str(p) for p in transports),
                "species": ck_results[0].species if ck_results else "",
                "reactions": ck_results[0].reactions if ck_results else "",
                "ck_status": ck_results[0].status if ck_results else "",
            }
        )
    with ROOT.joinpath("collection_index.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()) if rows else ["title"])
        writer.writeheader()
        writer.writerows(rows)
    ROOT.joinpath("manual_download_handoff.md").write_text("\n".join(handoff) + "\n", encoding="utf-8")
    ROOT.joinpath("run_summary.json").write_text(
        json.dumps(
            {
                "updated_at": dt.datetime.now().isoformat(timespec="seconds"),
                "metadata_records": len(records),
                "index_rows": len(rows),
                "included": sum(1 for r in rows if r["status"] == "included"),
                "pending_download": sum(1 for r in rows if r["status"] == "pending_download"),
                "root": str(ROOT),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )


def init() -> None:
    ensure_dirs()
    if not METADATA_JSON.exists():
        write_metadata([])
    README = ROOT / "README.md"
    if not README.exists():
        README.write_text(
            textwrap.dedent(
                f"""\
                # Combustion and Flame 2026 Mechanism Collection

                This directory stores the automated collection output.

                - Metadata: `{METADATA_JSON}`
                - Raw browser downloads: `{DOWNLOADS}`
                - Index: `{ROOT / "collection_index.csv"}`
                - Manual download handoff: `{ROOT / "manual_download_handoff.md"}`
                """
            ),
            encoding="utf-8",
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["init", "enrich-crossref", "probe-supplements", "process"])
    parser.add_argument("--max-mmc", type=int, default=8)
    args = parser.parse_args()
    if args.command == "init":
        init()
    elif args.command == "enrich-crossref":
        enrich_crossref()
    elif args.command == "probe-supplements":
        probe_supplements(max_mmc=args.max_mmc)
    elif args.command == "process":
        process()


if __name__ == "__main__":
    main()

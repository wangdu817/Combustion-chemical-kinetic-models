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
import gc
import html
import json
import os
import re
import shutil
import sys
import subprocess
import tarfile
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional, Iterable


WORKSPACE = Path(os.environ.get("MECH_COLLECTION_WORKSPACE", Path(__file__).resolve().parents[1])).resolve()
LEGACY_ROOT = WORKSPACE / "combustion_and_flame_2026_mechanisms"
ROOT = Path(os.environ.get("MECH_COLLECTION_ROOT", WORKSPACE / "combustion_and_flame_mechanisms")).resolve()
RAW = ROOT / "_raw"
DOWNLOADS = RAW / "downloads"
EXTRACTED = RAW / "extracted"
METADATA_JSON = RAW / "article_metadata.json"
LEGACY_METADATA_JSON = LEGACY_ROOT / "_raw" / "article_metadata.json"
LEGACY_DOWNLOADS = LEGACY_ROOT / "_raw" / "downloads"
PROCESSING_ARCHIVE = ROOT / "_processing_archive"
CKDIR = Path(r"D:\BaiduSyncdisk\soft\CoFlame_yang")
CKEXE = CKDIR / "ckinterp.exe"
CK_FILES = ["chem.inp", "therm.dat", "chem.out"]
_venv_python = Path(__file__).resolve().parents[1] / ".venv" / "bin" / "python"
if not _venv_python.exists():
    _venv_python = WORKSPACE / ".venv" / "bin" / "python"
_default_py = str(_venv_python) if _venv_python.exists() else sys.executable
ANALYSIS_PYTHON = Path(os.environ.get("MECH_COLLECTION_PYTHON", _default_py))  # no .resolve() — keep venv symlink
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

INDEX_FIELDS = [
    "title",
    "authors",
    "doi",
    "pii",
    "volume",
    "month",
    "article_number",
    "fuel_type",
    "plasma_related",
    "url",
    "paper_pdf_link",
    "paper_pdf_status",
    "candidate",
    "status",
    "folder",
    "mechanism_files",
    "thermo_files",
    "transport_files",
    "standard_mechanism",
    "standard_thermo",
    "standard_transport",
    "cantera_yaml",
    "species",
    "reactions",
    "preprocess_status",
]

ACTIVE_STATUSES = {"included", "conversion_failed"}
TERMINAL_PROCESSING_STATUSES = ACTIVE_STATUSES | {
    "excluded_non_kinetics_mechanism_attachment",
    "excluded_no_mechanism_attachment",
    "excluded_no_supplement_found",
    "excluded_no_mechanism_signal",
}

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

REACTION_KINETICS_INCLUDE_PATTERNS = [
    r"chemical kinetic",
    r"\bkinetic (model|modeling|modelling|study|analysis|mechanism|insight|investigation|simulation)",
    r"\bkinetics of\b",
    r"\bkinetic inhibition\b",
    r"\bkinetic coupling\b",
    r"\boxidation kinetics\b",
    r"\bpyrolysis kinetics\b",
    r"\bcombustion kinetics\b",
    r"\breaction mechanism\b",
    r"\bdetailed kinetic\b",
    r"\bmechanism development\b",
    r"\bexperimental and modeling study\b",
    r"\bdetailed and reduced kinetics\b",
    r"\bcarbon.?nitrogen interaction reactions\b",
    r"\bmodel development and validation\b",
    r"\bauto-?ignition\b",
    r"\bignition delay\b",
    r"\blaminar burning velocit",
    r"\blaminar flame speed\b",
    r"\bjet-?stirred reactor\b",
    r"\bshock tube\b",
    r"\brapid compression machine\b",
    r"\bflow reactor\b",
    r"\bflame speed measurements\b",
]

REACTION_KINETICS_EXCLUDE_PATTERNS = [
    r"thermoacoustic",
    r"instability mechanism",
    r"feedback mechanism",
    r"heat transfer mechanism",
    r"flame spread",
    r"flame quenching",
    r"suppression",
    r"dust explosion",
    r"porous medium",
    r"scramjet",
    r"combustion transition mechanisms",
    r"turbulence characteristics",
    r"spray flame",
    r"genetic programming control",
    r"nanoparticle synthesis",
    r"aluminum combustion",
    r"single al\b",
    r"al-li alloy particle",
    r"burning rate constant of pmma",
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
    # Nitrogen-containing
    (r"\bNH\s*3\b|ammonia", "ammonia"),
    (r"nitric oxide|\bNO\b removal|\bNOx\b", "nitric_oxide"),
    (r"N\s*2\s*O|nitrous oxide", "n2o"),
    (r"nitromethane", "nitromethane"),
    (r"methylamine", "methylamine"),
    (r"butyl nitrite|butylnitrite", "butyl_nitrite"),
    (r"N-methyl aniline|N-methylaniline", "n_methyl_aniline"),
    (r"ammonium nitrate", "ammonium_nitrate"),
    (r"ammonium chloride", "ammonium_chloride"),
    (r"pyridine", "pyridine"),
    (r"pyrrole", "pyrrole"),
    # Alkanes
    (r"\bmethane\b|\bCH\s*4\b", "methane"),
    (r"\bethane\b|\bC\s*2\s*H\s*6\b", "ethane"),
    (r"propane", "propane"),
    (r"n-?butane|\bbutane\b", "n_butane"),
    (r"pentane", "pentane"),
    (r"n-?heptane|heptane", "n_heptane"),
    (r"iso-?octane|isooctane|2,2,4-trimethylpentane", "iso_octane"),
    (r"n-?octane|\boctane\b", "n_octane"),
    (r"n-?decane|\bdecane\b", "n_decane"),
    (r"n-?dodecane|dodecane", "n_dodecane"),
    (r"n-?hexadecane|hexadecane|cetane", "n_hexadecane"),
    (r"triptane|2,2,3-trimethylbutane", "triptane"),
    # Alkenes and alkynes
    (r"ethylene|C\s*2\s*H\s*4", "ethylene"),
    (r"acetylene", "acetylene"),
    (r"propene|propylene", "propene"),
    (r"1-?butene|butene", "1_butene"),
    (r"1-?pentene|pentene", "pentene"),
    (r"1-?hexene|hexene", "hexene"),
    (r"1-?heptene|heptene", "heptene"),
    # Cyclic hydrocarbons
    (r"cyclohexane", "cyclohexane"),
    (r"cyclohexene", "cyclohexene"),
    (r"ethylcyclohexane", "ethylcyclohexane"),
    (r"cyclopentane", "cyclopentane"),
    (r"cyclopentene", "cyclopentene"),
    (r"cyclopentanone", "cyclopentanone"),
    (r"norbornane", "norbornane"),
    (r"quadricyclane", "quadricyclane"),
    # Aromatics
    (r"benzene", "benzene"),
    (r"toluene", "toluene"),
    (r"ethylbenzene", "ethylbenzene"),
    (r"xylene|dimethylbenzene", "xylene"),
    (r"n-?butylbenzene|butylbenzene", "n_butylbenzene"),
    (r"n-?propylbenzene|propylbenzene", "n_propylbenzene"),
    (r"1,2,4-trimethylbenzene|trimethylbenzene", "trimethylbenzene_124"),
    (r"3-?ethyltoluene", "3_ethyltoluene"),
    (r"3-?n-?propyltoluene", "3_n_propyltoluene"),
    (r"cumene|isopropylbenzene", "cumene"),
    (r"indene", "indene"),
    (r"naphthalene", "naphthalene"),
    (r"styrene", "styrene"),
    # Alcohols
    (r"methanol", "methanol"),
    (r"ethanol", "ethanol"),
    (r"propan-?1-?ol|1-?propanol|propanol", "propanol"),
    (r"butanol|1-?butanol|n-?butanol", "butanol"),
    (r"pentanol|secondary pentanols|2- and 3-pentanol|2-pentanol|3-pentanol", "pentanol"),
    # Ethers
    (r"dimethyl[ -]?ether|\bDME\b", "dimethyl_ether"),
    (r"diethyl ether", "diethyl_ether"),
    (r"dimethoxymethane|\bDMM\b", "dimethoxymethane"),
    (r"1,?2-?dimethoxyethane", "dimethoxyethane"),
    (r"ethyl tert-?butyl ether|\bETBE\b", "etbe"),
    (r"methyl tert-?butyl ether|\bMTBE\b", "mtbe"),
    # Esters
    (r"methyl formate", "methyl_formate"),
    (r"ethyl formate", "ethyl_formate"),
    (r"methyl acetate", "methyl_acetate"),
    (r"ethyl acetate", "ethyl_acetate"),
    (r"dimethyl carbonate", "dimethyl_carbonate"),
    (r"methyl butanoate|methyl butyrate", "methyl_butanoate"),
    (r"biodiesel|FAME|fatty acid methyl ester", "biodiesel"),
    # Ketones
    (r"acetone", "acetone"),
    (r"2-?butanone|butanone|methyl ethyl ketone", "2_butanone"),
    (r"cyclopentanone", "cyclopentanone"),
    # Aldehydes
    (r"formaldehyde", "formaldehyde"),
    (r"acetaldehyde", "acetaldehyde"),
    (r"benzaldehyde", "benzaldehyde"),
    # Furans
    (r"furan", "furan"),
    (r"tetrahydrofuran|\bTHF\b", "tetrahydrofuran"),
    (r"2-?methylfuran", "2_methylfuran"),
    (r"2,5-dimethylfuran|\bDMF\b", "dimethylfuran"),
    # Peroxides
    (r"di-tert-?butyl peroxide|\bDTBP\b", "dtbp"),
    (r"hydrogen peroxide", "hydrogen_peroxide"),
    # Energetic materials
    (r"CL-?20|hexanitrohexaazaisowurtzitane", "cl20"),
    # Practical fuels
    (r"gasoline", "gasoline"),
    (r"diesel", "diesel"),
    (r"jet fuel|Jet-?A|kerosene", "jet_fuel"),
    (r"RP-?3", "rp3"),
    (r"naphtha", "naphtha"),
    (r"gas to liquid jet fuel|gas-to-liquid jet fuel|\bGTL\b", "gtl_jet_fuel"),
    (r"sustainable aviation fuel|\bSAF\b", "saf"),
    # Other
    (r"\bH\s*2\b|hydrogen", "hydrogen"),
    (r"syngas|synthesis gas", "syngas"),
    (r"dimethyl carbonate", "dimethyl_carbonate"),
    (r"HCFO-?1233xf", "hcfo_1233xf"),
    (r"2-?ethylhexyl nitrate|\bEHN\b", "2_ethylhexyl_nitrate"),
    (r"coal", "coal"),
    (r"magnesium", "magnesium"),
    (r"iron", "iron"),
    (r"aluminum|aluminium", "aluminum"),
    (r"polyoxymethylene|\bPOM\b", "polyoxymethylene"),
    (r"nitrocellulose", "nitrocellulose"),
    # Generic fallbacks
    (r"PAH|polycyclic aromatic hydrocarbon", "pah"),
    (r"alkane", "alkane"),
    (r"alkene", "alkene"),
    (r"biofuel|bio-fuel", "biofuel"),
    (r"methyl palmitate|methyl stearate|methyl oleate", "methyl_ester"),
    (r"methyl isocyanate", "methyl_isocyanate"),
    (r"p-?cymene", "p_cymene"),
    (r"formic acid", "formic_acid"),
    (r"\\bsilane\\b", "silane"),
    (r"di-n-propyl ether|di-n-propylether|\\bDPE\\b", "di_n_propyl_ether"),
    (r"allene|propyne|propargyl", "allene_propyne"),
    (r"1,3-?butadiene|butadiene", "butadiene"),
    (r"R-?32|\\bCH2F2\\b|difluoromethane", "r32"),
    (r"\\bRDX\\b|trinitro-triazinane|hexogen", "rdx"),
    (r"pyrene", "pyrene"),
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
    source = METADATA_JSON if METADATA_JSON.exists() else LEGACY_METADATA_JSON
    if not source.exists():
        return []
    records = json.loads(source.read_text(encoding="utf-8-sig"))
    if source == LEGACY_METADATA_JSON and not METADATA_JSON.exists():
        write_metadata(records)
    return records


def write_metadata(records: list[dict]) -> None:
    ensure_dirs()
    METADATA_JSON.write_text(
        json.dumps(records, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def now_iso() -> str:
    return dt.datetime.now().isoformat(timespec="seconds")


def supplement_links_for_record(record: dict) -> list[dict]:
    links = record.get("probedSupplementLinks") or record.get("supplementLinks") or []
    return [link for link in links if isinstance(link, dict)]


def existing_index_rows() -> dict[str, dict[str, str]]:
    index = ROOT / "collection_index.csv"
    if not index.exists():
        return {}
    with index.open("r", newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    return {row.get("article_number", ""): row for row in rows if row.get("article_number")}


def clean_index_row(row: dict[str, str]) -> dict[str, str]:
    return {field: str(row.get(field, "") or "") for field in INDEX_FIELDS}


def seed_processing_state_from_index(record: dict, row: dict[str, str] | None) -> bool:
    if not row:
        return False
    changed = False
    mappings = {
        "processingStatus": "status",
        "processingFolder": "folder",
        "processingSpecies": "species",
        "processingReactions": "reactions",
        "processingPreprocessStatus": "preprocess_status",
        "processingMechanismFiles": "mechanism_files",
        "processingThermoFiles": "thermo_files",
        "processingTransportFiles": "transport_files",
        "processingCanteraYaml": "cantera_yaml",
        "processingStandardMechanism": "standard_mechanism",
        "processingStandardThermo": "standard_thermo",
        "processingStandardTransport": "standard_transport",
    }
    for record_key, row_key in mappings.items():
        if not record.get(record_key) and row.get(row_key):
            record[record_key] = row[row_key]
            changed = True
    return changed


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


def record_year(record: dict) -> str:
    for key in ("year", "publicationYear", "coverYear"):
        value = str(record.get(key, "") or "").strip()
        if re.fullmatch(r"\d{4}", value):
            return value
    # DOI registration strings can contain the prior online year even when the
    # article belongs to the 2026 journal volume, so do not derive folder years
    # from DOI text.
    return "2026"


def normalize_record_years(records: list[dict], default_year: str = "2026") -> bool:
    changed = False
    for record in records:
        if not record.get("year"):
            record["year"] = default_year
            changed = True
    return changed


def detect_fuel(record: dict) -> str:
    def scan(text: str) -> list[str]:
        found_labels: list[str] = []
        for pattern, label in FUEL_PATTERNS:
            if re.search(pattern, text, flags=re.I):
                if label not in found_labels:
                    found_labels.append(label)
        return found_labels

    found = scan(str(record.get("title", "")))
    if not found:
        found = scan(str(record.get("keywords", "")))
    if not found:
        abstract = str(record.get("abstract", ""))
        if abstract.strip():
            found = scan(abstract[:2000])  # scan full abstract
    if not found:
        return "unknown_fuel"
    return "_".join(found[:4])


def is_candidate(record: dict) -> bool:
    text = (str(record.get("title", "")) + " " + str(record.get("abstract", ""))).lower()
    return any(term in text for term in KINETIC_TERMS)


def is_reaction_kinetics_candidate(record: dict) -> bool:
    text = (str(record.get("title", "")) + " " + str(record.get("abstract", ""))).lower()
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    if any(re.search(pattern, text) for pattern in REACTION_KINETICS_EXCLUDE_PATTERNS):
        if not any(re.search(pattern, text) for pattern in [r"chemical kinetic", r"\bkinetic (model|modeling|modelling)", r"\breaction mechanism\b"]):
            return False
    if any(re.search(pattern, text) for pattern in REACTION_KINETICS_INCLUDE_PATTERNS):
        return True
    fuel = detect_fuel(record)
    if fuel != "unknown_fuel" and any(term in text for term in ["pyrolysis", "oxidation", "autoignition", "combustion kinetics"]):
        return True
    if fuel != "unknown_fuel" and "formation" in text and any(term in text for term in ["products", "pah", "polycyclic", "nitrogen-containing"]):
        return True
    chemistry_context = any(term in text for term in ["oxidation", "pyrolysis", "combustion", "autoignition", "flame speed"])
    modeling_context = any(term in text for term in ["kinetic", "kinetics", "modeling", "modelling", "mechanism"])
    reactor_context = any(term in text for term in ["shock tube", "jet-stirred", "jet stirred", "flow reactor", "rapid compression", "rcm"])
    return chemistry_context and modeling_context and reactor_context


def record_folder(record: dict) -> Path:
    fuel = record.get("fuelType") or detect_fuel(record)
    year = record_year(record)
    authors = record.get("authors") or []
    if isinstance(authors, str):
        first_author = authors.split(",")[0].strip()
    elif authors:
        first_author = str(authors[0]).strip()
    else:
        first_author = "unknown"
    surname = first_author_surname(first_author)
    fuel_slug = slugify(fuel, 60)
    name = f"{slugify(surname, 24)}_{year}_{fuel_slug}_{article_id(record)}"
    return ROOT / fuel_slug / year / name


def legacy_processing_folder(record: dict) -> Path:
    fuel = slugify(record.get("fuelType") or detect_fuel(record), 60)
    year = record_year(record)
    return PROCESSING_ARCHIVE / year / fuel / record_folder(record).name


def processing_folder(record: dict) -> Path:
    return record_folder(record) / "_processing"


def first_author_surname(author: str) -> str:
    author = re.sub(r"<[^>]+>", "", author or "").strip()
    author = re.sub(r"\s+", " ", author)
    if not author:
        return "unknown"
    if "," in author:
        return author.split(",", 1)[0].strip() or "unknown"
    tokens = [token for token in re.split(r"\s+", author) if token]
    return tokens[-1] if tokens else "unknown"


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
            return data.decode(enc, errors="ignore").lstrip("\ufeff")
        except UnicodeDecodeError:
            continue
    return data.decode("latin-1", errors="ignore").lstrip("\ufeff")


def looks_like_transport_table(text: str) -> bool:
    upper = text.upper()
    if "ENDDIFF" in upper:
        return True
    table_lines = 0
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("!", "#")):
            continue
        if re.match(r"^[A-Za-z0-9_()+,\-*.]+\s+[0-2]\s+[-+0-9.Ee]+\s+[-+0-9.Ee]+\s+[-+0-9.Ee]+", stripped):
            table_lines += 1
            if table_lines >= 5:
                return True
    return False


def classify_file(path: Path) -> set[str]:
    if not path.is_file() or not looks_like_text(path):
        return set()
    text = read_text_limited(path)
    upper = text.upper()
    labels: set[str] = set()
    if "SPECIES CONSIDERED" in upper or "REACTIONS CONSIDERED" in upper:
        return labels
    if re.search(r"(^|\n)\s*ELEMENTS\b", upper) and re.search(r"(^|\n)\s*SPECIES\b", upper):
        labels.add("chemkin_mechanism")
    if re.search(r"(^|\n)\s*REACTIONS(?!\s+CONSIDERED)\b", upper):
        labels.add("reactions")
        labels.add("chemkin_mechanism")
    if re.search(r"(^|\n)\s*THERMO\b", upper):
        labels.add("thermo")
    if re.search(r"(^|\n)\s*TRANSPORT\b", upper) or looks_like_transport_table(text):
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


def archive_kind(path: Path) -> str:
    try:
        header = path.read_bytes()[:8]
    except OSError:
        return ""
    suffix = path.suffix.lower()
    if header.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")):
        return "zip"
    if header.startswith(b"\x1f\x8b"):
        return "gzip"
    if header.startswith(b"7z\xbc\xaf\x27\x1c"):
        return "7z"
    if header.startswith((b"Rar!\x1a\x07\x00", b"Rar!\x1a\x07\x01\x00")):
        return "rar"
    if suffix in {".zip", ".docx"}:
        return "zip"
    if suffix in {".tar", ".tgz", ".tar.gz", ".tbz2", ".tar.bz2", ".txz", ".tar.xz"} or tarfile.is_tarfile(path):
        return "tar"
    if suffix == ".gz":
        return "gzip"
    if suffix == ".7z":
        return "7z"
    if suffix == ".rar":
        return "rar"
    return ""


def safe_extract_gzip(path: Path, dest: Path) -> Path:
    import gzip

    target_name = path.stem or (path.name + ".out")
    target = (dest / target_name).resolve()
    if not str(target).startswith(str(dest.resolve())):
        raise ValueError(f"unsafe gzip output path: {target_name}")
    target.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(path, "rb") as src, target.open("wb") as out:
        shutil.copyfileobj(src, out)
    return target


def safe_extract_with_7z(path: Path, dest: Path) -> bool:
    exe = shutil.which("7z") or shutil.which("7za") or shutil.which("7zr")
    if not exe:
        return False
    completed = subprocess.run(
        [exe, "x", "-y", f"-o{dest}", str(path)],
        text=True,
        capture_output=True,
        timeout=120,
    )
    if completed.returncode != 0:
        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
    return True


def extract_archives(files: Iterable[Path], dest: Path, max_depth: int = 5) -> list[str]:
    notes: list[str] = []
    dest.mkdir(parents=True, exist_ok=True)
    queue: list[tuple[Path, int]] = [(path, 0) for path in files]
    seen: set[Path] = set()
    while queue:
        path, depth = queue.pop(0)
        if depth > max_depth:
            notes.append(f"skip nested archive beyond depth {max_depth}: {path.name}")
            continue
        resolved = path.resolve()
        if resolved in seen or not path.exists() or not path.is_file():
            continue
        seen.add(resolved)
        kind = archive_kind(path)
        if not kind:
            continue
        out = dest / slugify(path.stem, 80)
        try:
            before = {p.resolve() for p in out.rglob("*")} if out.exists() else set()
            if kind == "zip":
                out.mkdir(parents=True, exist_ok=True)
                safe_extract_zip(path, out)
                notes.append(f"extracted {path.name}")
            elif kind == "tar":
                out.mkdir(parents=True, exist_ok=True)
                safe_extract_tar(path, out)
                notes.append(f"extracted {path.name}")
            elif kind == "gzip":
                out.mkdir(parents=True, exist_ok=True)
                safe_extract_gzip(path, out)
                notes.append(f"extracted {path.name}")
            elif kind in {"rar", "7z"}:
                out.mkdir(parents=True, exist_ok=True)
                if safe_extract_with_7z(path, out):
                    notes.append(f"extracted {path.name}")
                else:
                    notes.append(f"unsupported archive without 7z: {path.name}")
                    continue
            after = {p.resolve() for p in out.rglob("*")} if out.exists() else set()
            for nested in sorted(after - before):
                if nested.is_file() and archive_kind(nested):
                    queue.append((nested, depth + 1))
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


def find_transport_for(mech: Path, candidates: list[Path]) -> Path | None:
    scored: list[tuple[int, Path]] = []
    for path in candidates:
        cls = classify_file(path)
        if "transport" in cls:
            score = 10
            name = path.name.lower()
            if "tran" in name or "transport" in name:
                score += 5
            if path.parent == mech.parent:
                score += 3
            scored.append((score, path))
    return sorted(scored, reverse=True)[0][1] if scored else None


def detect_plasma_case(record: dict, files: Iterable[Path] = ()) -> str:
    text_parts = [
        str(record.get("title", "")),
        str(record.get("abstract", "")),
        str(record.get("keywords", "")),
    ]
    file_text_parts: list[str] = []
    for path in files:
        if path.is_file() and looks_like_text(path):
            file_text_parts.append(read_text_limited(path, 300_000))
    text_parts.extend(file_text_parts)
    text = "\n".join(text_parts)
    if re.search(r"\b(plasma|dielectric barrier|dbd|nanosecond discharge|glow discharge|electron[-\s]?impact)\b", text, re.I):
        return "yes"
    file_text = "\n".join(file_text_parts)
    if re.search(r"(?m)^\s*(E|E-|e-)\s", file_text) and re.search(r"(?m)^\s*[A-Za-z0-9_()+\-]+\+\s", file_text):
        return "possible"
    return "no"


def short_message(value: str, limit: int = 800) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if len(value) <= limit:
        return value
    return value[:limit].rstrip() + " ... [truncated; see _processing logs]"


def mechanism_priority(path: Path) -> tuple[int, str]:
    name = path.name.lower()
    score = 0
    if path.suffix.lower() in {".inp", ".dat", ".txt", ".yaml", ".yml", ".cti"}:
        score -= 20
    if "mech" in name or "mechanism" in name or "model" in name:
        score -= 10
    if "therm" in name or "tran" in name or "transport" in name:
        score += 20
    if "document.xml" in name or path.suffix.lower() == ".xml":
        score += 50
    return score, str(path)


@dataclass
class CkResult:
    status: str
    species: str = ""
    reactions: str = ""
    message: str = ""
    chem_out: Path | None = None
    cantera_yaml: Path | None = None
    method: str = ""
    standardized_mech: Path | None = None
    standardized_thermo: Path | None = None
    standardized_transport: Path | None = None


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


def parse_cantera_yaml_counts(path: Path) -> tuple[str, str]:
    if not path.exists():
        return "", ""
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(path.read_text(encoding="utf-8", errors="ignore")) or {}
        species = data.get("species") or []
        reactions = data.get("reactions") or []
        species_count = str(len(species)) if isinstance(species, list) and species else ""
        reaction_count = str(len(reactions)) if isinstance(reactions, list) and reactions else ""
        if species_count or reaction_count:
            return species_count, reaction_count
    except Exception:
        pass

    text = path.read_text(encoding="utf-8", errors="ignore").splitlines()
    counts = {"species": 0, "reactions": 0}
    section: str | None = None
    phase_species_tokens: list[str] = []
    collecting_phase_species = False
    phase_species_text = ""
    for line in text:
        if re.match(r"^[A-Za-z0-9_-]+:", line):
            section = None
        stripped = line.strip()
        if collecting_phase_species:
            phase_species_text += " " + stripped
            if "]" in stripped:
                inside = phase_species_text.split("[", 1)[1].split("]", 1)[0]
                phase_species_tokens.extend(item.strip() for item in inside.split(",") if item.strip())
                collecting_phase_species = False
                phase_species_text = ""
            continue
        if stripped.startswith("species:") and line.startswith(" "):
            if "[" in stripped:
                phase_species_text = stripped
                if "]" in stripped:
                    inside = stripped.split("[", 1)[1].split("]", 1)[0]
                    phase_species_tokens.extend(item.strip() for item in inside.split(",") if item.strip())
                    phase_species_text = ""
                else:
                    collecting_phase_species = True
            continue
        if line.startswith("species:"):
            section = "species"
            if "[" in line and "]" in line:
                inside = line.split("[", 1)[1].split("]", 1)[0]
                counts["species"] += len([item for item in inside.split(",") if item.strip()])
            continue
        if line.startswith("reactions:"):
            section = "reactions"
            continue
        if section in counts and re.match(r"^\s*-\s+", line):
            counts[section] += 1
    species_count = counts["species"] or len(dict.fromkeys(phase_species_tokens))
    return (str(species_count) if species_count else "", str(counts["reactions"]) if counts["reactions"] else "")


def first_chemkin_header_line(path: Path) -> int | None:
    lines = read_text_limited(path, 5_000_000).splitlines()
    for idx, line in enumerate(lines):
        stripped = line.strip().upper()
        if stripped.startswith(("ELEMENTS", "SPECIES", "THERMO", "REACTIONS")):
            return idx
    return None


def write_trimmed_chemkin_input(source: Path, target: Path) -> bool:
    text = read_text_limited(source, 20_000_000)
    lines = text.splitlines()
    start = first_chemkin_header_line(source)
    if start is None:
        return False
    trimmed = "\n".join(lines[start:]).lstrip() + "\n"
    if "SPECIES CONSIDERED" in trimmed.upper() or "REACTIONS CONSIDERED" in trimmed.upper():
        return False
    target.write_text(trimmed, encoding="utf-8")
    return True


def write_cantera_cleaned_chemkin_input(source: Path, target: Path) -> bool:
    text = read_text_limited(source, 50_000_000)
    if "SPECIES CONSIDERED" in text.upper() or "REACTIONS CONSIDERED" in text.upper():
        return False
    lines = text.splitlines()
    start = first_chemkin_header_line(source)
    if start is not None:
        lines = lines[start:]
    cleaned_lines: list[str] = []
    exponent_pattern = re.compile(r"(?<![A-Za-z0-9_])([+-]?(?:\d+\.\d*|\.\d+|\d+))([+-]\d{1,3})(?![A-Za-z0-9_.])")
    for raw in lines:
        line = raw.replace("\ufeff", "")
        line = re.sub(r"(?<=\d),(?=\s|$)", "", line)
        line = exponent_pattern.sub(r"\1E\2", line)
        cleaned_lines.append(line)
    target.write_text("\n".join(cleaned_lines).lstrip() + "\n", encoding="utf-8")
    return True


def standardize_mechanism_files(mech: Path, thermo: Path | None, transport: Path | None, dest: Path) -> tuple[Path, Path | None, Path | None]:
    dest.mkdir(parents=True, exist_ok=True)
    chem_target = dest / "chem.inp"
    thermo_target = dest / "therm.dat"
    transport_target = dest / "tran.dat"
    shutil.copy2(mech, chem_target)
    thermo_out = None
    transport_out = None
    if thermo is not None and thermo.exists():
        shutil.copy2(thermo, thermo_target)
        thermo_out = thermo_target
    elif thermo_target.exists():
        thermo_target.unlink()
    if transport is not None and transport.exists():
        shutil.copy2(transport, transport_target)
        transport_out = transport_target
    elif transport_target.exists():
        transport_target.unlink()
    return chem_target, thermo_out, transport_out


def cantera_convert_once(
    mech: Path,
    thermo: Path | None,
    transport: Path | None,
    out_yaml: Path,
    log_path: Path,
    result_path: Path | None = None,
) -> tuple[bool, str, str, str]:
    result_path = result_path or log_path.with_suffix(".result.json")
    result_path.parent.mkdir(parents=True, exist_ok=True)
    if result_path.exists():
        result_path.unlink()
    code = r"""
import json
import sys
import traceback
from pathlib import Path

import cantera as ct
import cantera.ck2yaml as ck2yaml

mech = Path(sys.argv[1])
thermo = Path(sys.argv[2]) if sys.argv[2] else None
transport = Path(sys.argv[3]) if sys.argv[3] else None
out_yaml = Path(sys.argv[4])
result_path = Path(sys.argv[5])

payload = {"ok": False, "species": "", "reactions": "", "message": ""}
try:
    suffix = mech.suffix.lower()
    if suffix in {".yaml", ".yml", ".cti"} and thermo is None:
        if suffix in {".yaml", ".yml"}:
            if mech.resolve() != out_yaml.resolve():
                out_yaml.write_text(mech.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
            gas = ct.Solution(str(out_yaml))
        else:
            gas = ct.Solution(str(mech))
    else:
        if hasattr(ck2yaml, "convert_mech"):
            ck2yaml.convert_mech(
                str(mech),
                thermo_file=str(thermo) if thermo else None,
                transport_file=str(transport) if transport else None,
                out_name=str(out_yaml),
                quiet=False,
                permissive=True,
            )
        else:
            ck2yaml.convert(
                str(mech),
                thermo_file=str(thermo) if thermo else None,
                transport_file=str(transport) if transport else None,
                out_name=str(out_yaml),
                quiet=False,
                permissive=True,
            )
        gas = ct.Solution(str(out_yaml))
    payload.update({"ok": True, "species": str(gas.n_species), "reactions": str(gas.n_reactions), "message": "cantera conversion ok"})
except Exception as exc:
    payload["message"] = f"{type(exc).__name__}: {exc}"
    payload["traceback"] = traceback.format_exc()
finally:
    result_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
"""
    try:
        completed = subprocess.run(
            [str(ANALYSIS_PYTHON), "-c", code, str(mech), str(thermo or ""), str(transport or ""), str(out_yaml), str(result_path)],
            text=True,
            capture_output=True,
            timeout=900,
        )
    except subprocess.TimeoutExpired as exc:
        log_path.write_text(
            f"Cantera conversion timed out after {exc.timeout} seconds.\nCOMMAND: {exc.cmd}\n",
            encoding="utf-8",
        )
        return False, "", "", f"TimeoutExpired: Cantera conversion exceeded {exc.timeout} seconds"
    log_path.write_text(
        "PERMISSIVE: True\nSTDOUT:\n" + completed.stdout + "\nSTDERR:\n" + completed.stderr + f"\nRETURN_CODE: {completed.returncode}\n",
        encoding="utf-8",
    )
    if result_path.exists():
        payload = json.loads(result_path.read_text(encoding="utf-8"))
    else:
        payload = {"ok": False, "species": "", "reactions": "", "message": "missing cantera result json"}
    return bool(payload.get("ok")), str(payload.get("species", "")), str(payload.get("reactions", "")), str(payload.get("message", ""))


def process_with_cantera(mech: Path, thermo: Path | None, transport: Path | None, dest: Path, work_dest: Path | None = None) -> CkResult:
    chem_target, thermo_target, transport_target = standardize_mechanism_files(mech, thermo, transport, dest)
    work_dest = work_dest or dest
    work_dest.mkdir(parents=True, exist_ok=True)
    yaml_path = dest / "mechanism.yaml"
    log_path = work_dest / "cantera_conversion.log"
    if not ANALYSIS_PYTHON.exists():
        return CkResult(
            "cantera_failed",
            message=f"missing analysis python: {ANALYSIS_PYTHON}",
            standardized_mech=chem_target,
            standardized_thermo=thermo_target,
            standardized_transport=transport_target,
            method="cantera",
        )
    original_suffix = mech.suffix.lower()
    conversion_input = mech if original_suffix in {".yaml", ".yml", ".cti"} else chem_target
    ok, species, reactions, message = cantera_convert_once(conversion_input, None if original_suffix in {".yaml", ".yml", ".cti"} else thermo_target, transport_target, yaml_path, log_path)
    gc.collect()
    if ok:
        return CkResult(
            "ok",
            species=species,
            reactions=reactions,
            message=message,
            cantera_yaml=yaml_path,
            method="cantera",
            standardized_mech=chem_target,
            standardized_thermo=thermo_target,
            standardized_transport=transport_target,
        )
    if "Section starts with unrecognized keyword" in message:
        cleaned = work_dest / "chem_cantera_clean.inp"
        if write_trimmed_chemkin_input(chem_target, cleaned):
            clean_yaml = dest / "mechanism.cleaned.yaml"
            clean_log = work_dest / "cantera_conversion.cleaned.log"
            ok, species, reactions, clean_message = cantera_convert_once(cleaned, thermo_target, transport_target, clean_yaml, clean_log)
            if ok:
                shutil.copy2(cleaned, chem_target)
                shutil.copy2(clean_yaml, yaml_path)
                return CkResult(
                    "ok_after_cleanup",
                    species=species,
                    reactions=reactions,
                    message=f"cleaned leading non-CHEMKIN content; {clean_message}",
                    cantera_yaml=yaml_path,
                    method="cantera",
                    standardized_mech=chem_target,
                    standardized_thermo=thermo_target,
                    standardized_transport=transport_target,
                )
            message = f"{message}; cleanup retry failed: {clean_message}"
        else:
            message = f"{message}; cleanup skipped because file is not a CHEMKIN input"
    if any(token in message for token in ["could not convert string to float", "list index out of range", "Unexpected token"]):
        cleaned = work_dest / "chem_cantera_numeric_clean.inp"
        if write_cantera_cleaned_chemkin_input(chem_target, cleaned):
            clean_yaml = dest / "mechanism.numeric_clean.yaml"
            clean_log = work_dest / "cantera_conversion.numeric_clean.log"
            ok, species, reactions, clean_message = cantera_convert_once(cleaned, thermo_target, transport_target, clean_yaml, clean_log)
            if ok:
                shutil.copy2(cleaned, chem_target)
                shutil.copy2(clean_yaml, yaml_path)
                return CkResult(
                    "ok_after_cleanup",
                    species=species,
                    reactions=reactions,
                    message=f"normalized legacy numeric/reaction syntax; {clean_message}",
                    cantera_yaml=yaml_path,
                    method="cantera",
                    standardized_mech=chem_target,
                    standardized_thermo=thermo_target,
                    standardized_transport=transport_target,
                )
            message = f"{message}; numeric cleanup retry failed: {clean_message}"
    yaml_counts = parse_cantera_yaml_counts(yaml_path) if yaml_path.exists() else ("", "")
    return CkResult(
        "cantera_failed",
        species=yaml_counts[0],
        reactions=yaml_counts[1],
        message=message,
        cantera_yaml=yaml_path if yaml_path.exists() else None,
        method="cantera",
        standardized_mech=chem_target,
        standardized_thermo=thermo_target,
        standardized_transport=transport_target,
    )


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
            author_text += ", et al."
    else:
        author_text = str(authors)
    title = record.get("title", "").rstrip(".")
    volume = record.get("volume", "")
    month = record.get("month", "")
    article = article_id(record)
    doi = normalize_doi(record.get("doi", ""))
    year = record_year(record)
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
    seen: set[Path] = set()
    legacy_raw = legacy_processing_folder(record) / "raw_downloads"
    for source_dir in [DOWNLOADS, LEGACY_DOWNLOADS, legacy_raw]:
        if not source_dir.exists():
            continue
        for file in source_dir.glob("*"):
            if not file.is_file() or file.resolve() in seen:
                continue
            seen.add(file.resolve())
            low = file.name.lower()
            if any(key and key.replace("/", "_").replace(".", "_") in low for key in keys) or any(
                key and key in low for key in keys
            ):
                target = dest / file.name
                if not target.exists() or target.stat().st_size != file.stat().st_size:
                    shutil.copy2(file, target)
                copied.append(target)
    return copied


def cleanup_inactive_paper_folders(root: Path, active_folders: set[Path]) -> None:
    root = root.resolve()
    active = {path.resolve() for path in active_folders}
    if not root.exists():
        return
    candidate_dirs = {path.parent.resolve() for path in root.rglob("mechanism_summary.md")}
    candidate_dirs |= {path.parent.resolve() for path in root.rglob("chem.inp")}
    for path in list(root.rglob("raw_downloads")) + list(root.rglob("extracted")):
        if not path.is_dir():
            continue
        parent = path.parent
        candidate_dirs.add((parent.parent if parent.name == "_processing" else parent).resolve())
    candidate_dirs = sorted(candidate_dirs, key=lambda p: len(p.parts), reverse=True)
    for paper_dir in candidate_dirs:
        if paper_dir in active or root not in paper_dir.parents or any(part.startswith("_") for part in paper_dir.relative_to(root).parts):
            continue
        if paper_dir.exists():
            shutil.rmtree(paper_dir)
    for directory in sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
        if any(part.startswith("_") for part in directory.relative_to(root).parts):
            continue
        try:
            directory.rmdir()
        except OSError:
            pass


def cleanup_active_paper_folder(folder: Path) -> None:
    allowed_files = {"mechanism_summary.md", "chem.inp", "therm.dat", "tran.dat", "mechanism.yaml"}
    allowed_dirs = {"_processing"}
    if not folder.exists():
        return
    for child in list(folder.iterdir()):
        if child.is_dir():
            if child.name not in allowed_dirs:
                shutil.rmtree(child)
            continue
        if child.name not in allowed_files:
            child.unlink()


def url_head(url: str) -> tuple[int, str, int]:
    req = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req, timeout=8) as response:
        length = response.headers.get("content-length") or "0"
        return response.status, response.headers.get("content-type") or "", int(length)


def url_download(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    tmp = dest.with_suffix(dest.suffix + ".part")
    try:
        with urllib.request.urlopen(req, timeout=30) as response, tmp.open("wb") as out:
            shutil.copyfileobj(response, out)
        tmp.replace(dest)
    except Exception:
        if tmp.exists():
            tmp.unlink()
        curl = shutil.which("curl.exe") or shutil.which("curl")
        if not curl:
            raise
        completed = subprocess.run(
            [curl, "-L", "--fail", "--max-time", "90", "-A", "Mozilla/5.0", "-o", str(tmp), url],
            capture_output=True,
            text=True,
            timeout=100,
        )
        if completed.returncode != 0:
            if tmp.exists():
                tmp.unlink()
            raise RuntimeError((completed.stderr or completed.stdout or f"curl failed {completed.returncode}").strip())
        tmp.replace(dest)


def probe_supplements(max_mmc: int = 8, year: str | None = None, force: bool = False, serial: bool = False) -> None:
    ensure_dirs()
    records = read_metadata()
    for record in records:
        print(f"[probing] {record.get("pii")}")
        if not record.get("candidate"):
            continue
        if year and record_year(record) != year:
            continue
        if not force and record.get("supplementProbeStatus") in {"complete", "no_links", "captcha", "error", "partial"}:
            continue
        pii = record.get("pii") or ""
        if not pii:
            continue
        found = record.get("probedSupplementLinks") or []
        found_urls = {item.get("url") for item in found if isinstance(item, dict)}
        if found and not force:
            record["supplementProbeStatus"] = "complete"
            record.setdefault("supplementProbeMethod", "recorded-links")
            write_metadata(records)
            continue
        original_error_count = len(record.get("probeErrors") or [])
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
            with concurrent.futures.ThreadPoolExecutor(max_workers=1 if serial else 8) as executor:
                future_map = {executor.submit(url_head, url): (ext, url) for ext, url in urls}
                for future in concurrent.futures.as_completed(future_map):
                    ext, url = future_map[future]
                    try:
                        status, content_type, length = future.result()
                    except urllib.error.HTTPError as exc:
                        if exc.code != 404:
                            record.setdefault("probeErrors", []).append({"url": url, "error": f"HTTP {exc.code}"})
                            changed = True
                        continue
                    except Exception as exc:  # noqa: BLE001
                        record.setdefault("probeErrors", []).append({"url": url, "error": str(exc)})
                        changed = True
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
                    try:
                        url_download(url, target)
                    except Exception as exc:  # noqa: BLE001 - network failures should not stop the batch
                        record.setdefault("probeErrors", []).append({"url": url, "error": str(exc)})
                        changed = True
                        continue
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
        error_count = len(record.get("probeErrors") or [])
        if found and error_count > original_error_count:
            record["supplementProbeStatus"] = "partial"
        elif found:
            record["supplementProbeStatus"] = "complete"
        elif error_count > original_error_count:
            record["supplementProbeStatus"] = "error"
        else:
            record["supplementProbeStatus"] = "no_links"
        record["supplementProbeCheckedAt"] = now_iso()
        record["supplementProbeMaxMmc"] = max_mmc
        record["supplementProbeMethod"] = "direct-ars"
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


def fetch_json(url: str, timeout: int = 20) -> dict:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Codex combustion mechanism collection (mailto:none@example.com)", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def normalize_abstract(value: str) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"^\s*abstract\s*", "", value, flags=re.I)
    value = re.sub(r"\s+", " ", value).strip()
    return value


def restore_openalex_abstract(inverted_index: dict) -> str:
    positions: dict[int, str] = {}
    for word, indexes in (inverted_index or {}).items():
        if not isinstance(indexes, list):
            continue
        for index in indexes:
            if isinstance(index, int):
                positions[index] = str(word)
    return " ".join(positions[index] for index in sorted(positions))


def fetch_crossref_abstract(doi: str) -> str:
    if not doi:
        return ""
    try:
        data = fetch_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    except Exception:
        return ""
    return normalize_abstract(data.get("message", {}).get("abstract", ""))


def fetch_openalex_abstract(doi: str) -> str:
    if not doi:
        return ""
    try:
        data = fetch_json("https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi))
    except Exception:
        return ""
    return normalize_abstract(restore_openalex_abstract(data.get("abstract_inverted_index") or {}))


def fetch_semantic_scholar_abstract(doi: str) -> str:
    if not doi:
        return ""
    url = "https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(doi) + "?fields=title,abstract"
    try:
        data = fetch_json(url)
    except Exception:
        return ""
    return normalize_abstract(data.get("abstract") or "")


def extract_abstract_from_pdf(pdf_path: Path) -> str:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext or not pdf_path.exists():
        return ""
    try:
        completed = subprocess.run(
            [pdftotext, "-f", "1", "-l", "3", "-layout", str(pdf_path), "-"],
            capture_output=True,
            timeout=30,
        )
    except Exception:
        return ""
    text = completed.stdout.decode("utf-8", errors="replace") if isinstance(completed.stdout, bytes) else completed.stdout
    text = re.sub(r"\s+", " ", text)
    match = re.search(r"\bAbstract\b(.{80,4000}?)(?:\bKeywords?\b|\b1\s*\.?\s*Introduction\b|\bIntroduction\b)", text, flags=re.I)
    if not match:
        return ""
    return normalize_abstract(match.group(1))


def find_local_pdf(folder: Path) -> Path | None:
    if not folder.exists():
        return None
    pdfs = sorted(path for path in folder.rglob("*.pdf") if path.is_file())
    return pdfs[0] if pdfs else None


def active_folders_from_index() -> dict[str, Path]:
    index = ROOT / "collection_index.csv"
    if not index.exists():
        return {}
    with index.open("r", newline="", encoding="utf-8-sig") as fh:
        rows = list(csv.DictReader(fh))
    return {
        row.get("article_number", ""): Path(row["folder"])
        for row in rows
        if row.get("folder") and row.get("status") in {"included", "conversion_failed"}
    }


def enrich_abstracts() -> None:
    ensure_dirs()
    records = read_metadata()
    active_folders = active_folders_from_index()
    changed = False
    for record in records:
        article = article_id(record)
        if active_folders and article not in active_folders:
            continue
        existing = normalize_abstract(record.get("abstract", ""))
        if existing:
            continue
        folder = active_folders.get(article) or record_folder(record)
        local_pdf = find_local_pdf(folder)
        sources = [
            ("local_pdf", lambda: extract_abstract_from_pdf(local_pdf) if local_pdf else ""),
            ("crossref", lambda: fetch_crossref_abstract(normalize_doi(record.get("doi", "")))),
            ("openalex", lambda: fetch_openalex_abstract(normalize_doi(record.get("doi", "")))),
            ("semantic_scholar", lambda: fetch_semantic_scholar_abstract(normalize_doi(record.get("doi", "")))),
        ]
        for source, getter in sources:
            abstract = getter()
            if abstract:
                record["abstract"] = abstract
                record["abstractSource"] = source
                changed = True
                break
        if not record.get("abstract"):
            record["abstractStatus"] = "not available from local PDF/Crossref/OpenAlex/Semantic Scholar"
            changed = True
        time.sleep(0.1)
    if changed:
        write_metadata(records)


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


def import_sciencedirect_volume_metadata(source_dir: Path, default_year: str) -> None:
    ensure_dirs()
    records = read_metadata()
    changed = normalize_record_years(records)
    by_pii = {str(record.get("pii", "")).lower(): record for record in records if record.get("pii")}
    for file in sorted(source_dir.glob("volume_*.json")):
        volume_records = json.loads(file.read_text(encoding="utf-8-sig"))
        for incoming in volume_records:
            if not incoming.get("pii"):
                continue
            incoming["year"] = str(incoming.get("year") or default_year)
            key = str(incoming["pii"]).lower()
            existing = by_pii.get(key)
            if existing:
                for field in [
                    "year",
                    "volume",
                    "month",
                    "issueUrl",
                    "issueText",
                    "title",
                    "authors",
                    "doi",
                    "articleNumber",
                    "url",
                    "issuePdfLink",
                    "articleType",
                    "access",
                ]:
                    if incoming.get(field) and not existing.get(field):
                        existing[field] = incoming[field]
                        changed = True
                continue
            records.append(incoming)
            by_pii[key] = incoming
            changed = True
    if changed:
        write_metadata(records)


def import_page_supplement_links(source_dir: Path) -> None:
    ensure_dirs()
    records = read_metadata()
    by_pii = {str(record.get("pii", "")).lower(): record for record in records if record.get("pii")}
    changed = False
    for file in sorted(source_dir.glob("chunk_*.json")):
        chunk = json.loads(file.read_text(encoding="utf-8-sig"))
        for item in chunk:
            record = by_pii.get(str(item.get("pii", "")).lower())
            if not record:
                continue
            links = []
            for link in item.get("links", []):
                href = link.get("href") or ""
                if re.search(r"-mmc\d+\.", href, re.I):
                    links.append(
                        {
                            "url": href,
                            "text": link.get("text", ""),
                            "source": "ScienceDirect article page",
                        }
                    )
            if not links:
                if item.get("captcha"):
                    record["articlePageSupplementStatus"] = "captcha"
                    record["supplementProbeStatus"] = "captcha"
                    record["supplementProbeMethod"] = "ScienceDirect article page"
                    record["supplementProbeCheckedAt"] = now_iso()
                    changed = True
                continue
            existing_urls = {
                link.get("url")
                for link in (record.get("probedSupplementLinks") or [])
                if isinstance(link, dict)
            }
            supplement_links = record.setdefault("probedSupplementLinks", [])
            for link in links:
                if link["url"] not in existing_urls:
                    supplement_links.append(link)
                    existing_urls.add(link["url"])
                    changed = True
            record["articlePageSupplementStatus"] = "links imported"
            record["supplementProbeStatus"] = "complete"
            record["supplementProbeMethod"] = "ScienceDirect article page"
            record["supplementProbeCheckedAt"] = now_iso()
    if changed:
        write_metadata(records)


def download_recorded_supplements(year: str | None = None, force: bool = False) -> None:
    ensure_dirs()
    records = read_metadata()
    changed = False
    for record in records:
        print(f"[downloading] {record.get("pii")}")
        if year and record_year(record) != year:
            continue
        links = supplement_links_for_record(record)
        if not links:
            if record.get("supplementDownloadStatus") != "none":
                record["supplementDownloadStatus"] = "none"
                changed = True
            continue
        if not force and record.get("supplementDownloadStatus") == "complete":
            if all(link.get("file") and Path(str(link["file"])).exists() and Path(str(link["file"])).stat().st_size for link in links):
                continue
        if not force and record.get("supplementDownloadStatus") in {"failed", "partial"}:
            continue
        any_file = False
        any_failure = False
        for idx, link in enumerate(links, 1):
            url = link.get("url") or ""
            if not url:
                continue
            if not force and link.get("downloadStatus") == "failed":
                any_failure = True
                continue
            existing_file = Path(str(link.get("file", ""))) if link.get("file") else None
            if existing_file and existing_file.exists() and existing_file.stat().st_size:
                any_file = True
                if link.get("downloadStatus") != "existing":
                    link["downloadStatus"] = "existing"
                    changed = True
                continue
            suffix = Path(urllib.parse.urlparse(url).path).suffix or ".dat"
            match = re.search(r"-mmc(\d+)", url, re.I)
            mmc = match.group(1) if match else str(idx)
            pii = record.get("pii") or "unknown"
            target = DOWNLOADS / f"{pii}_mmc{mmc}{suffix}"
            if target.exists() and target.stat().st_size:
                link["file"] = str(target)
                link["content_length"] = target.stat().st_size
                link["downloadStatus"] = "existing"
                any_file = True
                changed = True
                continue
            try:
                url_download(url, target)
                link["file"] = str(target)
                link["content_length"] = target.stat().st_size
                link["downloadStatus"] = "downloaded"
                link["downloadedAt"] = now_iso()
                any_file = True
                changed = True
            except Exception as exc:  # noqa: BLE001
                record.setdefault("supplementDownloadErrors", []).append({"url": url, "error": str(exc)})
                link["downloadStatus"] = "failed"
                link["downloadError"] = str(exc)
                any_failure = True
                changed = True
        if all(link.get("file") and Path(str(link["file"])).exists() and Path(str(link["file"])).stat().st_size for link in links):
            status = "complete"
        elif any_file and any_failure:
            status = "partial"
        elif any_file:
            status = "partial"
        elif any_failure:
            status = "failed"
        else:
            status = "none"
        if record.get("supplementDownloadStatus") != status:
            record["supplementDownloadStatus"] = status
            changed = True
        record["supplementDownloadCheckedAt"] = now_iso()
    if changed:
        write_metadata(records)


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
    processing_results: list[CkResult],
    extraction_notes: list[str],
) -> None:
    rel = lambda p: str(p.relative_to(dest)) if p and str(p).startswith(str(dest)) else str(p)
    plasma_flag = detect_plasma_case(record, [*mechanism_files, *thermo_files, *transport_files])
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
        f"- Plasma-related mechanism: {plasma_flag}",
        f"- Validation reactor/type from abstract: {detect_reactors(record)}",
        "",
        "## Mechanism Files",
        "",
        f"- Standard mechanism file: chem.inp" if any(r.standardized_mech for r in processing_results) else "- Standard mechanism file: not available",
        f"- Standard thermodynamic file: therm.dat" if any(r.standardized_thermo for r in processing_results) else "- Standard thermodynamic file: not available",
        f"- Standard transport file: tran.dat" if any(r.standardized_transport for r in processing_results) else "- Standard transport file: not available",
        f"- Original mechanism source files: {', '.join(rel(p) for p in mechanism_files) if mechanism_files else 'not found'}",
        f"- Original thermodynamic source files: {', '.join(rel(p) for p in thermo_files) if thermo_files else 'not found'}",
        f"- Original transport source files: {', '.join(rel(p) for p in transport_files) if transport_files else 'not found'}",
        "",
        "## Cantera Preprocessing Results",
        "",
    ]
    if processing_results:
        for idx, result in enumerate(processing_results, 1):
            lines.extend(
                [
                    f"### Mechanism {idx}",
                    "",
                    f"- Status: {result.status}",
                    f"- Species count: {result.species or 'not parsed'}",
                    f"- Reaction count: {result.reactions or 'not parsed'}",
                    f"- Message: {short_message(result.message)}",
                    f"- Method: {result.method or 'not available'}",
                    f"- Cantera YAML: {rel(result.cantera_yaml) if result.cantera_yaml else 'not available'}",
                    f"- Standard chem.inp: {rel(result.standardized_mech) if result.standardized_mech else 'not available'}",
                    f"- Standard therm.dat: {rel(result.standardized_thermo) if result.standardized_thermo else 'not available'}",
                    f"- Standard tran.dat: {rel(result.standardized_transport) if result.standardized_transport else 'not available'}",
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


def index_row(
    record: dict,
    candidate: bool,
    status: str,
    folder: Path | str | None = None,
    mechanism_files: list[Path] | None = None,
    thermo_files: list[Path] | None = None,
    transport_files: list[Path] | None = None,
    processing_results: list[CkResult] | None = None,
    plasma_flag: bool | str = "",
) -> dict[str, str]:
    mechanism_files = mechanism_files or []
    thermo_files = thermo_files or []
    transport_files = transport_files or []
    processing_results = processing_results or []
    last = processing_results[-1] if processing_results else None
    folder_text = str(folder or "")
    return {
        "title": str(record.get("title", "") or ""),
        "authors": "; ".join(record.get("authors", [])) if isinstance(record.get("authors"), list) else str(record.get("authors", "") or ""),
        "doi": str(record.get("doi", "") or ""),
        "pii": str(record.get("pii", "") or ""),
        "volume": str(record.get("volume", "") or ""),
        "month": str(record.get("month", "") or ""),
        "article_number": article_id(record),
        "fuel_type": str(record.get("fuelType", "") or ""),
        "plasma_related": str(plasma_flag),
        "url": str(record.get("url", "") or ""),
        "paper_pdf_link": str(record.get("issuePdfLink", "") or ""),
        "paper_pdf_status": str(record.get("paperPdfStatus", "") or ""),
        "candidate": str(bool(candidate)),
        "status": status,
        "folder": folder_text,
        "mechanism_files": "; ".join(str(p) for p in mechanism_files),
        "thermo_files": "; ".join(str(p) for p in thermo_files),
        "transport_files": "; ".join(str(p) for p in transport_files),
        "standard_mechanism": str(last.standardized_mech) if last and last.standardized_mech else "",
        "standard_thermo": str(last.standardized_thermo) if last and last.standardized_thermo else "",
        "standard_transport": str(last.standardized_transport) if last and last.standardized_transport else "",
        "cantera_yaml": str(last.cantera_yaml) if last and last.cantera_yaml else "",
        "species": str(last.species) if last and last.species else "",
        "reactions": str(last.reactions) if last and last.reactions else "",
        "preprocess_status": str(last.status) if last else "",
    }


def reusable_existing_row(record: dict, existing_row: dict[str, str] | None, folder: Path, force: bool) -> dict[str, str] | None:
    if force or not existing_row:
        return None
    status = record.get("processingStatus") or existing_row.get("status", "")
    if status not in TERMINAL_PROCESSING_STATUSES:
        return None
    if status in ACTIVE_STATUSES:
        summary = folder / "mechanism_summary.md"
        if not summary.exists():
            return None
        if status == "included" and not (folder / "chem.inp").exists() and not (folder / "mechanism.yaml").exists():
            return None
    row = clean_index_row(existing_row)
    row["fuel_type"] = record.get("fuelType", row.get("fuel_type", ""))
    row["candidate"] = str(bool(record.get("candidate")))
    row["status"] = status
    record["processingStatus"] = status
    if not record.get("processingSkipReason"):
        record["processingSkipReason"] = "reused existing terminal processing state from collection_index.csv"
    return row


def update_record_processing_state(
    record: dict,
    row: dict[str, str],
    local_downloads: list[Path],
    mechanism_files: list[Path],
    thermo_files: list[Path],
    transport_files: list[Path],
) -> None:
    record["processingStatus"] = row["status"]
    record["processedAt"] = now_iso()
    record["processingFolder"] = row["folder"]
    record["processedSupplementLinkCount"] = len(supplement_links_for_record(record))
    record["processedLocalDownloadCount"] = len(local_downloads)
    record["processingMechanismFiles"] = row["mechanism_files"]
    record["processingThermoFiles"] = row["thermo_files"]
    record["processingTransportFiles"] = row["transport_files"]
    record["processingStandardMechanism"] = row["standard_mechanism"]
    record["processingStandardThermo"] = row["standard_thermo"]
    record["processingStandardTransport"] = row["standard_transport"]
    record["processingCanteraYaml"] = row["cantera_yaml"]
    record["processingSpecies"] = row["species"]
    record["processingReactions"] = row["reactions"]
    record["processingPreprocessStatus"] = row["preprocess_status"]
    record["processingMechanismFileCount"] = len(mechanism_files)
    record["processingThermoFileCount"] = len(thermo_files)
    record["processingTransportFileCount"] = len(transport_files)


def summary_values(folder: Path, label: str) -> list[str]:
    summary = folder / "mechanism_summary.md"
    if not summary.exists():
        return []
    pattern = re.compile(rf"^-\s*{re.escape(label)}:\s*(.*)$", re.I)
    values: list[str] = []
    for line in summary.read_text(encoding="utf-8", errors="ignore").splitlines():
        match = pattern.match(line.strip())
        if match:
            values.append(match.group(1).strip())
    return values


def last_summary_value(folder: Path, label: str) -> str:
    values = [value for value in summary_values(folder, label) if value and value.lower() != "not available"]
    return values[-1] if values else ""


def append_handoff_items(
    handoff: list[str],
    record: dict,
    status: str,
    folder: Path,
    mechanism_files: list[Path] | None = None,
    cantera_files: list[Path] | None = None,
    thermo_files: list[Path] | None = None,
    processing_results: list[CkResult] | None = None,
) -> None:
    mechanism_files = mechanism_files or []
    cantera_files = cantera_files or []
    thermo_files = thermo_files or []
    processing_results = processing_results or []
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
    if status == "conversion_failed":
        if processing_results:
            last = processing_results[-1]
            last_message = short_message(last.message)
        else:
            last = CkResult(last_summary_value(folder, "Status") or str(record.get("processingPreprocessStatus") or "conversion_failed"))
            last_message = last_summary_value(folder, "Message")
        mechanism_text = "; ".join(str(p) for p in mechanism_files + cantera_files) or str(record.get("processingMechanismFiles", ""))
        thermo_text = "; ".join(str(p) for p in thermo_files) or str(record.get("processingThermoFiles", ""))
        handoff.extend(
            [
                f"## Cantera conversion failed: {record.get('title', 'Untitled')}",
                "",
                f"- DOI: {record.get('doi', '')}",
                f"- URL: {record.get('url', '')}",
                f"- Mechanism candidates: {mechanism_text}",
                f"- Thermodynamic candidates: {thermo_text}",
                f"- Last status: {last.status}",
                f"- Last message: {last_message}",
                f"- Target folder: {folder}",
                "",
            ]
        )
    if record_year(record) == "2025" and status in {"excluded_no_supplement_found", "excluded_no_mechanism_attachment"}:
        probe_errors = record.get("probeErrors") or []
        handoff.extend(
            [
                f"## 2025 supplement review needed: {record.get('title', 'Untitled')}",
                "",
                f"- DOI: {record.get('doi', '')}",
                f"- URL: {record.get('url', '')}",
                f"- Article number: {article_id(record)}",
                f"- Status: {status}",
                f"- Supplement links found: {len(supplement_links_for_record(record))}",
                f"- Probe errors: {len(probe_errors)}",
                "- Reason: automated direct supplement probing did not yield a processable mechanism; ScienceDirect article-page access is currently gated by CAPTCHA",
                "",
            ]
        )


def process(force: bool = False, year: str | None = None) -> None:
    ensure_dirs()
    records = read_metadata()
    if year is not None:
        records = [r for r in records if r.get("year") == year]
    previous_rows = existing_index_rows()
    metadata_changed = False
    rows: list[dict] = []
    handoff: list[str] = [
        "# Manual Download Handoff",
        "",
        "Items below need user-side ScienceDirect/Elsevier download or review.",
        "",
    ]
    seen_dois: set[str] = set()
    skipped_processing = 0
    for record in records:
        doi_key = normalize_doi(record.get("doi", "")) or record.get("url", "")
        if doi_key in seen_dois:
            continue
        seen_dois.add(doi_key)
        record["fuelType"] = detect_fuel(record)
        candidate = is_reaction_kinetics_candidate(record)
        record["candidate"] = candidate
        folder = record_folder(record)
        archive_folder = processing_folder(record)
        existing_row = previous_rows.get(article_id(record))
        metadata_changed = seed_processing_state_from_index(record, existing_row) or metadata_changed
        skipped_row = reusable_existing_row(record, existing_row, folder, force)
        if skipped_row is not None:
            skipped_processing += 1
            rows.append(skipped_row)
            append_handoff_items(handoff, record, skipped_row["status"], folder)
            metadata_changed = True
            continue
        local_downloads: list[Path] = []
        extraction_notes: list[str] = []
        mechanisms: list[Path] = []
        thermos: list[Path] = []
        transports: list[Path] = []
        cantera: list[Path] = []
        if candidate:
            local_downloads = copy_downloads_for_record(record, archive_folder / "raw_downloads")
            extracted_dest = archive_folder / "extracted"
            extraction_notes = extract_archives(local_downloads, extracted_dest)
            scan_roots = [archive_folder / "raw_downloads", extracted_dest]
            mechanisms, thermos, transports, cantera = scan_files(scan_roots)
        processing_results: list[CkResult] = []
        if mechanisms:
            if not record.get("paperPdfStatus"):
                record["paperPdfStatus"] = "pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed"
            for mech in sorted(mechanisms, key=mechanism_priority):
                thermo = find_thermo_for(mech, thermos + mechanisms)
                transport = find_transport_for(mech, transports)
                result = process_with_cantera(mech, thermo, transport, folder, archive_folder)
                processing_results.append(result)
                if result.status in {"ok", "ok_after_cleanup"}:
                    break
            write_summary(record, folder, mechanisms, thermos, transports, processing_results, extraction_notes)
        elif cantera:
            folder.mkdir(parents=True, exist_ok=True)
            if not record.get("paperPdfStatus"):
                record["paperPdfStatus"] = "pending manual download; ScienceDirect PDF access triggered CAPTCHA or was not exposed"
            for mech in sorted(cantera, key=mechanism_priority):
                result = process_with_cantera(mech, None, None, folder, archive_folder)
                processing_results.append(result)
                if result.status in {"ok", "ok_after_cleanup"}:
                    break
            write_summary(record, folder, cantera, thermos, transports, processing_results, extraction_notes + ["Cantera file detected"])
        elif candidate:
            pass
        plasma_flag = detect_plasma_case(record, [*mechanisms, *thermos, *transports, *cantera])
        has_success = any(result.status in {"ok", "ok_after_cleanup"} for result in processing_results)
        has_mechanism_candidate = bool(mechanisms or cantera)
        has_supplement_probe = bool(local_downloads or record.get("probedSupplementLinks") or record.get("supplementLinks"))
        if has_mechanism_candidate and not candidate:
            status = "excluded_non_kinetics_mechanism_attachment"
        elif has_success:
            status = "included"
        elif has_mechanism_candidate:
            status = "conversion_failed"
        elif candidate and has_supplement_probe:
            status = "excluded_no_mechanism_attachment"
        elif candidate:
            status = "excluded_no_supplement_found"
        else:
            status = "excluded_no_mechanism_signal"
        append_handoff_items(handoff, record, status, folder, mechanisms, cantera, thermos, processing_results)
        row = index_row(
            record,
            candidate,
            status,
            folder if (has_success or has_mechanism_candidate) else "",
            mechanisms + cantera,
            thermos,
            transports,
            processing_results,
            plasma_flag,
        )
        rows.append(row)
        update_record_processing_state(record, row, local_downloads, mechanisms + cantera, thermos, transports)
        metadata_changed = True
    with ROOT.joinpath("collection_index.csv").open("w", newline="", encoding="utf-8-sig") as fh:
        writer = csv.DictWriter(fh, fieldnames=INDEX_FIELDS)
        writer.writeheader()
        writer.writerows(clean_index_row(row) for row in rows)
    active_summary_paths = {
        (Path(row["folder"]) / "mechanism_summary.md").resolve()
        for row in rows
        if row.get("folder") and row["status"] in {"included", "conversion_failed"}
    }
    for summary in ROOT.rglob("mechanism_summary.md"):
        if summary.resolve() not in active_summary_paths:
            summary.unlink()
    active_folders = {path.parent for path in active_summary_paths}
    generated_names = {
        "chem.inp",
        "therm.dat",
        "tran.dat",
        "mechanism.yaml",
        "mechanism.cleaned.yaml",
        "mechanism.numeric_clean.yaml",
        "chem_cantera_clean.inp",
        "chem_cantera_numeric_clean.inp",
        "cantera_conversion.log",
        "cantera_conversion.cleaned.log",
        "cantera_conversion.numeric_clean.log",
        "mechanism.result.json",
        "mechanism.cleaned.result.json",
        "mechanism.numeric_clean.result.json",
    }
    for generated in ROOT.rglob("*"):
        if any(part.startswith("_") for part in generated.relative_to(ROOT).parts):
            continue
        if generated.is_file() and generated.name in generated_names and generated.parent.resolve() not in active_folders:
            generated.unlink()
    for folder_path in active_folders:
        cleanup_active_paper_folder(folder_path)
    cleanup_inactive_paper_folders(ROOT, active_folders)
    if PROCESSING_ARCHIVE.exists():
        shutil.rmtree(PROCESSING_ARCHIVE)
    ROOT.joinpath("manual_download_handoff.md").write_text("\n".join(handoff) + "\n", encoding="utf-8")
    ROOT.joinpath("run_summary.json").write_text(
        json.dumps(
            {
                "updated_at": dt.datetime.now().isoformat(timespec="seconds"),
                "metadata_records": len(records),
                "index_rows": len(rows),
                "included": sum(1 for r in rows if r["status"] == "included"),
                "conversion_failed": sum(1 for r in rows if r["status"] == "conversion_failed"),
                "excluded_non_kinetics_mechanism_attachment": sum(
                    1 for r in rows if r["status"] == "excluded_non_kinetics_mechanism_attachment"
                ),
                "excluded_no_mechanism_attachment": sum(1 for r in rows if r["status"] == "excluded_no_mechanism_attachment"),
                "excluded_no_mechanism_signal": sum(1 for r in rows if r["status"] == "excluded_no_mechanism_signal"),
                "excluded_no_supplement_found": sum(1 for r in rows if r["status"] == "excluded_no_supplement_found"),
                "pending_download": sum(1 for r in rows if r["status"] == "pending_download"),
                "skipped_existing_processing": skipped_processing,
                "root": str(ROOT),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    # Save ALL metadata, not just filtered records (preserve other years)
    all_records = read_metadata()
    if year is not None:
        filtered_ids = {article_id(r) for r in records}
        all_records = [r if article_id(r) in filtered_ids else r for r in all_records]
        # Update filtered records in all_records
        rec_map = {article_id(r): r for r in records}
        all_records = [rec_map.get(article_id(r), r) for r in all_records]
    else:
        all_records = records
    write_metadata(all_records)


def init() -> None:
    ensure_dirs()
    if not METADATA_JSON.exists():
        write_metadata([])
    README = ROOT / "README.md"
    if not README.exists():
        README.write_text(
            textwrap.dedent(
                f"""\
                # Combustion and Flame Mechanism Collection

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
    parser.add_argument(
        "command",
        choices=[
            "init",
            "import-sciencedirect-metadata",
            "import-page-supplements",
            "download-supplements",
            "enrich-crossref",
            "enrich-abstracts",
            "probe-supplements",
            "process",
        ],
    )
    parser.add_argument("--max-mmc", type=int, default=8)
    parser.add_argument("--source-dir", type=Path, default=RAW / "2025_volumes")
    parser.add_argument("--year", type=str, help="Only process this year")
    parser.add_argument("--force", action="store_true", help="re-run terminal probe, download, or processing states")
    parser.add_argument("--serial", action="store_true", help="serial mode: single-threaded probe to avoid OOM")
    args = parser.parse_args()
    if args.command == "init":
        init()
    elif args.command == "import-sciencedirect-metadata":
        import_sciencedirect_volume_metadata(args.source_dir, args.year or "2025")
    elif args.command == "import-page-supplements":
        import_page_supplement_links(args.source_dir)
    elif args.command == "download-supplements":
        download_recorded_supplements(year=args.year, force=args.force)
    elif args.command == "enrich-crossref":
        enrich_crossref()
    elif args.command == "enrich-abstracts":
        enrich_abstracts()
    elif args.command == "probe-supplements":
        probe_supplements(max_mmc=args.max_mmc, year=args.year, force=args.force, serial=args.serial)
    elif args.command == "process":
        process(force=args.force, year=args.year)


if __name__ == "__main__":
    main()

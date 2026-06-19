1|#!/usr/bin/env python3
2|"""Collect and post-process Combustion and Flame 2026 mechanism supplements.
3|
4|Browser automation writes article metadata and downloaded files into the output
5|tree. This script handles the local, reproducible parts: folder layout,
6|supplement extraction, mechanism detection, ckinterp execution, summaries, and
7|indexes.
8|"""
9|
10|from __future__ import annotations
11|
12|import argparse
13|import concurrent.futures
14|import csv
15|import datetime as dt
16|import difflib
17|import gc
18|import html
19|import json
20|import os
21|import re
22|import shutil
23|import sys
24|import subprocess
25|import tarfile
26|import textwrap
27|import time
28|import urllib.error
29|import urllib.parse
30|import urllib.request
31|import zipfile
32|from dataclasses import dataclass
33|from pathlib import Path
34|from typing import Iterable
35|
36|
37|WORKSPACE = Path(os.environ.get("MECH_COLLECTION_WORKSPACE", Path(__file__).resolve().parents[1])).resolve()
38|LEGACY_ROOT = WORKSPACE / "combustion_and_flame_2026_mechanisms"
39|ROOT = Path(os.environ.get("MECH_COLLECTION_ROOT", WORKSPACE / "combustion_and_flame_mechanisms")).resolve()
40|RAW = ROOT / "_raw"
41|DOWNLOADS = RAW / "downloads"
42|EXTRACTED = RAW / "extracted"
43|METADATA_JSON = RAW / "article_metadata.json"
44|LEGACY_METADATA_JSON = LEGACY_ROOT / "_raw" / "article_metadata.json"
45|LEGACY_DOWNLOADS = LEGACY_ROOT / "_raw" / "downloads"
46|PROCESSING_ARCHIVE = ROOT / "_processing_archive"
47|CKDIR = Path(r"D:\BaiduSyncdisk\soft\CoFlame_yang")
48|CKEXE = CKDIR / "ckinterp.exe"
49|CK_FILES = ["chem.inp", "therm.dat", "chem.out"]
50|ANALYSIS_PYTHON = Path(os.environ.get("MECH_COLLECTION_PYTHON", sys.executable)).resolve()
51|MMC_EXTENSIONS = [
52|    "zip",
53|    "txt",
54|    "docx",
55|    "pdf",
56|    "xlsx",
57|    "xls",
58|    "rar",
59|    "7z",
60|    "dat",
61|    "inp",
62|    "yaml",
63|    "yml",
64|    "cti",
65|    "xml",
66|]
67|
68|INDEX_FIELDS = [
69|    "title",
70|    "authors",
71|    "doi",
72|    "pii",
73|    "volume",
74|    "month",
75|    "article_number",
76|    "fuel_type",
77|    "plasma_related",
78|    "url",
79|    "paper_pdf_link",
80|    "paper_pdf_status",
81|    "candidate",
82|    "status",
83|    "folder",
84|    "mechanism_files",
85|    "thermo_files",
86|    "transport_files",
87|    "standard_mechanism",
88|    "standard_thermo",
89|    "standard_transport",
90|    "cantera_yaml",
91|    "species",
92|    "reactions",
93|    "preprocess_status",
94|]
95|
96|ACTIVE_STATUSES = {"included", "conversion_failed"}
97|TERMINAL_PROCESSING_STATUSES = ACTIVE_STATUSES | {
98|    "excluded_non_kinetics_mechanism_attachment",
99|    "excluded_no_mechanism_attachment",
100|    "excluded_no_supplement_found",
101|    "excluded_no_mechanism_signal",
102|}
103|
104|KINETIC_TERMS = [
105|    "kinetic",
106|    "kinetics",
107|    "mechanism",
108|    "mechanisms",
109|    "modeling",
110|    "modelling",
111|    "oxidation",
112|    "pyrolysis",
113|    "autoignition",
114|    "auto-ignition",
115|    "ignition delay",
116|    "laminar burning velocity",
117|    "laminar flame speed",
118|]
119|
120|REACTION_KINETICS_INCLUDE_PATTERNS = [
121|    r"chemical kinetic",
122|    r"\bkinetic (model|modeling|modelling|study|analysis|mechanism|insight|investigation|simulation)",
123|    r"\bkinetics of\b",
124|    r"\bkinetic inhibition\b",
125|    r"\bkinetic coupling\b",
126|    r"\boxidation kinetics\b",
127|    r"\bpyrolysis kinetics\b",
128|    r"\bcombustion kinetics\b",
129|    r"\breaction mechanism\b",
130|    r"\bdetailed kinetic\b",
131|    r"\bmechanism development\b",
132|    r"\bexperimental and modeling study\b",
133|    r"\bdetailed and reduced kinetics\b",
134|    r"\bcarbon.?nitrogen interaction reactions\b",
135|    r"\bmodel development and validation\b",
136|    r"\bauto-?ignition\b",
137|    r"\bignition delay\b",
138|    r"\blaminar burning velocit",
139|    r"\blaminar flame speed\b",
140|    r"\bjet-?stirred reactor\b",
141|    r"\bshock tube\b",
142|    r"\brapid compression machine\b",
143|    r"\bflow reactor\b",
144|    r"\bflame speed measurements\b",
145|]
146|
147|REACTION_KINETICS_EXCLUDE_PATTERNS = [
148|    r"thermoacoustic",
149|    r"instability mechanism",
150|    r"feedback mechanism",
151|    r"heat transfer mechanism",
152|    r"flame spread",
153|    r"flame quenching",
154|    r"suppression",
155|    r"dust explosion",
156|    r"porous medium",
157|    r"scramjet",
158|    r"combustion transition mechanisms",
159|    r"turbulence characteristics",
160|    r"spray flame",
161|    r"genetic programming control",
162|    r"nanoparticle synthesis",
163|    r"aluminum combustion",
164|    r"single al\b",
165|    r"al-li alloy particle",
166|    r"burning rate constant of pmma",
167|]
168|
169|REACTOR_TERMS = [
170|    ("shock tube", ["shock tube", "behind shock waves"]),
171|    ("rapid compression machine", ["rapid compression machine", "rcm"]),
172|    ("jet-stirred reactor", ["jet-stirred reactor", "jet stirred reactor", "jsr"]),
173|    ("flow reactor", ["flow reactor", "plug flow reactor"]),
174|    ("laminar flame speed", ["laminar flame speed", "laminar burning velocity"]),
175|    ("burner/flame structure", ["burner", "flame structure", "premixed flame", "diffusion flame"]),
176|    ("counterflow flame", ["counterflow"]),
177|    ("stirred reactor", ["stirred reactor"]),
178|]
179|
180|FUEL_PATTERNS = [
181|    (r"\bNH\s*3\b|ammonia", "ammonia"),
182|    (r"n\s*-?\s*dodecane|dodecane", "n_dodecane"),
183|    (r"n\s*-?\s*decane|\bdecane\b", "n_decane"),
184|    (r"n\s*-?\s*heptane|heptane", "n_heptane"),
185|    (r"methanol", "methanol"),
186|    (r"1,?2-?dimethoxyethane", "dimethoxyethane"),
187|    (r"dimethoxymethane|\bDMM\b", "dimethoxymethane"),
188|    (r"dimethyl[ -]?ether|\bDME\b", "dimethyl_ether"),
189|    (r"N-?methyl aniline|N-?methylaniline", "n_methyl_aniline"),
190|    (r"2-?ethylhexyl nitrate|\bEHN\b", "2_ethylhexyl_nitrate"),
191|    (r"ethyl acetate", "ethyl_acetate"),
192|    (r"methyl formate", "methyl_formate"),
193|    (r"methylamine", "methylamine"),
194|    (r"\bmethane\b|\bCH\s*4\b", "methane"),
195|    (r"\bH\s*2\b|hydrogen", "hydrogen"),
196|    (r"ethylene|C\s*2\s*H\s*4", "ethylene"),
197|    (r"\bethane\b|\bC\s*2\s*H\s*6\b", "ethane"),
198|    (r"acetone", "acetone"),
199|    (r"2-?butanone|butanone|methyl ethyl ketone", "2_butanone"),
200|    (r"1-?butene", "1_butene"),
201|    (r"n-?butane|\bbutane\b", "n_butane"),
202|    (r"ethylcyclohexane", "ethylcyclohexane"),
203|    (r"n-?butylbenzene|butylbenzene", "n_butylbenzene"),
204|    (r"quadricyclane", "quadricyclane"),
205|    (r"cyclopentene", "cyclopentene"),
206|    (r"cyclopentanone", "cyclopentanone"),
207|    (r"furan", "furan"),
208|    (r"tetrahydrofuran", "tetrahydrofuran"),
209|    (r"2-?methylfuran", "2_methylfuran"),
210|    (r"pyrrole", "pyrrole"),
211|    (r"pyridine", "pyridine"),
212|    (r"pentane", "pentane"),
213|    (r"pentanol|secondary pentanols|2- and 3-pentanol|2-pentanol|3-pentanol", "pentanol"),
214|    (r"RP-?3", "rp3"),
215|    (r"gas to liquid jet fuel|gas-to-liquid jet fuel|\bGTL\b", "gtl_jet_fuel"),
216|    (r"norbornane", "norbornane"),
217|    (r"propane", "propane"),
218|    (r"propan-?1-?ol|1-?propanol|propanol", "propanol"),
219|    (r"acetylene", "acetylene"),
220|    (r"syngas", "syngas"),
221|    (r"\bNO removal\b|direct\s+NO\s+removal|nitric oxide", "nitric_oxide"),
222|    (r"N\s*2\s*O|nitrous oxide", "n2o"),
223|    (r"nitromethane", "nitromethane"),
224|    (r"dimethyl carbonate", "dimethyl_carbonate"),
225|    (r"1,?2,?4-?trimethylbenzene", "trimethylbenzene_124"),
226|    (r"3-?ethyltoluene", "3_ethyltoluene"),
227|    (r"3-?n-?propyltoluene", "3_n_propyltoluene"),
228|    (r"cumene", "cumene"),
229|    (r"triptane|2,?2,?3-?trimethylbutane", "triptane"),
230|    (r"2-?ethylhexyl nitrate|\bEHN\b", "2_ethylhexyl_nitrate"),
231|    (r"HCFO-?1233xf", "hcfo_1233xf"),
232|    (r"ammonium nitrate", "ammonium_nitrate"),
233|    (r"ammonium chloride", "ammonium_chloride"),
234|    (r"magnesium", "magnesium"),
235|    (r"C0[–-]C1 multi-component fuel blends|C0[–-]C1", "c0_c1_fuel_blends"),
236|    (r"C0[–-]C3/N\s*2\s*O|C0[–-]C3", "c0_c3_fuel_blends"),
237|    (r"gasoline", "gasoline"),
238|    (r"coal", "coal"),
239|    (r"sustainable aviation fuel|SAF", "saf"),
240|    (r"naphtha", "naphtha"),
241|    (r"iron", "iron"),
242|]
243|
244|
245|def slugify(value: str, max_len: int = 80) -> str:
246|    value = re.sub(r"<[^>]+>", "", value or "")
247|    value = value.lower()
248|    value = re.sub(r"[^a-z0-9]+", "_", value)
249|    value = re.sub(r"_+", "_", value).strip("_")
250|    return (value[:max_len].strip("_") or "unknown")
251|
252|
253|def ensure_dirs() -> None:
254|    for path in [ROOT, RAW, DOWNLOADS, EXTRACTED]:
255|        path.mkdir(parents=True, exist_ok=True)
256|
257|
258|def read_metadata() -> list[dict]:
259|    source = METADATA_JSON if METADATA_JSON.exists() else LEGACY_METADATA_JSON
260|    if not source.exists():
261|        return []
262|    records = json.loads(source.read_text(encoding="utf-8-sig"))
263|    if source == LEGACY_METADATA_JSON and not METADATA_JSON.exists():
264|        write_metadata(records)
265|    return records
266|
267|
268|def write_metadata(records: list[dict]) -> None:
269|    ensure_dirs()
270|    METADATA_JSON.write_text(
271|        json.dumps(records, ensure_ascii=False, indent=2),
272|        encoding="utf-8",
273|    )
274|
275|
276|def now_iso() -> str:
277|    return dt.datetime.now().isoformat(timespec="seconds")
278|
279|
280|def supplement_links_for_record(record: dict) -> list[dict]:
281|    links = record.get("probedSupplementLinks") or record.get("supplementLinks") or []
282|    return [link for link in links if isinstance(link, dict)]
283|
284|
285|def existing_index_rows() -> dict[str, dict[str, str]]:
286|    index = ROOT / "collection_index.csv"
287|    if not index.exists():
288|        return {}
289|    with index.open("r", newline="", encoding="utf-8-sig") as fh:
290|        rows = list(csv.DictReader(fh))
291|    return {row.get("article_number", ""): row for row in rows if row.get("article_number")}
292|
293|
294|def clean_index_row(row: dict[str, str]) -> dict[str, str]:
295|    return {field: str(row.get(field, "") or "") for field in INDEX_FIELDS}
296|
297|
298|def seed_processing_state_from_index(record: dict, row: dict[str, str] | None) -> bool:
299|    if not row:
300|        return False
301|    changed = False
302|    mappings = {
303|        "processingStatus": "status",
304|        "processingFolder": "folder",
305|        "processingSpecies": "species",
306|        "processingReactions": "reactions",
307|        "processingPreprocessStatus": "preprocess_status",
308|        "processingMechanismFiles": "mechanism_files",
309|        "processingThermoFiles": "thermo_files",
310|        "processingTransportFiles": "transport_files",
311|        "processingCanteraYaml": "cantera_yaml",
312|        "processingStandardMechanism": "standard_mechanism",
313|        "processingStandardThermo": "standard_thermo",
314|        "processingStandardTransport": "standard_transport",
315|    }
316|    for record_key, row_key in mappings.items():
317|        if not record.get(record_key) and row.get(row_key):
318|            record[record_key] = row[row_key]
319|            changed = True
320|    return changed
321|
322|
323|def normalize_doi(doi: str) -> str:
324|    doi = (doi or "").strip()
325|    doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")
326|    return doi.lower()
327|
328|
329|def article_id(record: dict) -> str:
330|    if record.get("articleNumber"):
331|        return str(record["articleNumber"])
332|    doi = normalize_doi(record.get("doi", ""))
333|    match = re.search(r"(114\d+)", doi)
334|    if match:
335|        return match.group(1)
336|    pii = record.get("pii") or ""
337|    return pii[-8:] if pii else "article"
338|
339|
340|def record_year(record: dict) -> str:
341|    for key in ("year", "publicationYear", "coverYear"):
342|        value = str(record.get(key, "") or "").strip()
343|        if re.fullmatch(r"\d{4}", value):
344|            return value
345|    # DOI registration strings can contain the prior online year even when the
346|    # article belongs to the 2026 journal volume, so do not derive folder years
347|    # from DOI text.
348|    return "2026"
349|
350|
351|def normalize_record_years(records: list[dict], default_year: str = "2026") -> bool:
352|    changed = False
353|    for record in records:
354|        if not record.get("year"):
355|            record["year"] = default_year
356|            changed = True
357|    return changed
358|
359|
360|def detect_fuel(record: dict) -> str:
361|    def scan(text: str) -> list[str]:
362|        found_labels: list[str] = []
363|        for pattern, label in FUEL_PATTERNS:
364|            if re.search(pattern, text, flags=re.I):
365|                if label not in found_labels:
366|                    found_labels.append(label)
367|        return found_labels
368|
369|    found = scan(str(record.get("title", "")))
370|    if not found:
371|        found = scan(str(record.get("keywords", "")))
372|    if not found:
373|        abstract = str(record.get("abstract", ""))
374|        if re.search(r"\b(fuel|surrogate|oxidation of|pyrolysis of|combustion of)\b", abstract, flags=re.I):
375|            found = scan(abstract[:800])
376|    if not found:
377|        return "unknown_fuel"
378|    return "_".join(found[:4])
379|
380|
381|def is_candidate(record: dict) -> bool:
382|    text = (str(record.get("title", "")) + " " + str(record.get("abstract", ""))).lower()
383|    return any(term in text for term in KINETIC_TERMS)
384|
385|
386|def is_reaction_kinetics_candidate(record: dict) -> bool:
387|    text = (str(record.get("title", "")) + " " + str(record.get("abstract", ""))).lower()
388|    text = re.sub(r"<[^>]+>", " ", text)
389|    text = re.sub(r"\s+", " ", text)
390|    if any(re.search(pattern, text) for pattern in REACTION_KINETICS_EXCLUDE_PATTERNS):
391|        if not any(re.search(pattern, text) for pattern in [r"chemical kinetic", r"\bkinetic (model|modeling|modelling)", r"\breaction mechanism\b"]):
392|            return False
393|    if any(re.search(pattern, text) for pattern in REACTION_KINETICS_INCLUDE_PATTERNS):
394|        return True
395|    fuel = detect_fuel(record)
396|    if fuel != "unknown_fuel" and any(term in text for term in ["pyrolysis", "oxidation", "autoignition", "combustion kinetics"]):
397|        return True
398|    if fuel != "unknown_fuel" and "formation" in text and any(term in text for term in ["products", "pah", "polycyclic", "nitrogen-containing"]):
399|        return True
400|    chemistry_context = any(term in text for term in ["oxidation", "pyrolysis", "combustion", "autoignition", "flame speed"])
401|    modeling_context = any(term in text for term in ["kinetic", "kinetics", "modeling", "modelling", "mechanism"])
402|    reactor_context = any(term in text for term in ["shock tube", "jet-stirred", "jet stirred", "flow reactor", "rapid compression", "rcm"])
403|    return chemistry_context and modeling_context and reactor_context
404|
405|
406|def record_folder(record: dict) -> Path:
407|    fuel = record.get("fuelType") or detect_fuel(record)
408|    year = record_year(record)
409|    authors = record.get("authors") or []
410|    if isinstance(authors, str):
411|        first_author = authors.split(",")[0].strip()
412|    elif authors:
413|        first_author = str(authors[0]).strip()
414|    else:
415|        first_author = "unknown"
416|    surname = first_author_surname(first_author)
417|    fuel_slug = slugify(fuel, 60)
418|    name = f"{slugify(surname, 24)}_{year}_{fuel_slug}_{article_id(record)}"
419|    return ROOT / fuel_slug / year / name
420|
421|
422|def legacy_processing_folder(record: dict) -> Path:
423|    fuel = slugify(record.get("fuelType") or detect_fuel(record), 60)
424|    year = record_year(record)
425|    return PROCESSING_ARCHIVE / year / fuel / record_folder(record).name
426|
427|
428|def processing_folder(record: dict) -> Path:
429|    return record_folder(record) / "_processing"
430|
431|
432|def first_author_surname(author: str) -> str:
433|    author = re.sub(r"<[^>]+>", "", author or "").strip()
434|    author = re.sub(r"\s+", " ", author)
435|    if not author:
436|        return "unknown"
437|    if "," in author:
438|        return author.split(",", 1)[0].strip() or "unknown"
439|    tokens = [token for token in re.split(r"\s+", author) if token]
440|    return tokens[-1] if tokens else "unknown"
441|
442|
443|def looks_like_text(path: Path) -> bool:
444|    try:
445|        chunk = path.read_bytes()[:4096]
446|    except OSError:
447|        return False
448|    if not chunk:
449|        return False
450|    return b"\x00" not in chunk
451|
452|
453|def read_text_limited(path: Path, limit: int = 2_000_000) -> str:
454|    try:
455|        data = path.read_bytes()[:limit]
456|    except OSError:
457|        return ""
458|    for enc in ("utf-8", "latin-1", "cp1252"):
459|        try:
460|            return data.decode(enc, errors="ignore").lstrip("\ufeff")
461|        except UnicodeDecodeError:
462|            continue
463|    return data.decode("latin-1", errors="ignore").lstrip("\ufeff")
464|
465|
466|def looks_like_transport_table(text: str) -> bool:
467|    upper = text.upper()
468|    if "ENDDIFF" in upper:
469|        return True
470|    table_lines = 0
471|    for line in text.splitlines():
472|        stripped = line.strip()
473|        if not stripped or stripped.startswith(("!", "#")):
474|            continue
475|        if re.match(r"^[A-Za-z0-9_()+,\-*.]+\s+[0-2]\s+[-+0-9.Ee]+\s+[-+0-9.Ee]+\s+[-+0-9.Ee]+", stripped):
476|            table_lines += 1
477|            if table_lines >= 5:
478|                return True
479|    return False
480|
481|
482|def classify_file(path: Path) -> set[str]:
483|    if not path.is_file() or not looks_like_text(path):
484|        return set()
485|    text = read_text_limited(path)
486|    upper = text.upper()
487|    labels: set[str] = set()
488|    if "SPECIES CONSIDERED" in upper or "REACTIONS CONSIDERED" in upper:
489|        return labels
490|    if re.search(r"(^|\n)\s*ELEMENTS\b", upper) and re.search(r"(^|\n)\s*SPECIES\b", upper):
491|        labels.add("chemkin_mechanism")
492|    if re.search(r"(^|\n)\s*REACTIONS(?!\s+CONSIDERED)\b", upper):
493|        labels.add("reactions")
494|        labels.add("chemkin_mechanism")
495|    if re.search(r"(^|\n)\s*THERMO\b", upper):
496|        labels.add("thermo")
497|    if re.search(r"(^|\n)\s*TRANSPORT\b", upper) or looks_like_transport_table(text):
498|        labels.add("transport")
499|    if "UNITS:" in upper and "PHASES:" in upper and ("REACTIONS:" in upper or "SPECIES:" in upper):
500|        labels.add("cantera")
501|    return labels
502|
503|
504|def safe_extract_zip(path: Path, dest: Path) -> None:
505|    with zipfile.ZipFile(path) as zf:
506|        for member in zf.infolist():
507|            target = dest / member.filename
508|            resolved = target.resolve()
509|            if not str(resolved).startswith(str(dest.resolve())):
510|                continue
511|            if member.is_dir():
512|                resolved.mkdir(parents=True, exist_ok=True)
513|            else:
514|                resolved.parent.mkdir(parents=True, exist_ok=True)
515|                with zf.open(member) as src, resolved.open("wb") as out:
516|                    shutil.copyfileobj(src, out)
517|
518|
519|def safe_extract_tar(path: Path, dest: Path) -> None:
520|    with tarfile.open(path) as tf:
521|        for member in tf.getmembers():
522|            target = dest / member.name
523|            resolved = target.resolve()
524|            if str(resolved).startswith(str(dest.resolve())):
525|                tf.extract(member, dest)
526|
527|
528|def archive_kind(path: Path) -> str:
529|    try:
530|        header = path.read_bytes()[:8]
531|    except OSError:
532|        return ""
533|    suffix = path.suffix.lower()
534|    if header.startswith((b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")):
535|        return "zip"
536|    if header.startswith(b"\x1f\x8b"):
537|        return "gzip"
538|    if header.startswith(b"7z\xbc\xaf\x27\x1c"):
539|        return "7z"
540|    if header.startswith((b"Rar!\x1a\x07\x00", b"Rar!\x1a\x07\x01\x00")):
541|        return "rar"
542|    if suffix in {".zip", ".docx"}:
543|        return "zip"
544|    if suffix in {".tar", ".tgz", ".tar.gz", ".tbz2", ".tar.bz2", ".txz", ".tar.xz"} or tarfile.is_tarfile(path):
545|        return "tar"
546|    if suffix == ".gz":
547|        return "gzip"
548|    if suffix == ".7z":
549|        return "7z"
550|    if suffix == ".rar":
551|        return "rar"
552|    return ""
553|
554|
555|def safe_extract_gzip(path: Path, dest: Path) -> Path:
556|    import gzip
557|
558|    target_name = path.stem or (path.name + ".out")
559|    target = (dest / target_name).resolve()
560|    if not str(target).startswith(str(dest.resolve())):
561|        raise ValueError(f"unsafe gzip output path: {target_name}")
562|    target.parent.mkdir(parents=True, exist_ok=True)
563|    with gzip.open(path, "rb") as src, target.open("wb") as out:
564|        shutil.copyfileobj(src, out)
565|    return target
566|
567|
568|def safe_extract_with_7z(path: Path, dest: Path) -> bool:
569|    exe = shutil.which("7z") or shutil.which("7za") or shutil.which("7zr")
570|    if not exe:
571|        return False
572|    completed = subprocess.run(
573|        [exe, "x", "-y", f"-o{dest}", str(path)],
574|        text=True,
575|        capture_output=True,
576|        timeout=120,
577|    )
578|    if completed.returncode != 0:
579|        raise RuntimeError(completed.stderr.strip() or completed.stdout.strip())
580|    return True
581|
582|
583|def extract_archives(files: Iterable[Path], dest: Path, max_depth: int = 5) -> list[str]:
584|    notes: list[str] = []
585|    dest.mkdir(parents=True, exist_ok=True)
586|    queue: list[tuple[Path, int]] = [(path, 0) for path in files]
587|    seen: set[Path] = set()
588|    while queue:
589|        path, depth = queue.pop(0)
590|        if depth > max_depth:
591|            notes.append(f"skip nested archive beyond depth {max_depth}: {path.name}")
592|            continue
593|        resolved = path.resolve()
594|        if resolved in seen or not path.exists() or not path.is_file():
595|            continue
596|        seen.add(resolved)
597|        kind = archive_kind(path)
598|        if not kind:
599|            continue
600|        out = dest / slugify(path.stem, 80)
601|        try:
602|            before = {p.resolve() for p in out.rglob("*")} if out.exists() else set()
603|            if kind == "zip":
604|                out.mkdir(parents=True, exist_ok=True)
605|                safe_extract_zip(path, out)
606|                notes.append(f"extracted {path.name}")
607|            elif kind == "tar":
608|                out.mkdir(parents=True, exist_ok=True)
609|                safe_extract_tar(path, out)
610|                notes.append(f"extracted {path.name}")
611|            elif kind == "gzip":
612|                out.mkdir(parents=True, exist_ok=True)
613|                safe_extract_gzip(path, out)
614|                notes.append(f"extracted {path.name}")
615|            elif kind in {"rar", "7z"}:
616|                out.mkdir(parents=True, exist_ok=True)
617|                if safe_extract_with_7z(path, out):
618|                    notes.append(f"extracted {path.name}")
619|                else:
620|                    notes.append(f"unsupported archive without 7z: {path.name}")
621|                    continue
622|            after = {p.resolve() for p in out.rglob("*")} if out.exists() else set()
623|            for nested in sorted(after - before):
624|                if nested.is_file() and archive_kind(nested):
625|                    queue.append((nested, depth + 1))
626|        except Exception as exc:  # noqa: BLE001 - keep batch processing alive
627|            notes.append(f"extract failed {path.name}: {exc}")
628|    return notes
629|
630|
631|def find_thermo_for(mech: Path, candidates: list[Path]) -> Path | None:
632|    labels = classify_file(mech)
633|    if "thermo" in labels:
634|        return mech
635|    scored: list[tuple[int, Path]] = []
636|    for path in candidates:
637|        cls = classify_file(path)
638|        if "thermo" in cls:
639|            score = 10
640|            name = path.name.lower()
641|            if "therm" in name:
642|                score += 5
643|            if path.parent == mech.parent:
644|                score += 3
645|            scored.append((score, path))
646|    if not scored:
647|        return None
648|    return sorted(scored, reverse=True)[0][1]
649|
650|
651|def find_transport_for(mech: Path, candidates: list[Path]) -> Path | None:
652|    scored: list[tuple[int, Path]] = []
653|    for path in candidates:
654|        cls = classify_file(path)
655|        if "transport" in cls:
656|            score = 10
657|            name = path.name.lower()
658|            if "tran" in name or "transport" in name:
659|                score += 5
660|            if path.parent == mech.parent:
661|                score += 3
662|            scored.append((score, path))
663|    return sorted(scored, reverse=True)[0][1] if scored else None
664|
665|
666|def detect_plasma_case(record: dict, files: Iterable[Path] = ()) -> str:
667|    text_parts = [
668|        str(record.get("title", "")),
669|        str(record.get("abstract", "")),
670|        str(record.get("keywords", "")),
671|    ]
672|    file_text_parts: list[str] = []
673|    for path in files:
674|        if path.is_file() and looks_like_text(path):
675|            file_text_parts.append(read_text_limited(path, 300_000))
676|    text_parts.extend(file_text_parts)
677|    text = "\n".join(text_parts)
678|    if re.search(r"\b(plasma|dielectric barrier|dbd|nanosecond discharge|glow discharge|electron[-\s]?impact)\b", text, re.I):
679|        return "yes"
680|    file_text = "\n".join(file_text_parts)
681|    if re.search(r"(?m)^\s*(E|E-|e-)\s", file_text) and re.search(r"(?m)^\s*[A-Za-z0-9_()+\-]+\+\s", file_text):
682|        return "possible"
683|    return "no"
684|
685|
686|def short_message(value: str, limit: int = 800) -> str:
687|    value = re.sub(r"\s+", " ", value or "").strip()
688|    if len(value) <= limit:
689|        return value
690|    return value[:limit].rstrip() + " ... [truncated; see _processing logs]"
691|
692|
693|def mechanism_priority(path: Path) -> tuple[int, str]:
694|    name = path.name.lower()
695|    score = 0
696|    if path.suffix.lower() in {".inp", ".dat", ".txt", ".yaml", ".yml", ".cti"}:
697|        score -= 20
698|    if "mech" in name or "mechanism" in name or "model" in name:
699|        score -= 10
700|    if "therm" in name or "tran" in name or "transport" in name:
701|        score += 20
702|    if "document.xml" in name or path.suffix.lower() == ".xml":
703|        score += 50
704|    return score, str(path)
705|
706|
707|@dataclass
708|class CkResult:
709|    status: str
710|    species: str = ""
711|    reactions: str = ""
712|    message: str = ""
713|    chem_out: Path | None = None
714|    cantera_yaml: Path | None = None
715|    method: str = ""
716|    standardized_mech: Path | None = None
717|    standardized_thermo: Path | None = None
718|    standardized_transport: Path | None = None
719|
720|
721|def backup_ck_files() -> dict[str, Path | None]:
722|    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
723|    backups: dict[str, Path | None] = {}
724|    for name in CK_FILES:
725|        path = CKDIR / name
726|        if path.exists():
727|            backup = CKDIR / f"{name}.codex_backup_{stamp}"
728|            shutil.copy2(path, backup)
729|            backups[name] = backup
730|        else:
731|            backups[name] = None
732|    return backups
733|
734|
735|def restore_ck_files(backups: dict[str, Path | None]) -> list[str]:
736|    notes: list[str] = []
737|    for name in CK_FILES:
738|        path = CKDIR / name
739|        backup = backups.get(name)
740|        if backup is None:
741|            if path.exists():
742|                for attempt in range(8):
743|                    try:
744|                        path.unlink()
745|                        break
746|                    except PermissionError:
747|                        time.sleep(0.25 * (attempt + 1))
748|                else:
749|                    notes.append(f"could not remove generated {path}")
750|        elif backup.exists():
751|            restored = False
752|            for attempt in range(8):
753|                try:
754|                    shutil.copy2(backup, path)
755|                    backup.unlink()
756|                    restored = True
757|                    break
758|                except PermissionError:
759|                    time.sleep(0.25 * (attempt + 1))
760|            if not restored:
761|                notes.append(f"could not restore {path}; backup kept at {backup}")
762|    return notes
763|
764|
765|def parse_chem_out(path: Path) -> tuple[str, str]:
766|    text = read_text_limited(path, 1_000_000)
767|    species = ""
768|    reactions = ""
769|    patterns = [
770|        (r"(\d+)\s+SPECIES", "species"),
771|        (r"SPECIES\s*[:=]\s*(\d+)", "species"),
772|        (r"(\d+)\s+REACTIONS", "reactions"),
773|        (r"REACTIONS\s*[:=]\s*(\d+)", "reactions"),
774|        (r"NO\.\s*OF\s*SPECIES\s*=?\s*(\d+)", "species"),
775|        (r"NO\.\s*OF\s*REACTIONS\s*=?\s*(\d+)", "reactions"),
776|    ]
777|    for pattern, kind in patterns:
778|        match = re.search(pattern, text, flags=re.I)
779|        if match and kind == "species" and not species:
780|            species = match.group(1)
781|        if match and kind == "reactions" and not reactions:
782|            reactions = match.group(1)
783|    if not species:
784|        match = re.search(r"SPECIES\s+CONSIDERED[\s\S]+?(?=REACTIONS\s+CONSIDERED|$)", text, flags=re.I)
785|        if match:
786|            nums = [int(n) for n in re.findall(r"^\s*(\d+)\.\s+\S+", match.group(0), flags=re.M)]
787|            if nums:
788|                species = str(max(nums))
789|    if not reactions:
790|        match = re.search(r"REACTIONS\s+CONSIDERED[\s\S]+", text, flags=re.I)
791|        if match:
792|            nums = [int(n) for n in re.findall(r"^\s*(\d+)\.\s+\S", match.group(0), flags=re.M)]
793|            if nums:
794|                reactions = str(max(nums))
795|    return species, reactions
796|
797|
798|def strip_inline_comment(line: str) -> str:
799|    return line.split("!", 1)[0].strip()
800|
801|
802|def section_between(text: str, start: str) -> str:
803|    match = re.search(rf"(^|\n)\s*{start}\b(.*?)(^|\n)\s*END\b", text, flags=re.I | re.S)
804|    return match.group(2) if match else ""
805|
806|
807|def parse_chemkin_source_counts(path: Path) -> tuple[str, str]:
808|    text = read_text_limited(path, 5_000_000)
809|    species_block = section_between(text, "SPECIES")
810|    species_tokens: list[str] = []
811|    for raw in species_block.splitlines():
812|        line = strip_inline_comment(raw)
813|        if line:
814|            species_tokens.extend(line.split())
815|    reaction_block = section_between(text, "REACTIONS")
816|    reaction_count = 0
817|    aux_prefixes = (
818|        "LOW",
819|        "TROE",
820|        "SRI",
821|        "PLOG",
822|        "DUP",
823|        "DUPLICATE",
824|        "REV",
825|        "FORD",
826|        "HV",
827|        "CHEB",
828|        "TCHEB",
829|        "PCHEB",
830|    )
831|    for raw in reaction_block.splitlines():
832|        line = strip_inline_comment(raw)
833|        if not line:
834|            continue
835|        upper = line.upper().lstrip()
836|        if upper.startswith(aux_prefixes):
837|            continue
838|        if "=" in line or "<=>" in line or "=>" in line:
839|            reaction_count += 1
840|    return (str(len(species_tokens)) if species_tokens else "", str(reaction_count) if reaction_count else "")
841|
842|
843|def parse_cantera_yaml_counts(path: Path) -> tuple[str, str]:
844|    if not path.exists():
845|        return "", ""
846|    try:
847|        import yaml  # type: ignore
848|
849|        data = yaml.safe_load(path.read_text(encoding="utf-8", errors="ignore")) or {}
850|        species = data.get("species") or []
851|        reactions = data.get("reactions") or []
852|        species_count = str(len(species)) if isinstance(species, list) and species else ""
853|        reaction_count = str(len(reactions)) if isinstance(reactions, list) and reactions else ""
854|        if species_count or reaction_count:
855|            return species_count, reaction_count
856|    except Exception:
857|        pass
858|
859|    text = path.read_text(encoding="utf-8", errors="ignore").splitlines()
860|    counts = {"species": 0, "reactions": 0}
861|    section: str | None = None
862|    phase_species_tokens: list[str] = []
863|    collecting_phase_species = False
864|    phase_species_text = ""
865|    for line in text:
866|        if re.match(r"^[A-Za-z0-9_-]+:", line):
867|            section = None
868|        stripped = line.strip()
869|        if collecting_phase_species:
870|            phase_species_text += " " + stripped
871|            if "]" in stripped:
872|                inside = phase_species_text.split("[", 1)[1].split("]", 1)[0]
873|                phase_species_tokens.extend(item.strip() for item in inside.split(",") if item.strip())
874|                collecting_phase_species = False
875|                phase_species_text = ""
876|            continue
877|        if stripped.startswith("species:") and line.startswith(" "):
878|            if "[" in stripped:
879|                phase_species_text = stripped
880|                if "]" in stripped:
881|                    inside = stripped.split("[", 1)[1].split("]", 1)[0]
882|                    phase_species_tokens.extend(item.strip() for item in inside.split(",") if item.strip())
883|                    phase_species_text = ""
884|                else:
885|                    collecting_phase_species = True
886|            continue
887|        if line.startswith("species:"):
888|            section = "species"
889|            if "[" in line and "]" in line:
890|                inside = line.split("[", 1)[1].split("]", 1)[0]
891|                counts["species"] += len([item for item in inside.split(",") if item.strip()])
892|            continue
893|        if line.startswith("reactions:"):
894|            section = "reactions"
895|            continue
896|        if section in counts and re.match(r"^\s*-\s+", line):
897|            counts[section] += 1
898|    species_count = counts["species"] or len(dict.fromkeys(phase_species_tokens))
899|    return (str(species_count) if species_count else "", str(counts["reactions"]) if counts["reactions"] else "")
900|
901|
902|def first_chemkin_header_line(path: Path) -> int | None:
903|    lines = read_text_limited(path, 5_000_000).splitlines()
904|    for idx, line in enumerate(lines):
905|        stripped = line.strip().upper()
906|        if stripped.startswith(("ELEMENTS", "SPECIES", "THERMO", "REACTIONS")):
907|            return idx
908|    return None
909|
910|
911|def write_trimmed_chemkin_input(source: Path, target: Path) -> bool:
912|    text = read_text_limited(source, 20_000_000)
913|    lines = text.splitlines()
914|    start = first_chemkin_header_line(source)
915|    if start is None:
916|        return False
917|    trimmed = "\n".join(lines[start:]).lstrip() + "\n"
918|    if "SPECIES CONSIDERED" in trimmed.upper() or "REACTIONS CONSIDERED" in trimmed.upper():
919|        return False
920|    target.write_text(trimmed, encoding="utf-8")
921|    return True
922|
923|
924|def write_cantera_cleaned_chemkin_input(source: Path, target: Path) -> bool:
925|    text = read_text_limited(source, 50_000_000)
926|    if "SPECIES CONSIDERED" in text.upper() or "REACTIONS CONSIDERED" in text.upper():
927|        return False
928|    lines = text.splitlines()
929|    start = first_chemkin_header_line(source)
930|    if start is not None:
931|        lines = lines[start:]
932|    cleaned_lines: list[str] = []
933|    exponent_pattern = re.compile(r"(?<![A-Za-z0-9_])([+-]?(?:\d+\.\d*|\.\d+|\d+))([+-]\d{1,3})(?![A-Za-z0-9_.])")
934|    for raw in lines:
935|        line = raw.replace("\ufeff", "")
936|        line = re.sub(r"(?<=\d),(?=\s|$)", "", line)
937|        line = exponent_pattern.sub(r"\1E\2", line)
938|        cleaned_lines.append(line)
939|    target.write_text("\n".join(cleaned_lines).lstrip() + "\n", encoding="utf-8")
940|    return True
941|
942|
943|def standardize_mechanism_files(mech: Path, thermo: Path | None, transport: Path | None, dest: Path) -> tuple[Path, Path | None, Path | None]:
944|    dest.mkdir(parents=True, exist_ok=True)
945|    chem_target = dest / "chem.inp"
946|    thermo_target = dest / "therm.dat"
947|    transport_target = dest / "tran.dat"
948|    shutil.copy2(mech, chem_target)
949|    thermo_out = None
950|    transport_out = None
951|    if thermo is not None and thermo.exists():
952|        shutil.copy2(thermo, thermo_target)
953|        thermo_out = thermo_target
954|    elif thermo_target.exists():
955|        thermo_target.unlink()
956|    if transport is not None and transport.exists():
957|        shutil.copy2(transport, transport_target)
958|        transport_out = transport_target
959|    elif transport_target.exists():
960|        transport_target.unlink()
961|    return chem_target, thermo_out, transport_out
962|
963|
964|def cantera_convert_once(
965|    mech: Path,
966|    thermo: Path | None,
967|    transport: Path | None,
968|    out_yaml: Path,
969|    log_path: Path,
970|    result_path: Path | None = None,
971|) -> tuple[bool, str, str, str]:
972|    result_path = result_path or log_path.with_suffix(".result.json")
973|    result_path.parent.mkdir(parents=True, exist_ok=True)
974|    if result_path.exists():
975|        result_path.unlink()
976|    code = r"""
977|import json
978|import sys
979|import traceback
980|from pathlib import Path
981|
982|import cantera as ct
983|import cantera.ck2yaml as ck2yaml
984|
985|mech = Path(sys.argv[1])
986|thermo = Path(sys.argv[2]) if sys.argv[2] else None
987|transport = Path(sys.argv[3]) if sys.argv[3] else None
988|out_yaml = Path(sys.argv[4])
989|result_path = Path(sys.argv[5])
990|
991|payload = {"ok": False, "species": "", "reactions": "", "message": ""}
992|try:
993|    suffix = mech.suffix.lower()
994|    if suffix in {".yaml", ".yml", ".cti"} and thermo is None:
995|        if suffix in {".yaml", ".yml"}:
996|            if mech.resolve() != out_yaml.resolve():
997|                out_yaml.write_text(mech.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
998|            gas = ct.Solution(str(out_yaml))
999|        else:
1000|            gas = ct.Solution(str(mech))
1001|    else:
1002|        if hasattr(ck2yaml, "convert_mech"):
1003|            ck2yaml.convert_mech(
1004|                str(mech),
1005|                thermo_file=str(thermo) if thermo else None,
1006|                transport_file=str(transport) if transport else None,
1007|                out_name=str(out_yaml),
1008|                quiet=False,
1009|                permissive=True,
1010|            )
1011|        else:
1012|            ck2yaml.convert(
1013|                str(mech),
1014|                thermo_file=str(thermo) if thermo else None,
1015|                transport_file=str(transport) if transport else None,
1016|                out_name=str(out_yaml),
1017|                quiet=False,
1018|                permissive=True,
1019|            )
1020|        gas = ct.Solution(str(out_yaml))
1021|    payload.update({"ok": True, "species": str(gas.n_species), "reactions": str(gas.n_reactions), "message": "cantera conversion ok"})
1022|except Exception as exc:
1023|    payload["message"] = f"{type(exc).__name__}: {exc}"
1024|    payload["traceback"] = traceback.format_exc()
1025|finally:
1026|    result_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
1027|"""
1028|    try:
1029|        completed = subprocess.run(
1030|            [str(ANALYSIS_PYTHON), "-c", code, str(mech), str(thermo or ""), str(transport or ""), str(out_yaml), str(result_path)],
1031|            text=True,
1032|            capture_output=True,
1033|            timeout=900,
1034|        )
1035|    except subprocess.TimeoutExpired as exc:
1036|        log_path.write_text(
1037|            f"Cantera conversion timed out after {exc.timeout} seconds.\nCOMMAND: {exc.cmd}\n",
1038|            encoding="utf-8",
1039|        )
1040|        return False, "", "", f"TimeoutExpired: Cantera conversion exceeded {exc.timeout} seconds"
1041|    log_path.write_text(
1042|        "PERMISSIVE: True\nSTDOUT:\n" + completed.stdout + "\nSTDERR:\n" + completed.stderr + f"\nRETURN_CODE: {completed.returncode}\n",
1043|        encoding="utf-8",
1044|    )
1045|    if result_path.exists():
1046|        payload = json.loads(result_path.read_text(encoding="utf-8"))
1047|    else:
1048|        payload = {"ok": False, "species": "", "reactions": "", "message": "missing cantera result json"}
1049|    return bool(payload.get("ok")), str(payload.get("species", "")), str(payload.get("reactions", "")), str(payload.get("message", ""))
1050|
1051|
1052|def process_with_cantera(mech: Path, thermo: Path | None, transport: Path | None, dest: Path, work_dest: Path | None = None) -> CkResult:
1053|    chem_target, thermo_target, transport_target = standardize_mechanism_files(mech, thermo, transport, dest)
1054|    work_dest = work_dest or dest
1055|    work_dest.mkdir(parents=True, exist_ok=True)
1056|    yaml_path = dest / "mechanism.yaml"
1057|    log_path = work_dest / "cantera_conversion.log"
1058|    if not ANALYSIS_PYTHON.exists():
1059|        return CkResult(
1060|            "cantera_failed",
1061|            message=f"missing analysis python: {ANALYSIS_PYTHON}",
1062|            standardized_mech=chem_target,
1063|            standardized_thermo=thermo_target,
1064|            standardized_transport=transport_target,
1065|            method="cantera",
1066|        )
1067|    original_suffix = mech.suffix.lower()
1068|    conversion_input = mech if original_suffix in {".yaml", ".yml", ".cti"} else chem_target
1069|    ok, species, reactions, message = cantera_convert_once(conversion_input, None if original_suffix in {".yaml", ".yml", ".cti"} else thermo_target, transport_target, yaml_path, log_path)
    gc.collect()
1070|    if ok:
1071|        return CkResult(
1072|            "ok",
1073|            species=species,
1074|            reactions=reactions,
1075|            message=message,
1076|            cantera_yaml=yaml_path,
1077|            method="cantera",
1078|            standardized_mech=chem_target,
1079|            standardized_thermo=thermo_target,
1080|            standardized_transport=transport_target,
1081|        )
1082|    if "Section starts with unrecognized keyword" in message:
1083|        cleaned = work_dest / "chem_cantera_clean.inp"
1084|        if write_trimmed_chemkin_input(chem_target, cleaned):
1085|            clean_yaml = dest / "mechanism.cleaned.yaml"
1086|            clean_log = work_dest / "cantera_conversion.cleaned.log"
1087|            ok, species, reactions, clean_message = cantera_convert_once(cleaned, thermo_target, transport_target, clean_yaml, clean_log)
1088|            if ok:
1089|                shutil.copy2(cleaned, chem_target)
1090|                shutil.copy2(clean_yaml, yaml_path)
1091|                return CkResult(
1092|                    "ok_after_cleanup",
1093|                    species=species,
1094|                    reactions=reactions,
1095|                    message=f"cleaned leading non-CHEMKIN content; {clean_message}",
1096|                    cantera_yaml=yaml_path,
1097|                    method="cantera",
1098|                    standardized_mech=chem_target,
1099|                    standardized_thermo=thermo_target,
1100|                    standardized_transport=transport_target,
1101|                )
1102|            message = f"{message}; cleanup retry failed: {clean_message}"
1103|        else:
1104|            message = f"{message}; cleanup skipped because file is not a CHEMKIN input"
1105|    if any(token in message for token in ["could not convert string to float", "list index out of range", "Unexpected token"]):
1106|        cleaned = work_dest / "chem_cantera_numeric_clean.inp"
1107|        if write_cantera_cleaned_chemkin_input(chem_target, cleaned):
1108|            clean_yaml = dest / "mechanism.numeric_clean.yaml"
1109|            clean_log = work_dest / "cantera_conversion.numeric_clean.log"
1110|            ok, species, reactions, clean_message = cantera_convert_once(cleaned, thermo_target, transport_target, clean_yaml, clean_log)
1111|            if ok:
1112|                shutil.copy2(cleaned, chem_target)
1113|                shutil.copy2(clean_yaml, yaml_path)
1114|                return CkResult(
1115|                    "ok_after_cleanup",
1116|                    species=species,
1117|                    reactions=reactions,
1118|                    message=f"normalized legacy numeric/reaction syntax; {clean_message}",
1119|                    cantera_yaml=yaml_path,
1120|                    method="cantera",
1121|                    standardized_mech=chem_target,
1122|                    standardized_thermo=thermo_target,
1123|                    standardized_transport=transport_target,
1124|                )
1125|            message = f"{message}; numeric cleanup retry failed: {clean_message}"
1126|    yaml_counts = parse_cantera_yaml_counts(yaml_path) if yaml_path.exists() else ("", "")
1127|    return CkResult(
1128|        "cantera_failed",
1129|        species=yaml_counts[0],
1130|        reactions=yaml_counts[1],
1131|        message=message,
1132|        cantera_yaml=yaml_path if yaml_path.exists() else None,
1133|        method="cantera",
1134|        standardized_mech=chem_target,
1135|        standardized_thermo=thermo_target,
1136|        standardized_transport=transport_target,
1137|    )
1138|
1139|
1140|def run_ckinterp(mech: Path, thermo: Path | None, dest: Path) -> CkResult:
1141|    warning_file = dest / "ckinterp_restore_warnings.txt"
1142|    if warning_file.exists():
1143|        warning_file.unlink()
1144|    if not CKEXE.exists():
1145|        return CkResult("failed", message=f"missing {CKEXE}")
1146|    if thermo is None:
1147|        return CkResult("failed", message="missing therm.dat or embedded THERMO block")
1148|    backups = backup_ck_files()
1149|    try:
1150|        shutil.copy2(mech, CKDIR / "chem.inp")
1151|        shutil.copy2(thermo, CKDIR / "therm.dat")
1152|        completed = subprocess.run(
1153|            [str(CKEXE)],
1154|            cwd=str(CKDIR),
1155|            text=True,
1156|            input="\n",
1157|            capture_output=True,
1158|            timeout=120,
1159|        )
1160|        chem_out = CKDIR / "chem.out"
1161|        dest.mkdir(parents=True, exist_ok=True)
1162|        copied = dest / "ckinterp_chem.out"
1163|        if chem_out.exists():
1164|            shutil.copy2(chem_out, copied)
1165|        else:
1166|            copied.write_text(
1167|                completed.stdout + "\n" + completed.stderr,
1168|                encoding="utf-8",
1169|                errors="ignore",
1170|            )
1171|        species, reactions = parse_chem_out(copied)
1172|        if not species or not reactions:
1173|            source_species, source_reactions = parse_chemkin_source_counts(mech)
1174|            species = species or source_species
1175|            reactions = reactions or source_reactions
1176|        has_errors = "Error..." in read_text_limited(copied, 2_000_000)
1177|        status = "ok_with_ck_warnings" if (species or reactions) and has_errors else ("ok" if species or reactions else "failed")
1178|        return CkResult(
1179|            status=status,
1180|            species=species,
1181|            reactions=reactions,
1182|            message=f"returncode={completed.returncode}",
1183|            chem_out=copied,
1184|        )
1185|    except Exception as exc:  # noqa: BLE001
1186|        return CkResult("failed", message=str(exc))
1187|    finally:
1188|        restore_notes = restore_ck_files(backups)
1189|        if restore_notes:
1190|            warning_file.write_text("\n".join(restore_notes) + "\n", encoding="utf-8")
1191|
1192|
1193|def detect_reactors(record: dict) -> str:
1194|    text = (str(record.get("title", "")) + " " + str(record.get("abstract", ""))).lower()
1195|    found = [label for label, terms in REACTOR_TERMS if any(term in text for term in terms)]
1196|    return ", ".join(dict.fromkeys(found)) if found else "not clear from abstract"
1197|
1198|
1199|def gb_t_7714(record: dict) -> str:
1200|    authors = record.get("authors") or []
1201|    if isinstance(authors, list):
1202|        author_text = ", ".join(str(a) for a in authors[:6])
1203|        if len(authors) > 6:
1204|            author_text += ", et al."
1205|    else:
1206|        author_text = str(authors)
1207|    title = record.get("title", "").rstrip(".")
1208|    volume = record.get("volume", "")
1209|    month = record.get("month", "")
1210|    article = article_id(record)
1211|    doi = normalize_doi(record.get("doi", ""))
1212|    year = record_year(record)
1213|    tail = f"Combustion and Flame, {year}"
1214|    if volume:
1215|        tail += f", {volume}"
1216|    if article:
1217|        tail += f": {article}"
1218|    if doi:
1219|        tail += f". DOI: {doi}"
1220|    return f"{author_text}. {title}[J]. {tail}."
1221|
1222|
1223|def copy_downloads_for_record(record: dict, dest: Path) -> list[Path]:
1224|    dest.mkdir(parents=True, exist_ok=True)
1225|    keys = {normalize_doi(record.get("doi", "")), str(record.get("pii", "")).lower(), article_id(record).lower()}
1226|    copied: list[Path] = []
1227|    seen: set[Path] = set()
1228|    legacy_raw = legacy_processing_folder(record) / "raw_downloads"
1229|    for source_dir in [DOWNLOADS, LEGACY_DOWNLOADS, legacy_raw]:
1230|        if not source_dir.exists():
1231|            continue
1232|        for file in source_dir.glob("*"):
1233|            if not file.is_file() or file.resolve() in seen:
1234|                continue
1235|            seen.add(file.resolve())
1236|            low = file.name.lower()
1237|            if any(key and key.replace("/", "_").replace(".", "_") in low for key in keys) or any(
1238|                key and key in low for key in keys
1239|            ):
1240|                target = dest / file.name
1241|                if not target.exists() or target.stat().st_size != file.stat().st_size:
1242|                    shutil.copy2(file, target)
1243|                copied.append(target)
1244|    return copied
1245|
1246|
1247|def cleanup_inactive_paper_folders(root: Path, active_folders: set[Path]) -> None:
1248|    root = root.resolve()
1249|    active = {path.resolve() for path in active_folders}
1250|    if not root.exists():
1251|        return
1252|    candidate_dirs = {path.parent.resolve() for path in root.rglob("mechanism_summary.md")}
1253|    candidate_dirs |= {path.parent.resolve() for path in root.rglob("chem.inp")}
1254|    for path in list(root.rglob("raw_downloads")) + list(root.rglob("extracted")):
1255|        if not path.is_dir():
1256|            continue
1257|        parent = path.parent
1258|        candidate_dirs.add((parent.parent if parent.name == "_processing" else parent).resolve())
1259|    candidate_dirs = sorted(candidate_dirs, key=lambda p: len(p.parts), reverse=True)
1260|    for paper_dir in candidate_dirs:
1261|        if paper_dir in active or root not in paper_dir.parents or any(part.startswith("_") for part in paper_dir.relative_to(root).parts):
1262|            continue
1263|        if paper_dir.exists():
1264|            shutil.rmtree(paper_dir)
1265|    for directory in sorted((p for p in root.rglob("*") if p.is_dir()), key=lambda p: len(p.parts), reverse=True):
1266|        if any(part.startswith("_") for part in directory.relative_to(root).parts):
1267|            continue
1268|        try:
1269|            directory.rmdir()
1270|        except OSError:
1271|            pass
1272|
1273|
1274|def cleanup_active_paper_folder(folder: Path) -> None:
1275|    allowed_files = {"mechanism_summary.md", "chem.inp", "therm.dat", "tran.dat", "mechanism.yaml"}
1276|    allowed_dirs = {"_processing"}
1277|    if not folder.exists():
1278|        return
1279|    for child in list(folder.iterdir()):
1280|        if child.is_dir():
1281|            if child.name not in allowed_dirs:
1282|                shutil.rmtree(child)
1283|            continue
1284|        if child.name not in allowed_files:
1285|            child.unlink()
1286|
1287|
1288|def url_head(url: str) -> tuple[int, str, int]:
1289|    req = urllib.request.Request(
1290|        url,
1291|        method="HEAD",
1292|        headers={"User-Agent": "Mozilla/5.0"},
1293|    )
1294|    with urllib.request.urlopen(req, timeout=8) as response:
1295|        length = response.headers.get("content-length") or "0"
1296|        return response.status, response.headers.get("content-type") or "", int(length)
1297|
1298|
1299|def url_download(url: str, dest: Path) -> None:
1300|    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
1301|    tmp = dest.with_suffix(dest.suffix + ".part")
1302|    try:
1303|        with urllib.request.urlopen(req, timeout=30) as response, tmp.open("wb") as out:
1304|            shutil.copyfileobj(response, out)
1305|        tmp.replace(dest)
1306|    except Exception:
1307|        if tmp.exists():
1308|            tmp.unlink()
1309|        curl = shutil.which("curl.exe") or shutil.which("curl")
1310|        if not curl:
1311|            raise
1312|        completed = subprocess.run(
1313|            [curl, "-L", "--fail", "--max-time", "90", "-A", "Mozilla/5.0", "-o", str(tmp), url],
1314|            capture_output=True,
1315|            text=True,
1316|            timeout=100,
1317|        )
1318|        if completed.returncode != 0:
1319|            if tmp.exists():
1320|                tmp.unlink()
1321|            raise RuntimeError((completed.stderr or completed.stdout or f"curl failed {completed.returncode}").strip())
1322|        tmp.replace(dest)
1323|
1324|
1325|def probe_supplements(max_mmc: int = 8, year: str | None = None, force: bool = False, serial: bool = False) -> None:
1326|    ensure_dirs()
1327|    records = read_metadata()
1328|    for record in records:
1329|        if not record.get("candidate"):
1330|            continue
1331|        if year and record_year(record) != year:
1332|            continue
1333|        if not force and record.get("supplementProbeStatus") in {"complete", "no_links", "captcha", "error", "partial"}:
1334|            continue
1335|        pii = record.get("pii") or ""
1336|        if not pii:
1337|            continue
1338|        found = record.get("probedSupplementLinks") or []
1339|        found_urls = {item.get("url") for item in found if isinstance(item, dict)}
1340|        if found and not force:
1341|            record["supplementProbeStatus"] = "complete"
1342|            record.setdefault("supplementProbeMethod", "recorded-links")
1343|            write_metadata(records)
1344|            continue
1345|        original_error_count = len(record.get("probeErrors") or [])
1346|        changed = False
1347|        for idx in range(1, max_mmc + 1):
1348|            existing = sorted(DOWNLOADS.glob(f"{pii}_mmc{idx}.*"))
1349|            if existing:
1350|                for target in existing:
1351|                    url = f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}-mmc{idx}{target.suffix}"
1352|                    if url not in found_urls:
1353|                        found.append(
1354|                            {
1355|                                "url": url,
1356|                                "file": str(target),
1357|                                "content_type": "",
1358|                                "content_length": target.stat().st_size,
1359|                            }
1360|                        )
1361|                        found_urls.add(url)
1362|                        changed = True
1363|                continue
1364|            if any(f"-mmc{idx}." in (url or "") for url in found_urls):
1365|                continue
1366|            urls = [(ext, f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}-mmc{idx}.{ext}") for ext in MMC_EXTENSIONS]
1367|            head_results: list[tuple[str, str, int, str]] = []
1368|            with concurrent.futures.ThreadPoolExecutor(max_workers=1 if serial else 8) as executor:
1369|                future_map = {executor.submit(url_head, url): (ext, url) for ext, url in urls}
1370|                for future in concurrent.futures.as_completed(future_map):
1371|                    ext, url = future_map[future]
1372|                    try:
1373|                        status, content_type, length = future.result()
1374|                    except urllib.error.HTTPError as exc:
1375|                        if exc.code != 404:
1376|                            record.setdefault("probeErrors", []).append({"url": url, "error": f"HTTP {exc.code}"})
1377|                            changed = True
1378|                        continue
1379|                    except Exception as exc:  # noqa: BLE001
1380|                        record.setdefault("probeErrors", []).append({"url": url, "error": str(exc)})
1381|                        changed = True
1382|                        continue
1383|                    if status == 200:
1384|                        head_results.append((ext, url, length, content_type))
1385|            if not head_results:
1386|                break
1387|            hit = False
1388|            for ext, url, length, content_type in sorted(head_results, key=lambda item: MMC_EXTENSIONS.index(item[0])):
1389|                url = f"https://ars.els-cdn.com/content/image/1-s2.0-{pii}-mmc{idx}.{ext}"
1390|                target = DOWNLOADS / f"{pii}_mmc{idx}.{ext}"
1391|                if not target.exists() or target.stat().st_size != length:
1392|                    try:
1393|                        url_download(url, target)
1394|                    except Exception as exc:  # noqa: BLE001 - network failures should not stop the batch
1395|                        record.setdefault("probeErrors", []).append({"url": url, "error": str(exc)})
1396|                        changed = True
1397|                        continue
1398|                found.append(
1399|                    {
1400|                        "url": url,
1401|                        "file": str(target),
1402|                        "content_type": content_type,
1403|                        "content_length": length,
1404|                    }
1405|                )
1406|                found_urls.add(url)
1407|                changed = True
1408|                hit = True
1409|                break
1410|            if not hit:
1411|                break
1412|        if found:
1413|            record["probedSupplementLinks"] = found
1414|            changed = True
1415|        error_count = len(record.get("probeErrors") or [])
1416|        if found and error_count > original_error_count:
1417|            record["supplementProbeStatus"] = "partial"
1418|        elif found:
1419|            record["supplementProbeStatus"] = "complete"
1420|        elif error_count > original_error_count:
1421|            record["supplementProbeStatus"] = "error"
1422|        else:
1423|            record["supplementProbeStatus"] = "no_links"
1424|        record["supplementProbeCheckedAt"] = now_iso()
1425|        record["supplementProbeMaxMmc"] = max_mmc
1426|        record["supplementProbeMethod"] = "direct-ars"
1427|        changed = True
1428|        if changed:
1429|            write_metadata(records)
1430|
1431|
1432|def crossref_json(url: str) -> dict:
1433|    req = urllib.request.Request(
1434|        url,
1435|        headers={"User-Agent": "Codex combustion mechanism collection (mailto:none@example.com)"},
1436|    )
1437|    with urllib.request.urlopen(req, timeout=12) as response:
1438|        return json.loads(response.read().decode("utf-8", errors="replace"))
1439|
1440|
1441|def fetch_json(url: str, timeout: int = 20) -> dict:
1442|    req = urllib.request.Request(
1443|        url,
1444|        headers={"User-Agent": "Codex combustion mechanism collection (mailto:none@example.com)", "Accept": "application/json"},
1445|    )
1446|    with urllib.request.urlopen(req, timeout=timeout) as response:
1447|        return json.loads(response.read().decode("utf-8", errors="replace"))
1448|
1449|
1450|def normalize_abstract(value: str) -> str:
1451|    value = html.unescape(value or "")
1452|    value = re.sub(r"<[^>]+>", " ", value)
1453|    value = re.sub(r"^\s*abstract\s*", "", value, flags=re.I)
1454|    value = re.sub(r"\s+", " ", value).strip()
1455|    return value
1456|
1457|
1458|def restore_openalex_abstract(inverted_index: dict) -> str:
1459|    positions: dict[int, str] = {}
1460|    for word, indexes in (inverted_index or {}).items():
1461|        if not isinstance(indexes, list):
1462|            continue
1463|        for index in indexes:
1464|            if isinstance(index, int):
1465|                positions[index] = str(word)
1466|    return " ".join(positions[index] for index in sorted(positions))
1467|
1468|
1469|def fetch_crossref_abstract(doi: str) -> str:
1470|    if not doi:
1471|        return ""
1472|    try:
1473|        data = fetch_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
1474|    except Exception:
1475|        return ""
1476|    return normalize_abstract(data.get("message", {}).get("abstract", ""))
1477|
1478|
1479|def fetch_openalex_abstract(doi: str) -> str:
1480|    if not doi:
1481|        return ""
1482|    try:
1483|        data = fetch_json("https://api.openalex.org/works/https://doi.org/" + urllib.parse.quote(doi))
1484|    except Exception:
1485|        return ""
1486|    return normalize_abstract(restore_openalex_abstract(data.get("abstract_inverted_index") or {}))
1487|
1488|
1489|def fetch_semantic_scholar_abstract(doi: str) -> str:
1490|    if not doi:
1491|        return ""
1492|    url = "https://api.semanticscholar.org/graph/v1/paper/DOI:" + urllib.parse.quote(doi) + "?fields=title,abstract"
1493|    try:
1494|        data = fetch_json(url)
1495|    except Exception:
1496|        return ""
1497|    return normalize_abstract(data.get("abstract") or "")
1498|
1499|
1500|def extract_abstract_from_pdf(pdf_path: Path) -> str:
1501|    pdftotext = shutil.which("pdftotext")
1502|    if not pdftotext or not pdf_path.exists():
1503|        return ""
1504|    try:
1505|        completed = subprocess.run(
1506|            [pdftotext, "-f", "1", "-l", "3", "-layout", str(pdf_path), "-"],
1507|            capture_output=True,
1508|            timeout=30,
1509|        )
1510|    except Exception:
1511|        return ""
1512|    text = completed.stdout.decode("utf-8", errors="replace") if isinstance(completed.stdout, bytes) else completed.stdout
1513|    text = re.sub(r"\s+", " ", text)
1514|    match = re.search(r"\bAbstract\b(.{80,4000}?)(?:\bKeywords?\b|\b1\s*\.?\s*Introduction\b|\bIntroduction\b)", text, flags=re.I)
1515|    if not match:
1516|        return ""
1517|    return normalize_abstract(match.group(1))
1518|
1519|
1520|def find_local_pdf(folder: Path) -> Path | None:
1521|    if not folder.exists():
1522|        return None
1523|    pdfs = sorted(path for path in folder.rglob("*.pdf") if path.is_file())
1524|    return pdfs[0] if pdfs else None
1525|
1526|
1527|def active_folders_from_index() -> dict[str, Path]:
1528|    index = ROOT / "collection_index.csv"
1529|    if not index.exists():
1530|        return {}
1531|    with index.open("r", newline="", encoding="utf-8-sig") as fh:
1532|        rows = list(csv.DictReader(fh))
1533|    return {
1534|        row.get("article_number", ""): Path(row["folder"])
1535|        for row in rows
1536|        if row.get("folder") and row.get("status") in {"included", "conversion_failed"}
1537|    }
1538|
1539|
1540|def enrich_abstracts() -> None:
1541|    ensure_dirs()
1542|    records = read_metadata()
1543|    active_folders = active_folders_from_index()
1544|    changed = False
1545|    for record in records:
1546|        article = article_id(record)
1547|        if active_folders and article not in active_folders:
1548|            continue
1549|        existing = normalize_abstract(record.get("abstract", ""))
1550|        if existing:
1551|            continue
1552|        folder = active_folders.get(article) or record_folder(record)
1553|        local_pdf = find_local_pdf(folder)
1554|        sources = [
1555|            ("local_pdf", lambda: extract_abstract_from_pdf(local_pdf) if local_pdf else ""),
1556|            ("crossref", lambda: fetch_crossref_abstract(normalize_doi(record.get("doi", "")))),
1557|            ("openalex", lambda: fetch_openalex_abstract(normalize_doi(record.get("doi", "")))),
1558|            ("semantic_scholar", lambda: fetch_semantic_scholar_abstract(normalize_doi(record.get("doi", "")))),
1559|        ]
1560|        for source, getter in sources:
1561|            abstract = getter()
1562|            if abstract:
1563|                record["abstract"] = abstract
1564|                record["abstractSource"] = source
1565|                changed = True
1566|                break
1567|        if not record.get("abstract"):
1568|            record["abstractStatus"] = "not available from local PDF/Crossref/OpenAlex/Semantic Scholar"
1569|            changed = True
1570|        time.sleep(0.1)
1571|    if changed:
1572|        write_metadata(records)
1573|
1574|
1575|def clean_title(value: str) -> str:
1576|    value = re.sub(r"<[^>]+>", "", value or "")
1577|    value = re.sub(r"[^a-z0-9]+", " ", value.lower())
1578|    return re.sub(r"\s+", " ", value).strip()
1579|
1580|
1581|def title_similarity(left: str, right: str) -> float:
1582|    return difflib.SequenceMatcher(None, clean_title(left), clean_title(right)).ratio()
1583|
1584|
1585|def enrich_crossref() -> None:
1586|    ensure_dirs()
1587|    records = read_metadata()
1588|    for record in records:
1589|        if not record.get("candidate"):
1590|            continue
1591|        if record.get("doi"):
1592|            continue
1593|        title = record.get("title") or ""
1594|        if not title:
1595|            continue
1596|        url = (
1597|            "https://api.crossref.org/works?rows=5&filter=type:journal-article&query.title="
1598|            + urllib.parse.quote(title)
1599|        )
1600|        try:
1601|            data = crossref_json(url)
1602|        except Exception as exc:  # noqa: BLE001
1603|            record["crossrefError"] = str(exc)
1604|            continue
1605|        best = None
1606|        best_score = 0.0
1607|        for item in data.get("message", {}).get("items", []):
1608|            item_title = (item.get("title") or [""])[0]
1609|            venue = " ".join(item.get("container-title") or [])
1610|            if "combustion and flame" not in venue.lower():
1611|                continue
1612|            score = title_similarity(title, item_title)
1613|            if score > best_score:
1614|                best = item
1615|                best_score = score
1616|        if not best or best_score < 0.86:
1617|            continue
1618|        record["doi"] = best.get("DOI", record.get("doi", ""))
1619|        record["crossrefScore"] = round(best_score, 3)
1620|        if best.get("article-number") and not record.get("articleNumber"):
1621|            record["articleNumber"] = str(best["article-number"])
1622|        if best.get("volume") and not record.get("volume"):
1623|            record["volume"] = str(best["volume"])
1624|        if not record.get("authors") and best.get("author"):
1625|            authors = []
1626|            for author in best["author"]:
1627|                given = author.get("given", "")
1628|                family = author.get("family", "")
1629|                name = f"{given} {family}".strip()
1630|                if name:
1631|                    authors.append(name)
1632|            record["authors"] = authors
1633|        write_metadata(records)
1634|        time.sleep(0.1)
1635|
1636|
1637|def import_sciencedirect_volume_metadata(source_dir: Path, default_year: str) -> None:
1638|    ensure_dirs()
1639|    records = read_metadata()
1640|    changed = normalize_record_years(records)
1641|    by_pii = {str(record.get("pii", "")).lower(): record for record in records if record.get("pii")}
1642|    for file in sorted(source_dir.glob("volume_*.json")):
1643|        volume_records = json.loads(file.read_text(encoding="utf-8-sig"))
1644|        for incoming in volume_records:
1645|            if not incoming.get("pii"):
1646|                continue
1647|            incoming["year"] = str(incoming.get("year") or default_year)
1648|            key = str(incoming["pii"]).lower()
1649|            existing = by_pii.get(key)
1650|            if existing:
1651|                for field in [
1652|                    "year",
1653|                    "volume",
1654|                    "month",
1655|                    "issueUrl",
1656|                    "issueText",
1657|                    "title",
1658|                    "authors",
1659|                    "doi",
1660|                    "articleNumber",
1661|                    "url",
1662|                    "issuePdfLink",
1663|                    "articleType",
1664|                    "access",
1665|                ]:
1666|                    if incoming.get(field) and not existing.get(field):
1667|                        existing[field] = incoming[field]
1668|                        changed = True
1669|                continue
1670|            records.append(incoming)
1671|            by_pii[key] = incoming
1672|            changed = True
1673|    if changed:
1674|        write_metadata(records)
1675|
1676|
1677|def import_page_supplement_links(source_dir: Path) -> None:
1678|    ensure_dirs()
1679|    records = read_metadata()
1680|    by_pii = {str(record.get("pii", "")).lower(): record for record in records if record.get("pii")}
1681|    changed = False
1682|    for file in sorted(source_dir.glob("chunk_*.json")):
1683|        chunk = json.loads(file.read_text(encoding="utf-8-sig"))
1684|        for item in chunk:
1685|            record = by_pii.get(str(item.get("pii", "")).lower())
1686|            if not record:
1687|                continue
1688|            links = []
1689|            for link in item.get("links", []):
1690|                href = link.get("href") or ""
1691|                if re.search(r"-mmc\d+\.", href, re.I):
1692|                    links.append(
1693|                        {
1694|                            "url": href,
1695|                            "text": link.get("text", ""),
1696|                            "source": "ScienceDirect article page",
1697|                        }
1698|                    )
1699|            if not links:
1700|                if item.get("captcha"):
1701|                    record["articlePageSupplementStatus"] = "captcha"
1702|                    record["supplementProbeStatus"] = "captcha"
1703|                    record["supplementProbeMethod"] = "ScienceDirect article page"
1704|                    record["supplementProbeCheckedAt"] = now_iso()
1705|                    changed = True
1706|                continue
1707|            existing_urls = {
1708|                link.get("url")
1709|                for link in (record.get("probedSupplementLinks") or [])
1710|                if isinstance(link, dict)
1711|            }
1712|            supplement_links = record.setdefault("probedSupplementLinks", [])
1713|            for link in links:
1714|                if link["url"] not in existing_urls:
1715|                    supplement_links.append(link)
1716|                    existing_urls.add(link["url"])
1717|                    changed = True
1718|            record["articlePageSupplementStatus"] = "links imported"
1719|            record["supplementProbeStatus"] = "complete"
1720|            record["supplementProbeMethod"] = "ScienceDirect article page"
1721|            record["supplementProbeCheckedAt"] = now_iso()
1722|    if changed:
1723|        write_metadata(records)
1724|
1725|
1726|def download_recorded_supplements(year: str | None = None, force: bool = False) -> None:
1727|    ensure_dirs()
1728|    records = read_metadata()
1729|    changed = False
1730|    for record in records:
1731|        if year and record_year(record) != year:
1732|            continue
1733|        links = supplement_links_for_record(record)
1734|        if not links:
1735|            if record.get("supplementDownloadStatus") != "none":
1736|                record["supplementDownloadStatus"] = "none"
1737|                changed = True
1738|            continue
1739|        if not force and record.get("supplementDownloadStatus") == "complete":
1740|            if all(link.get("file") and Path(str(link["file"])).exists() and Path(str(link["file"])).stat().st_size for link in links):
1741|                continue
1742|        if not force and record.get("supplementDownloadStatus") in {"failed", "partial"}:
1743|            continue
1744|        any_file = False
1745|        any_failure = False
1746|        for idx, link in enumerate(links, 1):
1747|            url = link.get("url") or ""
1748|            if not url:
1749|                continue
1750|            if not force and link.get("downloadStatus") == "failed":
1751|                any_failure = True
1752|                continue
1753|            existing_file = Path(str(link.get("file", ""))) if link.get("file") else None
1754|            if existing_file and existing_file.exists() and existing_file.stat().st_size:
1755|                any_file = True
1756|                if link.get("downloadStatus") != "existing":
1757|                    link["downloadStatus"] = "existing"
1758|                    changed = True
1759|                continue
1760|            suffix = Path(urllib.parse.urlparse(url).path).suffix or ".dat"
1761|            match = re.search(r"-mmc(\d+)", url, re.I)
1762|            mmc = match.group(1) if match else str(idx)
1763|            pii = record.get("pii") or "unknown"
1764|            target = DOWNLOADS / f"{pii}_mmc{mmc}{suffix}"
1765|            if target.exists() and target.stat().st_size:
1766|                link["file"] = str(target)
1767|                link["content_length"] = target.stat().st_size
1768|                link["downloadStatus"] = "existing"
1769|                any_file = True
1770|                changed = True
1771|                continue
1772|            try:
1773|                url_download(url, target)
1774|                link["file"] = str(target)
1775|                link["content_length"] = target.stat().st_size
1776|                link["downloadStatus"] = "downloaded"
1777|                link["downloadedAt"] = now_iso()
1778|                any_file = True
1779|                changed = True
1780|            except Exception as exc:  # noqa: BLE001
1781|                record.setdefault("supplementDownloadErrors", []).append({"url": url, "error": str(exc)})
1782|                link["downloadStatus"] = "failed"
1783|                link["downloadError"] = str(exc)
1784|                any_failure = True
1785|                changed = True
1786|        if all(link.get("file") and Path(str(link["file"])).exists() and Path(str(link["file"])).stat().st_size for link in links):
1787|            status = "complete"
1788|        elif any_file and any_failure:
1789|            status = "partial"
1790|        elif any_file:
1791|            status = "partial"
1792|        elif any_failure:
1793|            status = "failed"
1794|        else:
1795|            status = "none"
1796|        if record.get("supplementDownloadStatus") != status:
1797|            record["supplementDownloadStatus"] = status
1798|            changed = True
1799|        record["supplementDownloadCheckedAt"] = now_iso()
1800|    if changed:
1801|        write_metadata(records)
1802|
1803|
1804|def scan_files(paths: list[Path]) -> tuple[list[Path], list[Path], list[Path], list[Path]]:
1805|    all_files: list[Path] = []
1806|    for base in paths:
1807|        if base.is_file():
1808|            all_files.append(base)
1809|        elif base.is_dir():
1810|            all_files.extend([p for p in base.rglob("*") if p.is_file()])
1811|    mechanisms: list[Path] = []
1812|    thermos: list[Path] = []
1813|    transports: list[Path] = []
1814|    cantera: list[Path] = []
1815|    for path in all_files:
1816|        labels = classify_file(path)
1817|        if "chemkin_mechanism" in labels:
1818|            mechanisms.append(path)
1819|        if "thermo" in labels:
1820|            thermos.append(path)
1821|        if "transport" in labels:
1822|            transports.append(path)
1823|        if "cantera" in labels:
1824|            cantera.append(path)
1825|    return mechanisms, thermos, transports, cantera
1826|
1827|
1828|def write_summary(
1829|    record: dict,
1830|    dest: Path,
1831|    mechanism_files: list[Path],
1832|    thermo_files: list[Path],
1833|    transport_files: list[Path],
1834|    processing_results: list[CkResult],
1835|    extraction_notes: list[str],
1836|) -> None:
1837|    rel = lambda p: str(p.relative_to(dest)) if p and str(p).startswith(str(dest)) else str(p)
1838|    plasma_flag = detect_plasma_case(record, [*mechanism_files, *thermo_files, *transport_files])
1839|    lines = [
1840|        f"# {record.get('title', 'Untitled')}",
1841|        "",
1842|        "## Bibliography",
1843|        "",
1844|        gb_t_7714(record),
1845|        "",
1846|        "## Metadata",
1847|        "",
1848|        f"- Journal: Combustion and Flame",
1849|        f"- Volume/issue month: {record.get('volume', '')} / {record.get('month', '')}",
1850|        f"- Article number: {article_id(record)}",
1851|        f"- DOI: {record.get('doi', '')}",
1852|        f"- ScienceDirect URL: {record.get('url', '')}",
1853|        f"- Paper PDF: {record.get('paperPdfStatus', 'pending manual download')}",
1854|        f"- Paper PDF link: {record.get('issuePdfLink', '')}",
1855|        f"- Fuel type: {record.get('fuelType') or detect_fuel(record)}",
1856|        f"- Plasma-related mechanism: {plasma_flag}",
1857|        f"- Validation reactor/type from abstract: {detect_reactors(record)}",
1858|        "",
1859|        "## Mechanism Files",
1860|        "",
1861|        f"- Standard mechanism file: chem.inp" if any(r.standardized_mech for r in processing_results) else "- Standard mechanism file: not available",
1862|        f"- Standard thermodynamic file: therm.dat" if any(r.standardized_thermo for r in processing_results) else "- Standard thermodynamic file: not available",
1863|        f"- Standard transport file: tran.dat" if any(r.standardized_transport for r in processing_results) else "- Standard transport file: not available",
1864|        f"- Original mechanism source files: {', '.join(rel(p) for p in mechanism_files) if mechanism_files else 'not found'}",
1865|        f"- Original thermodynamic source files: {', '.join(rel(p) for p in thermo_files) if thermo_files else 'not found'}",
1866|        f"- Original transport source files: {', '.join(rel(p) for p in transport_files) if transport_files else 'not found'}",
1867|        "",
1868|        "## Cantera Preprocessing Results",
1869|        "",
1870|    ]
1871|    if processing_results:
1872|        for idx, result in enumerate(processing_results, 1):
1873|            lines.extend(
1874|                [
1875|                    f"### Mechanism {idx}",
1876|                    "",
1877|                    f"- Status: {result.status}",
1878|                    f"- Species count: {result.species or 'not parsed'}",
1879|                    f"- Reaction count: {result.reactions or 'not parsed'}",
1880|                    f"- Message: {short_message(result.message)}",
1881|                    f"- Method: {result.method or 'not available'}",
1882|                    f"- Cantera YAML: {rel(result.cantera_yaml) if result.cantera_yaml else 'not available'}",
1883|                    f"- Standard chem.inp: {rel(result.standardized_mech) if result.standardized_mech else 'not available'}",
1884|                    f"- Standard therm.dat: {rel(result.standardized_thermo) if result.standardized_thermo else 'not available'}",
1885|                    f"- Standard tran.dat: {rel(result.standardized_transport) if result.standardized_transport else 'not available'}",
1886|                    "",
1887|                ]
1888|            )
1889|    else:
1890|        lines.extend(["- Status: not run", "- Species count: not available", "- Reaction count: not available", ""])
1891|    lines.extend(
1892|        [
1893|            "## Abstract",
1894|            "",
1895|            record.get("abstract") or "not available",
1896|            "",
1897|            "## Processing Notes",
1898|            "",
1899|        ]
1900|    )
1901|    if extraction_notes:
1902|        lines.extend([f"- {note}" for note in extraction_notes])
1903|    else:
1904|        lines.append("- none")
1905|    dest.joinpath("mechanism_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
1906|
1907|
1908|def index_row(
1909|    record: dict,
1910|    candidate: bool,
1911|    status: str,
1912|    folder: Path | str | None = None,
1913|    mechanism_files: list[Path] | None = None,
1914|    thermo_files: list[Path] | None = None,
1915|    transport_files: list[Path] | None = None,
1916|    processing_results: list[CkResult] | None = None,
1917|    plasma_flag: bool | str = "",
1918|) -> dict[str, str]:
1919|    mechanism_files = mechanism_files or []
1920|    thermo_files = thermo_files or []
1921|    transport_files = transport_files or []
1922|    processing_results = processing_results or []
1923|    last = processing_results[-1] if processing_results else None
1924|    folder_text = str(folder or "")
1925|    return {
1926|        "title": str(record.get("title", "") or ""),
1927|        "authors": "; ".join(record.get("authors", [])) if isinstance(record.get("authors"), list) else str(record.get("authors", "") or ""),
1928|        "doi": str(record.get("doi", "") or ""),
1929|        "pii": str(record.get("pii", "") or ""),
1930|        "volume": str(record.get("volume", "") or ""),
1931|        "month": str(record.get("month", "") or ""),
1932|        "article_number": article_id(record),
1933|        "fuel_type": str(record.get("fuelType", "") or ""),
1934|        "plasma_related": str(plasma_flag),
1935|        "url": str(record.get("url", "") or ""),
1936|        "paper_pdf_link": str(record.get("issuePdfLink", "") or ""),
1937|        "paper_pdf_status": str(record.get("paperPdfStatus", "") or ""),
1938|        "candidate": str(bool(candidate)),
1939|        "status": status,
1940|        "folder": folder_text,
1941|        "mechanism_files": "; ".join(str(p) for p in mechanism_files),
1942|        "thermo_files": "; ".join(str(p) for p in thermo_files),
1943|        "transport_files": "; ".join(str(p) for p in transport_files),
1944|        "standard_mechanism": str(last.standardized_mech) if last and last.standardized_mech else "",
1945|        "standard_thermo": str(last.standardized_thermo) if last and last.standardized_thermo else "",
1946|        "standard_transport": str(last.standardized_transport) if last and last.standardized_transport else "",
1947|        "cantera_yaml": str(last.cantera_yaml) if last and last.cantera_yaml else "",
1948|        "species": str(last.species) if last and last.species else "",
1949|        "reactions": str(last.reactions) if last and last.reactions else "",
1950|        "preprocess_status": str(last.status) if last else "",
1951|    }
1952|
1953|
1954|def reusable_existing_row(record: dict, existing_row: dict[str, str] | None, folder: Path, force: bool) -> dict[str, str] | None:
1955|    if force or not existing_row:
1956|        return None
1957|    status = record.get("processingStatus") or existing_row.get("status", "")
1958|    if status not in TERMINAL_PROCESSING_STATUSES:
1959|        return None
1960|    if status in ACTIVE_STATUSES:
1961|        summary = folder / "mechanism_summary.md"
1962|        if not summary.exists():
1963|            return None
1964|        if status == "included" and not (folder / "chem.inp").exists() and not (folder / "mechanism.yaml").exists():
1965|            return None
1966|    row = clean_index_row(existing_row)
1967|    row["fuel_type"] = record.get("fuelType", row.get("fuel_type", ""))
1968|    row["candidate"] = str(bool(record.get("candidate")))
1969|    row["status"] = status
1970|    record["processingStatus"] = status
1971|    if not record.get("processingSkipReason"):
1972|        record["processingSkipReason"] = "reused existing terminal processing state from collection_index.csv"
1973|    return row
1974|
1975|
1976|def update_record_processing_state(
1977|    record: dict,
1978|    row: dict[str, str],
1979|    local_downloads: list[Path],
1980|    mechanism_files: list[Path],
1981|    thermo_files: list[Path],
1982|    transport_files: list[Path],
1983|) -> None:
1984|    record["processingStatus"] = row["status"]
1985|    record["processedAt"] = now_iso()
1986|    record["processingFolder"] = row["folder"]
1987|    record["processedSupplementLinkCount"] = len(supplement_links_for_record(record))
1988|    record["processedLocalDownloadCount"] = len(local_downloads)
1989|    record["processingMechanismFiles"] = row["mechanism_files"]
1990|    record["processingThermoFiles"] = row["thermo_files"]
1991|    record["processingTransportFiles"] = row["transport_files"]
1992|    record["processingStandardMechanism"] = row["standard_mechanism"]
1993|    record["processingStandardThermo"] = row["standard_thermo"]
1994|    record["processingStandardTransport"] = row["standard_transport"]
1995|    record["processingCanteraYaml"] = row["cantera_yaml"]
1996|    record["processingSpecies"] = row["species"]
1997|    record["processingReactions"] = row["reactions"]
1998|    record["processingPreprocessStatus"] = row["preprocess_status"]
1999|    record["processingMechanismFileCount"] = len(mechanism_files)
2000|    record["processingThermoFileCount"] = len(thermo_files)
2001|
# Reproducing The Mechanism Collection Workflow

This guide covers collecting, downloading, and summarizing Combustion and Flame chemical kinetic mechanism supplements. The workflow is resumable — steps that have already completed are skipped unless `--force` is used.

## 1. What This Repository Does

The main script `scripts/collect_cf2026.py` handles:

- Import article metadata (from Crossref API or ScienceDirect volume JSONs).
- Identify reaction-kinetics candidates from titles and abstracts.
- Probe and download supplementary materials from Elsevier's `mmc` CDN links.
- Recursively extract archives (up to 5 levels deep).
- Detect CHEMKIN, Cantera, thermodynamic, and transport files by content markers.
- Standardize files as `chem.inp`, `therm.dat`, and `tran.dat`.
- Convert mechanisms with Cantera `ck2yaml --permissive`.
- Count species and reactions from Cantera output or generated YAML.
- Write `mechanism_summary.md` for each mechanism folder.
- Maintain `collection_index.csv`, `manual_download_handoff.md`, `run_summary.json`.

Additional scripts:

- `scripts/enrich_abstracts.py` — fetch article abstracts via Elsevier API.
- `scripts/scihub_dl.py` — download full-text PDFs for ≤2021 articles via Sci-Hub CDN (no captcha).

## 2. Directory Layout

```text
combustion_and_flame_mechanisms/
  fuel_type/
    year/
      firstauthorsurname_year_fueltype_articlenumber/
        mechanism_summary.md      # Article summary with abstract
        chem.inp                  # Standardized mechanism
        therm.dat                 # Standardized thermodynamic data
        tran.dat                  # Standardized transport data
        mechanism.yaml            # Cantera YAML (if conversion succeeded)
        {surname}_{year}_{fuel}_{article}.pdf   # Full-text PDF (if downloaded)
        _processing/              # Raw downloads, extraction, conversion logs
  collection_index.csv            # Article-level index
  manual_download_handoff.md      # Items needing manual access
  run_summary.json                # Counts and metadata
  _raw/
    article_metadata.json         # Per-article resume state
    downloads/                    # Raw supplement downloads
```

## 3. Required Software

- Python 3.10+
- Cantera 3.x and PyYAML (see `requirements.txt`)
- Git
- Optional: `7z` for `.rar`/`.7z` supplements, `curl` for fallback downloads

Setup:

```bash
git clone https://github.com/wangdu817/Combustion-chemical-kinetic-models.git
cd Combustion-chemical-kinetic-models
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 4. Environment Variables

```bash
export MECH_COLLECTION_WORKSPACE=/path/to/repo          # defaults to repo root
export MECH_COLLECTION_ROOT=/path/to/output             # defaults to repo/combustion_and_flame_mechanisms
export MECH_COLLECTION_PYTHON=/path/to/python            # Python for Cantera subprocess
```

If `MECH_COLLECTION_PYTHON` is unset, the current `sys.executable` is used. The Python interpreter MUST have Cantera importable — on Linux systems with uv-managed Python, you may need to `pip install cantera --break-system-packages` into the resolved Python.

## 5. Resume State

Per-article state is stored in `_raw/article_metadata.json`. Key fields:

- `supplementProbeStatus`: `complete`, `no_links`, `captcha`, `error`, `partial`
- `supplementDownloadStatus`: `complete`, `partial`, `failed`, `none`
- `processingStatus`: `included`, `conversion_failed`, `excluded_no_mechanism_attachment`, etc.
- `downloadStatus`: per-link (`downloaded`, `existing`, `failed`)

Default behavior: each step skips records with terminal status. Use `--force` only for deliberate re-runs.

## 6. Adding A New Year

### 6.1 Fetch Metadata from Crossref

If you can't scrape ScienceDirect issue pages, use the Crossref API to get article metadata with PIIs (needed for CDN probing):

```bash
.venv/bin/python scripts/collect_cf2026.py import-sciencedirect-metadata \
  --year 20XX \
  --source-dir combustion_and_flame_mechanisms/_raw/20XX_volumes
```

The volume JSON files should contain `doi`, `pii`, `title`, `authors`, `volume`, `month`, `articleNumber`, `url`.

### 6.2 Probe and Download Supplements

```bash
# Default: probes up to 12 mmc links per article with all available CPU cores
.venv/bin/python scripts/collect_cf2026.py probe-supplements --year 20XX --max-mmc 12
.venv/bin/python scripts/collect_cf2026.py download-supplements --year 20XX
.venv/bin/python scripts/collect_cf2026.py process --force --year 20XX
```

The probe step checks `https://ars.els-cdn.com/content/image/1-s2.0-{PII}-mmc{N}.{ext}` for each candidate article. Found files are downloaded immediately. `ThreadPoolExecutor` default workers = `os.cpu_count() + 4`.

### 6.3 Enrich Abstracts

```bash
# Set up API key (one-time)
cp api_keys.example.json api_keys.json
# Edit api_keys.json with your Elsevier API key from https://dev.elsevier.com/

.venv/bin/python scripts/enrich_abstracts.py
.venv/bin/python scripts/collect_cf2026.py process --force
```

Public APIs (Crossref, OpenAlex, Semantic Scholar) rarely have abstracts for paywalled C&F articles. The Elsevier API provides full abstracts.

### 6.4 Download Full-Text PDFs

Only articles published in **2021 or earlier** are available via Sci-Hub CDN (no captcha needed):

```bash
.venv/bin/python scripts/scihub_dl.py
```

PDFs are downloaded from `sci.bban.top` and saved alongside mechanism files with matching naming convention. Articles 2022+ are skipped.

## 7. Complete Workflow (New Year)

```bash
# Set up
cp api_keys.example.json api_keys.json  # edit with your Elsevier key

# Metadata
.venv/bin/python scripts/collect_cf2026.py import-sciencedirect-metadata \
  --year 2020 --source-dir combustion_and_flame_mechanisms/_raw/2020_volumes

# Supplement discovery (parallel, all cores)
.venv/bin/python scripts/collect_cf2026.py probe-supplements --year 2020 --max-mmc 12
.venv/bin/python scripts/collect_cf2026.py download-supplements --year 2020
.venv/bin/python scripts/collect_cf2026.py process --force --year 2020

# Abstracts
.venv/bin/python scripts/enrich_abstracts.py
.venv/bin/python scripts/collect_cf2026.py process --force --year 2020

# PDFs (if year ≤ 2021)
.venv/bin/python scripts/scihub_dl.py
```

## 8. Git Hygiene

Safe files to commit:

- `scripts/`, `docs/`, `README.md`
- `environment.yml`, `requirements.txt`
- `api_keys.example.json`
- `combustion_and_flame_mechanisms/README.md`
- `combustion_and_flame_mechanisms/collection_index.csv`
- `combustion_and_flame_mechanisms/manual_download_handoff.md`
- `combustion_and_flame_mechanisms/run_summary.json`
- `combustion_and_flame_mechanisms/_raw/article_metadata.json`
- `combustion_and_flame_mechanisms/**/mechanism_summary.md`
- `combustion_and_flame_mechanisms/**/chem.inp`
- `combustion_and_flame_mechanisms/**/therm.dat`
- `combustion_and_flame_mechanisms/**/tran.dat`
- `combustion_and_flame_mechanisms/**/mechanism.yaml`

Never commit: `api_keys.json`, PDFs, `_processing/`, `_raw/downloads/`, `*.zip`, `*.rar`.

## 9. Quality Checks

```bash
python - <<'PY'
import csv
from collections import Counter
with open('combustion_and_flame_mechanisms/collection_index.csv', encoding='utf-8-sig', newline='') as f:
    print(Counter(row['status'] for row in csv.DictReader(f)))
PY
```

## 10. Current Collection

| Year | Articles | Mechanisms | Cantera OK | Abstracts |
|------|----------|------------|------------|-----------|
| 2015 | 397 | 29 | 10 | 29 |
| 2018 | 479 | 23 | 5 | — |
| 2019 | 462 | 32 | — | — |
| 2020 | 481 | 27 | 15 | 25 |
| 2021 | 521 | 46 | 19 | 46 |
| 2022 | 642 | 55 | 26 | 55 |
| 2023 | 525 | 49 | 24 | 49 |
| 2024 | 568 | 67 | 30 | 67 |
| 2025 | 631 | 64 | 21 | 63 |
| 2026 | 485 | 42 | 21 | — |

**Parallel mode:** `ThreadPoolExecutor` default workers (`os.cpu_count()+4`), max 12 mmc links per article. 
**Cantera:** Uses `.venv/bin/python` symlink to ensure cantera importable.
**Push:** Only mechanism files, summaries, and PDFs via `scripts/safe_push.sh`.

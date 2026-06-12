# Reproducing The Mechanism Collection Workflow

This guide is for users who clone this repository on another computer and want to collect, download, and summarize Combustion and Flame chemical kinetic mechanism supplements. Codex is not required. An agent can help with browser automation, but the same workflow can be run manually with Python and a normal browser.

The workflow is resumable by design. Do not repeatedly visit article pages or re-download files that already have terminal status records in `combustion_and_flame_mechanisms/_raw/article_metadata.json`.

## 1. What The Repository Does

The script `scripts/collect_cf2026.py` handles the local and reproducible parts:

- Import article metadata harvested from ScienceDirect issue pages.
- Identify reaction-kinetics candidates from titles and abstracts.
- Record supplementary-material links and download attachments when direct links are available.
- Recursively extract archives, including nested archives.
- Detect CHEMKIN, Cantera, thermodynamic, and transport files by content markers.
- Standardize files as `chem.inp`, `therm.dat`, and `tran.dat`.
- Convert CHEMKIN mechanisms with Cantera `ck2yaml --permissive`.
- Count species and reactions from Cantera output or generated YAML.
- Write `mechanism_summary.md` for each mechanism folder.
- Maintain `collection_index.csv`, `manual_download_handoff.md`, `run_summary.json`, and per-article resume state.

It does not bypass ScienceDirect access controls. If login, institutional SSO, CAPTCHA, or license confirmation is required, a human must complete that step in the browser.

## 2. Directory Layout

After processing, the collection is organized by fuel first, year second:

```text
combustion_and_flame_mechanisms/
  fuel_type/
    year/
      firstauthorsurname_year_fueltype_articlenumber/
        mechanism_summary.md
        chem.inp
        therm.dat
        tran.dat
        mechanism.yaml
        _processing/
  collection_index.csv
  manual_download_handoff.md
  run_summary.json
  _raw/
    article_metadata.json
    downloads/
```

The top level of each paper folder keeps only the summary and standardized mechanism files. Raw downloads, extracted attachments, conversion logs, and intermediate files stay under that paper's `_processing/` folder.

## 3. Required Software

Required:

- Git.
- Python 3.10 or newer.
- Cantera 3.x.
- PyYAML.
- A normal browser, preferably Chrome or Edge, for ScienceDirect login and manual supplement access.

Optional but recommended:

- `7z` / `7za` / `7zr` on `PATH` for `.rar` and `.7z` supplements.
- `curl` on `PATH` for fallback Elsevier CDN downloads.
- `pdftotext` on `PATH` if you want abstracts extracted from local PDFs before online metadata APIs.

Create the recommended Conda environment:

```bash
git clone https://github.com/wangdu817/Combustion-chemical-kinetic-models.git
cd Combustion-chemical-kinetic-models
conda env create -f environment.yml
conda activate mechanism-collection
python -c "import cantera, yaml; print(cantera.__version__)"
```

If you do not use Conda, install equivalent packages in your own Python environment:

```bash
python -m pip install -r requirements.txt
```

## 4. Paths And Environment Variables

By default, the script uses the cloned repository root as the workspace and writes to:

```text
combustion_and_flame_mechanisms/
```

You can override paths without editing the script:

```bash
export MECH_COLLECTION_WORKSPACE=/path/to/repo
export MECH_COLLECTION_ROOT=/path/to/output/combustion_and_flame_mechanisms
export MECH_COLLECTION_PYTHON=/path/to/python
```

On PowerShell:

```powershell
$env:MECH_COLLECTION_WORKSPACE = "D:\work\Combustion-chemical-kinetic-models"
$env:MECH_COLLECTION_ROOT = "D:\work\combustion_and_flame_mechanisms"
$env:MECH_COLLECTION_PYTHON = "C:\Users\you\miniconda3\envs\mechanism-collection\python.exe"
```

`MECH_COLLECTION_PYTHON` matters because Cantera conversion is executed in a subprocess. If it is unset, the current Python interpreter is used.

## 5. Resume State

Per-article state is stored in `combustion_and_flame_mechanisms/_raw/article_metadata.json`.

Important fields:

- `supplementProbeStatus`: `complete`, `no_links`, `captcha`, `error`, or `partial`.
- `supplementProbeCheckedAt`: last supplement-link probe time.
- `supplementDownloadStatus`: `complete`, `partial`, `failed`, or `none`.
- `downloadStatus`: per-link status such as `downloaded`, `existing`, or `failed`.
- `processingStatus`: `included`, `conversion_failed`, `excluded_no_mechanism_attachment`, `excluded_no_supplement_found`, `excluded_no_mechanism_signal`, etc.
- `processedAt`: last real processing time.
- `processingFolder`: output folder for that article.

Default behavior:

- `probe-supplements` skips records with a terminal `supplementProbeStatus`.
- `download-supplements` skips already complete, failed, or partial records.
- `process` reuses existing terminal `processingStatus` and existing output folders.
- Use `--force` only when you intentionally want to rerun that step.

## 6. Human Work vs Agent Work

Human-only or human-supervised work:

- Log in to ScienceDirect or institutional SSO.
- Complete CAPTCHA or robot verification.
- Confirm license/access prompts.
- Manually download attachments or PDFs when automated direct links fail.
- Decide whether a failed conversion should be manually corrected.
- Review ambiguous fuel classification or unclear abstract evidence.

Work that a Python script can do without an agent:

- Import JSON metadata.
- Probe predictable Elsevier `mmc` links.
- Download already recorded direct supplement URLs.
- Extract archives and nested archives.
- Detect mechanism, thermo, and transport files.
- Run Cantera conversion and write summaries.
- Maintain index, handoff, and resume state.

Work that an agent can help automate, if available:

- Open ScienceDirect issue pages and collect article metadata into JSON.
- Open article pages and collect supplementary-material links into JSON.
- Pause when CAPTCHA or SSO appears, then continue after the user completes it.
- Inspect failed conversions and adjust parser-cleanup rules.
- Run quality checks, commit, and push.

If no agent is available, replace those browser-automation steps with manual browser work and save the same JSON files described below.

## 7. Metadata From ScienceDirect Issues

For each year, collect ScienceDirect issue-page metadata into files like:

```text
combustion_and_flame_mechanisms/_raw/2025_volumes/volume_*.json
```

Each article record should contain as many of these fields as possible:

```json
{
  "year": "2025",
  "volume": "280",
  "month": "June 2025",
  "title": "Article title",
  "authors": ["First Author", "Second Author"],
  "doi": "10.1016/j.combustflame....",
  "pii": "S00102180...",
  "articleNumber": "114000",
  "url": "https://www.sciencedirect.com/science/article/pii/S00102180...",
  "issuePdfLink": "https://www.sciencedirect.com/science/article/pii/.../pdfft"
}
```

Import the metadata:

```bash
python scripts/collect_cf2026.py import-sciencedirect-metadata --year 2025 --source-dir combustion_and_flame_mechanisms/_raw/2025_volumes
```

Run local candidate screening and processing:

```bash
python scripts/collect_cf2026.py process
```

## 8. Supplement Link Discovery And Download

First try predictable Elsevier `mmc` supplement links:

```bash
python scripts/collect_cf2026.py probe-supplements --year 2025 --max-mmc 12
python scripts/collect_cf2026.py download-supplements --year 2025
python scripts/collect_cf2026.py process
```

If the network, login, or CDN state has changed and you intentionally need to retry:

```bash
python scripts/collect_cf2026.py probe-supplements --year 2025 --max-mmc 12 --force
python scripts/collect_cf2026.py download-supplements --year 2025 --force
```

Do not use `--force` as a normal habit. It is for deliberate retry or reprocessing.

## 9. Article-Page Supplement Links

Some supplements cannot be found by predictable `mmc` probing. In that case, open the ScienceDirect article page in a logged-in browser and collect supplementary-material links into:

```text
combustion_and_flame_mechanisms/_raw/2025_supplement_links/chunk_*.json
```

The JSON format is:

```json
{
  "pii": "S0010218025000000",
  "url": "https://www.sciencedirect.com/science/article/pii/S0010218025000000",
  "captcha": false,
  "links": [
    {
      "href": "https://ars.els-cdn.com/content/image/1-s2.0-S0010218025000000-mmc1.zip",
      "text": "Supplementary material"
    }
  ]
}
```

If the page shows CAPTCHA or SSO instead of the article:

```json
{
  "pii": "S0010218025000000",
  "url": "https://www.sciencedirect.com/science/article/pii/S0010218025000000",
  "captcha": true,
  "links": []
}
```

Import page-harvested links:

```bash
python scripts/collect_cf2026.py import-page-supplements --source-dir combustion_and_flame_mechanisms/_raw/2025_supplement_links
python scripts/collect_cf2026.py download-supplements --year 2025
python scripts/collect_cf2026.py process
```

## 10. Manual Downloads

When direct download fails, use `manual_download_handoff.md` to continue manually. For each item:

1. Open the DOI or ScienceDirect URL in a logged-in browser.
2. Download the PDF and supplementary files if access is available.
3. Put files into `combustion_and_flame_mechanisms/_raw/downloads/`.
4. Use a filename containing one of DOI-normalized text, PII, or article number. PII-based names are best, for example `S0010218025000000_mmc1.zip`.
5. Run:

```bash
python scripts/collect_cf2026.py process
```

The script matches downloads by DOI, PII, or article number, then copies them into the paper's `_processing/raw_downloads/` folder.

## 11. Abstracts

Summaries should include abstracts. The script tries local PDFs first, then Crossref, OpenAlex, and Semantic Scholar:

```bash
python scripts/collect_cf2026.py enrich-abstracts
python scripts/collect_cf2026.py process
```

Use title/abstract evidence for fuel type and validation reactor type. If the abstract does not make the reactor type clear, write `not clear from abstract` instead of guessing from the full paper.

## 12. Quality Checks

Run tests after changing code or processing rules:

```bash
python -m unittest discover -s tests
```

Check current status counts:

```bash
python - <<'PY'
import csv
from collections import Counter
with open('combustion_and_flame_mechanisms/collection_index.csv', encoding='utf-8-sig', newline='') as f:
    print(Counter(row['status'] for row in csv.DictReader(f)))
PY
```

Check duplicate DOI values:

```bash
python - <<'PY'
import csv
from collections import Counter
with open('combustion_and_flame_mechanisms/collection_index.csv', encoding='utf-8-sig', newline='') as f:
    dois = [row['doi'].strip().lower() for row in csv.DictReader(f) if row.get('doi')]
for doi, count in Counter(dois).items():
    if count > 1:
        print(count, doi)
PY
```

Inspect `manual_download_handoff.md` for articles still blocked by access, CAPTCHA, missing supplements, or conversion failures.

## 13. Git Hygiene

Before committing, make sure you do not stage payload files such as PDFs, archives, raw downloads, `_processing/`, `chem.inp`, `therm.dat`, `tran.dat`, or generated YAML/log files.

Safe files to commit usually include:

- `scripts/`
- `tests/`
- `docs/`
- `README.md`
- `environment.yml`
- `combustion_and_flame_mechanisms/README.md`
- `combustion_and_flame_mechanisms/collection_index.csv`
- `combustion_and_flame_mechanisms/manual_download_handoff.md`
- `combustion_and_flame_mechanisms/run_summary.json`
- `combustion_and_flame_mechanisms/_raw/article_metadata.json`

Example:

```bash
git status --short
git add scripts tests docs README.md environment.yml combustion_and_flame_mechanisms/README.md combustion_and_flame_mechanisms/collection_index.csv combustion_and_flame_mechanisms/manual_download_handoff.md combustion_and_flame_mechanisms/run_summary.json combustion_and_flame_mechanisms/_raw/article_metadata.json
git diff --cached --name-only
```

If staged files include `.pdf`, `.zip`, `.rar`, `.7z`, `.inp`, `.dat`, `.yaml`, `_processing`, or `_raw/downloads`, unstage those files before committing.

## 14. Typical Continuation Cases

Add a new year:

```bash
python scripts/collect_cf2026.py import-sciencedirect-metadata --year 2024 --source-dir combustion_and_flame_mechanisms/_raw/2024_volumes
python scripts/collect_cf2026.py process
python scripts/collect_cf2026.py probe-supplements --year 2024 --max-mmc 12
python scripts/collect_cf2026.py download-supplements --year 2024
python scripts/collect_cf2026.py process
```

Continue after CAPTCHA:

1. Complete CAPTCHA or SSO in the browser.
2. Continue article-page link harvesting from the first unfinished item.
3. Save the next `chunk_*.json`.
4. Import links and run downloads again.

Retry failed downloads:

```bash
python scripts/collect_cf2026.py download-supplements --year 2025 --force
```

Rerun after changing fuel detection or Cantera cleanup logic:

```bash
python scripts/collect_cf2026.py process --force
```

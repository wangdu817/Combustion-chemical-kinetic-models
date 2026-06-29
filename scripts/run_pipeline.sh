#!/bin/bash
# Per-year full mechanism collection pipeline (with fuel classification)
# Usage: bash scripts/run_pipeline.sh <YEAR>
set -euo pipefail

REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

YEAR="${1:?Usage: $0 <YEAR>}"
LOG="${YEAR}_pipeline.log"
PYTHON=".venv/bin/python"
export CONDA_PREFIX="/home/icaurs/miniconda3"

rm -f "$LOG"
echo "=== ${YEAR} pipeline at $(date) ===" | tee -a "$LOG"

# Step 1: Detect candidates + init folders
echo "=== STEP1: detect candidates ===" | tee -a "$LOG"
$PYTHON scripts/collect_cf2026.py process --force --year "$YEAR" 2>> "$LOG" | tee -a "$LOG"
echo "STEP1 done" | tee -a "$LOG"

# Step 2: Probe supplements
echo "=== STEP2: probe ===" | tee -a "$LOG"
$PYTHON scripts/collect_cf2026.py probe-supplements --year "$YEAR" --max-mmc 12 2>> "$LOG" | tee -a "$LOG"
echo "STEP2 done" | tee -a "$LOG"

# Step 3: Download supplements
echo "=== STEP3: download ===" | tee -a "$LOG"
$PYTHON scripts/collect_cf2026.py download-supplements --year "$YEAR" 2>> "$LOG" | tee -a "$LOG"
echo "STEP3 done" | tee -a "$LOG"

# Step 4: Extract mechanisms
echo "=== STEP4: extract ===" | tee -a "$LOG"
$PYTHON scripts/collect_cf2026.py process --force --year "$YEAR" 2>> "$LOG" | tee -a "$LOG"
echo "STEP4 done" | tee -a "$LOG"

# Step 5: Enrich abstracts
echo "=== STEP5: abstracts ===" | tee -a "$LOG"
$PYTHON scripts/enrich_abstracts.py 2>> "$LOG" | tee -a "$LOG"
echo "STEP5 done" | tee -a "$LOG"

# Step 6: Final update (write abstracts into summaries)
echo "=== STEP6: final ===" | tee -a "$LOG"
$PYTHON scripts/collect_cf2026.py process --force --year "$YEAR" 2>> "$LOG" | tee -a "$LOG"
echo "STEP6 done" | tee -a "$LOG"

# Step 7: Reclassify fuel types
echo "=== STEP7: reclassify fuel ===" | tee -a "$LOG"
$PYTHON scripts/reclassify_fuel.py "$YEAR" 2>> "$LOG" | tee -a "$LOG"
echo "STEP7 done" | tee -a "$LOG"

# Step 8: Stats
echo "=== STEP8: stats ===" | tee -a "$LOG"
$PYTHON -c "
import json; from pathlib import Path
m=json.loads(Path('combustion_and_flame_mechanisms/_raw/article_metadata.json').read_text('utf-8'))
inc=cf=0
for r in m:
    if str(r.get('year',''))!='${YEAR}': continue
    if r.get('processingStatus')=='included': inc+=1
    if r.get('processingStatus')=='conversion_failed': cf+=1
s=len(list(Path('combustion_and_flame_mechanisms').glob('*/${YEAR}/*/mechanism_summary.md')))
print(f'${YEAR}: {s} summaries, inc={inc}, fail={cf}')
" 2>> "$LOG" | tee -a "$LOG"

# Push
bash scripts/safe_push.sh "${YEAR} mechanism collection" 2>> "$LOG" | tee -a "$LOG"
echo "=== DONE $(date) ===" | tee -a "$LOG"

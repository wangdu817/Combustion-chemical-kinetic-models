#!/bin/bash
# One-shot: collect 2026 mechanisms and PDFs for 2015
cd /home/ubuntu/Combustion-chemical-kinetic-models
export MECH_COLLECTION_WORKSPACE=/home/ubuntu/Combustion-chemical-kinetic-models
export MECH_COLLECTION_ROOT=/home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms
export MECH_COLLECTION_PYTHON=/home/ubuntu/Combustion-chemical-kinetic-models/.venv/bin/python

echo "=== $(date): Starting 2026 collection ==="
.venv/bin/python scripts/collect_cf2026.py probe-supplements --year 2026 --max-mmc 12 --serial
echo "PROBE=$?"
.venv/bin/python scripts/collect_cf2026.py download-supplements --year 2026
echo "DL=$?"
.venv/bin/python scripts/collect_cf2026.py process --force
echo "PROCESS=$?"
.venv/bin/python scripts/enrich_abstracts.py
echo "ENRICH=$?"
.venv/bin/python scripts/collect_cf2026.py process --force
echo "FINAL=$?"

echo "=== $(date): 2015 PDF download ==="
.venv/bin/python scripts/scihub_dl.py
echo "PDF=$?"

echo "=== $(date): ALL DONE ==="
# Remove this one-shot from crontab
crontab -l | grep -v "run_2026_pipeline.sh" | crontab -

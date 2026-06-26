#!/bin/bash
# Safe add: only mechanism files, summaries, yaml, and PDFs
# Respects .gitignore which already excludes _raw/downloads and _processing/
cd "$(dirname "$0")/.."

git add \
  'combustion_and_flame_mechanisms/**/mechanism_summary.md' \
  'combustion_and_flame_mechanisms/**/chem.inp' \
  'combustion_and_flame_mechanisms/**/therm.dat' \
  'combustion_and_flame_mechanisms/**/tran.dat' \
  'combustion_and_flame_mechanisms/**/mechanism.yaml' \
  'combustion_and_flame_mechanisms/**/*.pdf' \
  'combustion_and_flame_mechanisms/_raw/article_metadata.json' \
  'combustion_and_flame_mechanisms/collection_index.csv' \
  'combustion_and_flame_mechanisms/run_summary.json' \
  'combustion_and_flame_mechanisms/manual_download_handoff.md' \
  'scripts/' \
  2>/dev/null

git commit -m "$1" 2>/dev/null
git push origin master 2>&1
echo "PUSH done"

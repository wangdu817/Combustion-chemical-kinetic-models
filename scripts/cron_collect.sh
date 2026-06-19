#!/bin/bash
# Cron helper: run yearly_collect.py for the next pending year
set -e
cd /home/ubuntu/Combustion-chemical-kinetic-models
export MECH_COLLECTION_WORKSPACE="$(pwd)"
export MECH_COLLECTION_ROOT="$(pwd)/combustion_and_flame_mechanisms"
export MECH_COLLECTION_PYTHON="$(pwd)/.venv/bin/python"

STATE="$(pwd)/.collection_state"
rm -f /tmp/collect.lock

# Lock to prevent overlap
exec 200>/tmp/collect.lock
flock -n 200 || { echo "Another collection is running"; exit 0; }

# Init state
[[ -f "$STATE" ]] || echo "2019" > "$STATE"
NEXT=$(cat "$STATE")
if [[ "$NEXT" -lt 2006 ]]; then
    echo "All years 2006-2019 completed."
    exit 0
fi

echo "=== Starting collection of year $NEXT ==="
"$MECH_COLLECTION_PYTHON" scripts/yearly_collect.py "$NEXT"
RC=$?

if [[ $RC -eq 0 ]]; then
    echo $((NEXT - 1)) > "$STATE"
    echo "Done. Next: $((NEXT - 1))"
    # Cleanup downloads after collection
    "$MECH_COLLECTION_PYTHON" -c "
import json; from pathlib import Path
m=json.loads(Path('combustion_and_flame_mechanisms/_raw/article_metadata.json').read_text('utf-8'))
mech_piis={r.get('pii','') for r in m if r.get('processingStatus') in ('included','conversion_failed')}
dl=Path('combustion_and_flame_mechanisms/_raw/downloads')
k=d=0
for f in dl.iterdir():
    if any(f.name.startswith(p) for p in mech_piis): k+=1
    else: f.unlink(); d+=1
print(f'Downloads: {k} kept, {d} deleted')
"
else
    echo "Failed with exit code $RC"
    exit $RC
fi

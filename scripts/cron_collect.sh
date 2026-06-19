#!/bin/bash
# Cron helper: collect mechanisms for pending years 2006-2019.
# Before advancing to the next year, verifies the current year is complete
# (mechanisms extracted, abstracts fetched). If incomplete, re-processes it.
set -e
cd /home/ubuntu/Combustion-chemical-kinetic-models
export MECH_COLLECTION_WORKSPACE="$(pwd)"
export MECH_COLLECTION_ROOT="$(pwd)/combustion_and_flame_mechanisms"
export MECH_COLLECTION_PYTHON="$(pwd)/.venv/bin/python"

STATE="$(pwd)/.collection_state"

# Lock to prevent overlap
exec 200>/tmp/collect.lock
flock -n 200 || { echo "Another collection is running"; exit 0; }

# Init state
[[ -f "$STATE" ]] || echo "2019" > "$STATE"
CURRENT=$(cat "$STATE")

if [[ "$CURRENT" -lt 2006 ]]; then
    echo "All years 2006-2019 completed."
    exit 0
fi

echo "=== Current target year: $CURRENT ==="

# Check if $CURRENT is complete
"$MECH_COLLECTION_PYTHON" -c "
import json; from pathlib import Path; import sys
meta = json.loads(Path('combustion_and_flame_mechanisms/_raw/article_metadata.json').read_text('utf-8'))

candidates = 0
pending = 0
has_mechanism = False

for r in meta:
    if r.get('year') != '$CURRENT':
        continue
    if r.get('candidate'):
        candidates += 1
        status = r.get('processingStatus', 'NOT_PROCESSED')
        if status in ('included', 'conversion_failed'):
            has_mechanism = True
        if status == 'NOT_PROCESSED' or (not r.get('candidate')):
            continue
        # Articles with downloads but not yet processed
        if status not in ('included', 'conversion_failed',
                          'excluded_no_mechanism_attachment',
                          'excluded_no_supplement_found',
                          'excluded_no_mechanism_signal'):
            pending += 1

# Also check for articles that need abstract enrichment
need_abstract = sum(1 for r in meta
    if r.get('year') == '$CURRENT'
    and r.get('processingStatus') in ('included', 'conversion_failed')
    and not r.get('abstract', '').strip())

complete = has_mechanism and pending == 0 and need_abstract == 0
print(f'Year=$CURRENT candidates={candidates} mechanism={has_mechanism} pending={pending} missing_abstracts={need_abstract} complete={complete}')
sys.exit(0 if complete else 1)
"

if [[ $? -eq 0 ]]; then
    echo "Year $CURRENT is complete. Moving to next."
    echo $((CURRENT - 1)) > "$STATE"
    NEXT=$((CURRENT - 1))
    echo "=== Starting collection of year $NEXT ==="
else
    NEXT=$CURRENT
    echo "Year $CURRENT is incomplete (pending or missing abstracts). Re-running."
    echo "=== Re-processing year $NEXT ==="
fi

# Run collection for this year
"$MECH_COLLECTION_PYTHON" scripts/yearly_collect.py "$NEXT"
RC=$?

if [[ $RC -eq 0 ]]; then
    echo "Collection of $NEXT finished successfully."
    
    # Check again: if still incomplete, keep same year for next run
    "$MECH_COLLECTION_PYTHON" -c "
import json; from pathlib import Path; import sys
meta = json.loads(Path('combustion_and_flame_mechanisms/_raw/article_metadata.json').read_text('utf-8'))
has_mech = False; pending = 0
for r in meta:
    if r.get('year') != '$NEXT': continue
    if r.get('processingStatus') in ('included','conversion_failed'): has_mech = True
need_ab = sum(1 for r in meta
    if r.get('year')=='$NEXT' and r.get('processingStatus') in ('included','conversion_failed')
    and not r.get('abstract','').strip())
complete = has_mech and need_ab == 0
if complete:
    print('$NEXT is now complete. Will advance next run.')
else:
    print('$NEXT still incomplete. Keeping as current target.')
    with open('$STATE','w') as f: f.write('$NEXT\n')
"

    # Cleanup non-mechanism downloads
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
    echo "Collection of $NEXT failed with exit code $RC."
    echo "$NEXT" > "$STATE"
    exit $RC
fi

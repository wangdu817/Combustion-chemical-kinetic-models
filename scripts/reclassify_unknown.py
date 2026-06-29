#!/usr/bin/env python3
"""Reclassify unknown_fuel folders — handles both summary-based (PII) and empty (articleNumber) dirs."""
import json, shutil, sys, re
from pathlib import Path

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import detect_fuel, slugify, read_metadata, write_metadata, first_author_surname

ROOT = REPO / 'combustion_and_flame_mechanisms'
records = read_metadata()
pii_map = {r.get('pii',''): r for r in records if r.get('pii')}
artnum_map = {}
for r in records:
    an = str(r.get('articleNumber','')).strip()
    if an:
        artnum_map[an] = r

moved = 0
unknown = 0

# Phase 1: folders with mechanism_summary.md → extract PII from content
for summary in sorted(ROOT.glob('unknown_fuel/*/*/mechanism_summary.md')):
    folder = summary.parent
    year = folder.parent.name
    
    content = summary.read_text()
    pii_match = re.search(r'S00102180\d+X?|S15407489\d+X?', content)
    if pii_match:
        r = pii_map.get(pii_match.group(0))
    else:
        r = None
    
    if not r:
        unknown += 1
        continue
    
    new_fuel = detect_fuel(r)
    if new_fuel == 'unknown_fuel':
        unknown += 1
        continue
    
    authors = r.get('authors',['unknown'])
    fa = str(authors[0]) if isinstance(authors,list) and authors else str(authors)
    au = first_author_surname(fa)
    aid = str(r.get('articleNumber','')) or r.get('pii','')[-8:]
    new_name = f'{slugify(au,24)}_{year}_{slugify(new_fuel,60)}_{aid}'
    new_folder = ROOT / new_fuel / year / new_name
    
    if new_folder == folder:
        r['fuelType'] = new_fuel
        continue
    
    new_folder.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.move(str(folder), str(new_folder))
        r['fuelType'] = new_fuel
        moved += 1
        if moved <= 5 or moved % 20 == 0:
            print(f'  [PII] {moved}: {new_fuel}/{year}')
    except Exception as e:
        print(f'  ERR: {e}')
        unknown += 1

# Phase 2: empty folders (no summary) → match by articleNumber from folder name
for folder in sorted(ROOT.glob('unknown_fuel/*/*')):
    if (folder / 'mechanism_summary.md').exists():
        continue  # already handled above
    
    year = folder.parent.name
    parts = folder.name.split('_')
    # Extract article number — page range or numeric ID
    an = None
    for part in reversed(parts):
        if re.match(r'^\d+-\d+$', part):  # page range: 505-521
            an = part
            break
        elif part.isdigit():
            an = part
            break
        elif len(part) >= 5 and re.match(r'^\d+', part):
            an = part
            break
    
    if not an:
        unknown += 1
        continue
    
    r = artnum_map.get(an)
    if not r:
        unknown += 1
        continue
    
    new_fuel = detect_fuel(r)
    if new_fuel == 'unknown_fuel':
        unknown += 1
        continue
    
    authors = r.get('authors',['unknown'])
    fa = str(authors[0]) if isinstance(authors,list) and authors else str(authors)
    au = first_author_surname(fa)
    aid = an
    new_name = f'{slugify(au,24)}_{year}_{slugify(new_fuel,60)}_{aid}'
    new_folder = ROOT / new_fuel / year / new_name
    
    if new_folder == folder:
        r['fuelType'] = new_fuel
        continue
    
    new_folder.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.move(str(folder), str(new_folder))
        r['fuelType'] = new_fuel
        moved += 1
        if moved <= 5 or moved % 20 == 0:
            print(f'  [AN]  {moved}: {new_fuel}/{year}')
    except Exception as e:
        print(f'  ERR: {e}')
        unknown += 1

write_metadata(records)

# Clean up empty directories
for fuel_dir in sorted(ROOT.iterdir()):
    if not fuel_dir.is_dir() or fuel_dir.name.startswith('_') or fuel_dir.name.startswith('.'):
        continue
    for year_dir in sorted(fuel_dir.iterdir()):
        if year_dir.is_dir() and not any(year_dir.iterdir()):
            year_dir.rmdir()
    # Remove fuel dir if empty (all years cleaned)
    if not any(fuel_dir.iterdir()):
        fuel_dir.rmdir()
        if moved <= 5 or fuel_dir.name == 'unknown_fuel':
            print(f'  Cleaned: {fuel_dir.name}/')

print(f'\nDone: {moved} moved, {unknown} still unknown')

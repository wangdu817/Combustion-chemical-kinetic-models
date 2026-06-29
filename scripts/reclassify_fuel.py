#!/usr/bin/env python3
"""Post-pipeline fuel reclassification for a specific year.

After process --force --year completes and abstracts are enriched,
re-run detect_fuel() on all records for that year, then move any
unknown_fuel folders to their detected fuel directories.

Run: .venv/bin/python scripts/reclassify_fuel.py <YEAR>
"""
import sys, re, shutil
from pathlib import Path

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import (
    detect_fuel, slugify, read_metadata, write_metadata,
    first_author_surname, article_id
)

ROOT = REPO / 'combustion_and_flame_mechanisms'

def main():
    year = sys.argv[1] if len(sys.argv) > 1 else None
    records = read_metadata()

    # Build lookup maps
    pii_map = {r.get('pii',''): r for r in records if r.get('pii')}
    artnum_map = {}
    for r in records:
        an = str(r.get('articleNumber','')).strip()
        if an:
            artnum_map[an] = r

    # Step 1: Re-detect fuel for all records in target year
    redetected = 0
    for r in records:
        if year and str(r.get('year','')) != year:
            continue
        if r.get('processingStatus') not in ('included', 'conversion_failed'):
            continue
        old = r.get('fuelType', 'unknown_fuel')
        new = detect_fuel(r)
        if old != new:
            r['fuelType'] = new
            redetected += 1
    print(f'Re-detected fuel: {redetected} records')

    # Step 2: Reclassify unknown_fuel folders that now have known fuel
    moved_pii = 0
    moved_an = 0

    # Phase 2a: folders with summaries → match by PII in content
    for summary in sorted(ROOT.glob('unknown_fuel/*/*/mechanism_summary.md')):
        folder = summary.parent
        fy = folder.parent.name
        if year and fy != year:
            continue

        content = summary.read_text()
        m = re.search(r'S00102180\d+X?|S15407489\d+X?', content)
        r = m and pii_map.get(m.group(0))
        if not r or r.get('fuelType') == 'unknown_fuel':
            continue

        _move_folder(folder, r, fy)
        moved_pii += 1

    # Phase 2b: folders without summaries → match by articleNumber
    for folder in sorted(ROOT.glob('unknown_fuel/*/*')):
        if (folder / 'mechanism_summary.md').exists():
            continue
        fy = folder.parent.name
        if year and fy != year:
            continue

        # Extract article number from folder name
        parts = folder.name.split('_')
        an = None
        for part in reversed(parts):
            if re.match(r'^\d+-\d+$', part):
                an = part; break
            elif part.isdigit():
                an = part; break
        if not an:
            continue

        r = artnum_map.get(an)
        if not r or r.get('fuelType') == 'unknown_fuel':
            continue

        _move_folder(folder, r, fy)
        moved_an += 1

    write_metadata(records)
    print(f'Moved: {moved_pii} (PII) + {moved_an} (articleNumber) = {moved_pii + moved_an}')
    print(f'Remaining unknown_fuel for {year or "all years"}: {_count_unknown(year)}')

    # Step 3: Clean up empty dirs
    _cleanup_empty_dirs()
    # Step 4: Build year-fuel index
    _build_year_fuel_index(year)


def _classify_element(fuel_type):
    """Classify fuel type into element category."""
    import re
    ft = fuel_type.lower()
    N = [r'ammonia','nitric','n2o','nitro','amine','pyridine','pyrrole','nitrogen','ammonium','nitrite','nitrate','rdx','hmx','cl20','isocyanate','nitrile','cyan']
    M = [r'aluminum','aluminium','iron','magnesium','silane','potassium','sodium','copper','zinc','titanium','metal']
    F = [r'fluorine','fluoride','hfo','hcfc','hfc','r32','r1234','halon']
    O = [r'methanol','ethanol','propanol','butanol','pentanol','hexanol','octanol',
         r'ether','ester','aldehyde','ketone','acetone','furan','formate','acetate',
         r'carbonate','alcohol','dme\b','phenol','peroxide','oxygenat','biofuel',
         r'formic','dtbp','nitrite','ehn','levulinate']
    if any(re.search(p, ft) for p in N): return 'nitrogen'
    if any(re.search(p, ft) for p in M): return 'metal'
    if any(re.search(p, ft) for p in F): return 'fluorine'
    if any(re.search(p, ft) for p in O): return 'oxygenated'
    return 'hydrocarbon'

def _move_folder(folder, record, year):
    fuel = record.get('fuelType', 'unknown_fuel')
    element = _classify_element(fuel)
    authors = record.get('authors', ['unknown'])
    fa = str(authors[0]) if isinstance(authors, list) and authors else str(authors)
    au = first_author_surname(fa)
    aid = article_id(record)
    new_name = f'{slugify(au, 24)}_{year}_{slugify(fuel, 60)}_{aid}'
    new_folder = ROOT / element / fuel / year / new_name

    if new_folder == folder:
        return  # already correct

    new_folder.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(folder), str(new_folder))


def _count_unknown(year):
    n = 0
    for d in ROOT.glob('unknown_fuel/*/*'):
        fy = d.parent.name
        if year and fy != year:
            continue
        if d.is_dir():
            n += 1
    return n


def _cleanup_empty_dirs():
    """Remove empty year dirs and empty fuel dirs."""
    for fuel_dir in sorted(ROOT.iterdir()):
        if not fuel_dir.is_dir():
            continue
        if fuel_dir.name.startswith('_') or fuel_dir.name.startswith('.'):
            continue
        for year_dir in sorted(fuel_dir.iterdir()):
            if year_dir.is_dir() and not any(year_dir.iterdir()):
                year_dir.rmdir()
        if not any(fuel_dir.iterdir()):
            fuel_dir.rmdir()


def _build_year_fuel_index(year=None):
    """Build year_fuel_index.json: {year: {fuel: count}}"""
    records = read_metadata()

    # Count from metadata for mechanism records only
    index = {}
    for r in records:
        y = str(r.get('year', ''))
        if not y or (year and y != year):
            continue
        st = r.get('processingStatus', '')
        if st not in ('included', 'conversion_failed'):
            continue
        fuel = r.get('fuelType', 'unknown_fuel')
        if y not in index:
            index[y] = {}
        index[y][fuel] = index[y].get(fuel, 0) + 1

    # Sort by year, then by fuel count descending
    from collections import OrderedDict
    sorted_index = OrderedDict()
    for y in sorted(index.keys()):
        fuels = index[y]
        sorted_index[y] = dict(sorted(fuels.items(), key=lambda x: -x[1]))

    # Write
    import json
    idx_path = ROOT.parent / 'year_fuel_index.json'
    idx_path.write_text(json.dumps(sorted_index, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Index written: {idx_path} ({len(sorted_index)} years)')


if __name__ == '__main__':
    main()

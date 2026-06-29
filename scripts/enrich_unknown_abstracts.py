#!/usr/bin/env python3
"""Enrich abstracts for unknown_fuel records that have mechanism files (chem.inp)."""
import sys, re, time
from pathlib import Path

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import (
    read_metadata, write_metadata, detect_fuel, 
    fetch_crossref_abstract, fetch_openalex_abstract, 
    fetch_semantic_scholar_abstract, extract_abstract_from_pdf,
    normalize_abstract, normalize_doi, find_local_pdf, record_folder
)

ROOT = REPO / 'combustion_and_flame_mechanisms'
records = read_metadata()
pii_map = {r.get('pii',''): r for r in records if r.get('pii')}

# Find all folders with chem.inp under unknown_fuel
mech_folders = {chem.parent for chem in ROOT.glob('unknown_fuel/*/*/chem.inp')}
print(f'Mechanism folders to process: {len(mech_folders)}')

# Build lookup: folder -> record
folder_records = {}
for folder in mech_folders:
    r = None
    summary = folder / 'mechanism_summary.md'
    if summary.exists():
        m = re.search(r'S00102180\d+X?|S15407489\d+X?', summary.read_text())
        if m:
            r = pii_map.get(m.group(0))
    if not r:
        parts = folder.name.split('_')
        for part in reversed(parts):
            if re.match(r'^\d+-\d+$', part) or part.isdigit():
                for rec in records:
                    if str(rec.get('articleNumber','')) == part:
                        r = rec
                        break
                break
    if r:
        folder_records[str(folder)] = r

print(f'Matched to metadata: {len(folder_records)}')

enriched = 0
for folder_str, record in folder_records.items():
    existing = normalize_abstract(record.get('abstract', ''))
    if existing:
        continue
    
    doi = normalize_doi(record.get('doi', ''))
    if not doi:
        continue
    
    folder = Path(folder_str)
    local_pdf = find_local_pdf(folder)
    
    sources = [
        ('local_pdf', lambda: extract_abstract_from_pdf(local_pdf) if local_pdf else ''),
        ('crossref', lambda: fetch_crossref_abstract(doi)),
        ('openalex', lambda: fetch_openalex_abstract(doi)),
        ('semantic_scholar', lambda: fetch_semantic_scholar_abstract(doi)),
    ]
    
    for source, getter in sources:
        abstract = getter()
        if abstract:
            record['abstract'] = abstract
            record['abstractSource'] = source
            enriched += 1
            print(f'  [{enriched}] {source:15s} {folder.name[:50]}')
            break
    
    if not record.get('abstract'):
        record['abstractStatus'] = 'not available'
    
    # Write after each record so progress survives interruption
    write_metadata(records)
    time.sleep(0.15)  # rate limit

print(f'\nEnriched: {enriched}/{len(folder_records)}')
write_metadata(records)

# Re-check: how many are now classifiable?
reclassifiable = 0
for record in records:
    if record.get('fuelType') == 'unknown_fuel' and detect_fuel(record) != 'unknown_fuel':
        reclassifiable += 1

print(f'Now reclassifiable (fuelType=unknown_fuel -> known): {reclassifiable}')

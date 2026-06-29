#!/usr/bin/env python3
"""Build comprehensive candidate index: candidates, mechanisms, storage paths."""
import json, sys
from pathlib import Path
from collections import defaultdict

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import read_metadata, article_id, record_folder

ROOT = REPO / 'combustion_and_flame_mechanisms'
records = read_metadata()

# Element classification
def classify_element(fuel_type):
    N = ['ammonia','nitric_oxide','n2o','nitromethane','methylamine','pyridine','pyrrole',
         'ammonium','nitrocellulose','methyl_isocyanate','rdx','cl20','nitrogen','nitrite','nitrate','amine','nitro','nitrile','cyan','isocyanate']
    M = ['aluminum','aluminium','iron','magnesium','silane','potassium','sodium','copper','zinc','titanium','metal']
    F = ['fluorine','fluoride','hfo','hcfc','hfc','r32','r1234','ch2f2','difluoromethane','trifluoromethane']
    O = ['methanol','ethanol','propanol','butanol','pentanol','ether','dme','etbe','mtbe',
         'dimethoxymethane','formate','acetate','carbonate','butanoate','ester','biodiesel',
         'acetone','butanone','ketone','aldehyde','formaldehyde','acetaldehyde','benzaldehyde',
         'furan','thf','formic_acid','dtbp','peroxide','polyoxymethylene',
         'oxygenated','oxygenate','biofuel','nitrite','nitrate','ehn']
    ft = fuel_type.lower()
    import re
    if any(re.search(r'\b'+p+r'\b', ft) for p in N): return 'nitrogen'
    if any(re.search(r'\b'+p+r'\b', ft) for p in M): return 'metal'
    if any(re.search(r'\b'+p+r'\b', ft) for p in F): return 'fluorine'
    if any(re.search(r'\b'+p+r'\b', ft) for p in O): return 'oxygenated'
    return 'hydrocarbon'

index = []
by_year = defaultdict(lambda: {'candidates': 0, 'mechanisms': 0, 'no_supplement': 0, 'no_mech_attachment': 0})

for r in records:
    y = str(r.get('year', '?'))
    if not r.get('candidate'):
        continue
    
    aid = article_id(r)
    st = r.get('processingStatus', '')
    fuel = r.get('fuelType', 'unknown_fuel')
    folder = record_folder(r)
    
    # Check what's on disk
    disk = {
        'exists': folder.exists(),
        'chem_inp': (folder / 'chem.inp').exists(),
        'therm_dat': (folder / 'therm.dat').exists(),
        'tran_dat': (folder / 'tran.dat').exists(),
        'mechanism_yaml': (folder / 'mechanism.yaml').exists(),
        'summary': (folder / 'mechanism_summary.md').exists(),
        'pdf': any(folder.glob('*.pdf')),
    }
    
    entry = {
        'year': y,
        'pii': r.get('pii', ''),
        'doi': r.get('doi', ''),
        'title': str(r.get('title', ''))[:200],
        'authors': str(r.get('authors', ['?'])[0]) if isinstance(r.get('authors'), list) else str(r.get('authors', '?')),
        'candidate': True,
        'status': st,
        'fuel_type': fuel,
        'element': classify_element(fuel),
        'storage_path': str(folder.relative_to(ROOT)) if folder.exists() else None,
        'on_disk': disk,
    }
    index.append(entry)
    
    # Stats
    by_year[y]['candidates'] += 1
    if st in ('included', 'conversion_failed'):
        by_year[y]['mechanisms'] += 1
    if st == 'excluded_no_supplement_found':
        by_year[y]['no_supplement'] += 1
    if st == 'excluded_no_mechanism_attachment':
        by_year[y]['no_mech_attachment'] += 1

# Write index
out_path = REPO / 'candidate_index.json'
out_path.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding='utf-8')

# Summary
hdr = f"{'Year':<6} {'Cand':>5} {'Mech':>5} {'NoSupp':>7} {'NoAttach':>9} {'Gap':>5}"
print(f'Index: {len(index)} candidates written to {out_path}')
print()
print(hdr)
for y in sorted(by_year.keys()):
    d = by_year[y]
    gap = d['candidates'] - d['mechanisms'] - d['no_supplement'] - d['no_mech_attachment']
    print('{:<6} {:>5} {:>5} {:>7} {:>9} {:>5}'.format(y, d['candidates'], d['mechanisms'], d['no_supplement'], d['no_mech_attachment'], gap))

total = {k: sum(d[k] for d in by_year.values()) for k in ['candidates','mechanisms','no_supplement','no_mech_attachment']}
print('{:<6} {:>5} {:>5} {:>7} {:>9}'.format('Total', total['candidates'], total['mechanisms'], total['no_supplement'], total['no_mech_attachment']))

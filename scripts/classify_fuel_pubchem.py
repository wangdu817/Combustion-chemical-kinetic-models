#!/usr/bin/env python3
"""Classify unknown_fuel papers using pubchempy + simple chemical name extraction.
Scans abstract for potential chemical names, verifies against PubChem, 
then maps verified names to fuel categories.
"""
import sys, json, re
from pathlib import Path

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import read_metadata, write_metadata, detect_fuel, normalize_abstract

ROOT = REPO / 'combustion_and_flame_mechanisms'

# Simple chemical name patterns found in combustion papers
CHEM_PATTERNS = [
    # Chemical formulas
    r'\b[A-Z][a-z]?\d*(?:[A-Z][a-z]?\d*)+\b',  # C8H10, SiH4, CH3OH
    # Named compounds (capitalized, multi-word)
    r'\b(?:n-|iso-|tert-|cis-|trans-|1,?\d-)?[A-Z][a-z]+(?:[- ][a-z0-9,]+){0,3}\b',
    # Numbers with suffixes: JP-10, RP-3
    r'\b[A-Z]{2,4}-\d+\b',
]

def extract_candidates(text):
    """Extract potential chemical names from text."""
    candidates = set()
    for pat in CHEM_PATTERNS:
        for m in re.finditer(pat, text):
            name = m.group(0).strip('.,;:()[]{}')
            if len(name) > 2 and not name.lower() in STOP_WORDS:
                candidates.add(name)
    return candidates

STOP_WORDS = {
    'the', 'and', 'for', 'was', 'with', 'that', 'this', 'from', 'are',
    'has', 'had', 'not', 'but', 'its', 'can', 'may', 'also', 'used',
    'were', 'been', 'will', 'have', 'than', 'more', 'over', 'into',
    'such', 'only', 'other', 'new', 'some', 'could', 'these', 'which',
    'their', 'time', 'first', 'would', 'about', 'after', 'between',
    'during', 'through', 'under', 'while', 'above', 'below',
    'one', 'two', 'three', 'high', 'low', 'large', 'small',
    'data', 'model', 'method', 'result', 'study', 'experiment',
    'figure', 'table', 'paper', 'work', 'process', 'system',
    'The', 'In', 'This', 'For', 'An', 'At', 'It', 'We', 'A',
    'Combustion', 'Flame', 'Journal', 'DOI', 'ScienceDirect',
    'Elsevier', 'Copyright', 'Abstract', 'Introduction', 'Conclusion',
}

def verify_pubchem(name):
    """Check if a name exists in PubChem."""
    try:
        import pubchempy as pcp
        compounds = pcp.get_compounds(name, 'name', listkey_count=1)
        return len(compounds) > 0
    except Exception:
        return False

# Main
records = read_metadata()
unknown = [r for r in records if r.get('fuelType') == 'unknown_fuel'
           and r.get('processingStatus') in ('included', 'conversion_failed')]

print(f'Unknown fuel papers to classify: {len(unknown)}')

classified = 0
for r in unknown:
    title = str(r.get('title', ''))
    abstract = normalize_abstract(r.get('abstract', ''))
    text = title + ' ' + abstract
    
    # Extract candidates
    candidates = extract_candidates(text)
    
    # Filter common fuel terms first (fast regex)
    fuel_terms = set()
    FUEL_QUICK = [
        'methane', 'ethane', 'propane', 'butane', 'pentane', 'hexane', 'heptane', 'octane', 'nonane', 'decane',
        'dodecane', 'hexadecane', 'ethylene', 'propylene', 'butene', 'acetylene', 'benzene', 'toluene', 'xylene',
        'naphthalene', 'methanol', 'ethanol', 'propanol', 'butanol', 'pentanol', 'dimethyl ether', 'diethyl ether',
        'hydrogen', 'ammonia', 'syngas', 'diesel', 'gasoline', 'jet fuel', 'kerosene', 'naphtha',
        'silane', 'disilane', 'RDX', 'CL-20', 'HMX', 'JP-10', 'surrogate',
    ]
    for term in FUEL_QUICK:
        if re.search(r'\b' + re.escape(term) + r'\b', text, re.I):
            fuel_terms.add(term.lower().replace(' ', '_'))
    
    if fuel_terms:
        # Re-run detect_fuel with the enhanced text
        # Temporarily add found terms to the record's keywords for detection
        old_fuel = r.get('fuelType')
        r['_found_terms'] = list(fuel_terms)
        new_fuel = detect_fuel(r)
        if new_fuel != 'unknown_fuel':
            r['fuelType'] = new_fuel
            r.pop('_found_terms', None)
            classified += 1
            print(f'  {new_fuel:30s} <- {title[:60]}')
            continue
        r.pop('_found_terms', None)
    
    # If no match from quick patterns, print for manual review
    if not fuel_terms:
        print(f'  NO MATCH: {title[:70]}')
        print(f'    candidates: {sorted(candidates)[:10]}')

if classified:
    write_metadata(records)
    print(f'\nClassified: {classified}/{len(unknown)}')
    print(f'Re-run reclassify_fuel.py to move folders and update index.')

#!/usr/bin/env python3
"""Enrich abstracts for unknown_fuel papers only. Uses Crossref + OpenAlex APIs."""
import sys, json, time, urllib.request, urllib.parse
from pathlib import Path

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import read_metadata, write_metadata, normalize_abstract

records = read_metadata()
uf = [r for r in records if r.get('fuelType') == 'unknown_fuel'
      and r.get('processingStatus') in ('included', 'conversion_failed')
      and not normalize_abstract(r.get('abstract', ''))
      and r.get('doi')]

print(f'Papers to enrich: {len(uf)}')

enriched = 0
for r in uf:
    doi = r.get('doi', '').strip()
    title = str(r.get('title', ''))[:60]
    
    # Try Crossref first
    abstract = ''
    try:
        url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi)
        req = urllib.request.Request(url, headers={'User-Agent': 'MechCollector/1.0'})
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())
        abstract = data.get('message', {}).get('abstract', '') or ''
    except Exception:
        pass
    
    # Fallback to OpenAlex
    if not abstract:
        try:
            url = 'https://api.openalex.org/works/https://doi.org/' + urllib.parse.quote(doi)
            req = urllib.request.Request(url, headers={'User-Agent': 'MechCollector/1.0'})
            resp = urllib.request.urlopen(req, timeout=10)
            data = json.loads(resp.read())
            ai = data.get('abstract_inverted_index', {}) or {}
            if ai:
                # Reconstruct abstract from inverted index
                positions = {}
                for word, indexes in ai.items():
                    for idx in indexes:
                        positions[idx] = word
                abstract = ' '.join(positions[i] for i in sorted(positions))
        except Exception:
            pass
    
    if abstract and len(abstract) > 50:
        r['abstract'] = abstract
        r['abstractSource'] = 'crossref_or_openalex'
        enriched += 1
        print(f'  [{enriched}] {title}')
    else:
        print(f'  [FAIL] {title}')
    
    write_metadata(records)  # per-record persistence
    time.sleep(0.3)  # rate limit

print(f'\nEnriched: {enriched}/{len(uf)}')

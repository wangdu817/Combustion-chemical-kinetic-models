#!/usr/bin/env python3
"""
Enrich article abstracts using Elsevier and Semantic Scholar APIs.
Set API keys via environment or api_keys.json.
"""
import json, re, time, html, os, urllib.request, urllib.parse
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'

def load_api_keys():
    keys = {}
    for ev, name in [('ELSEVIER_API_KEY', 'elsevier'), ('SEMANTIC_API_KEY', 'semantic')]:
        val = os.environ.get(ev, '').strip()
        if val: keys[name] = val
    if (REPO / 'api_keys.json').exists():
        keys.update(json.loads((REPO / 'api_keys.json').read_text()))
    return keys

def norm(text):
    text = html.unescape(text or '')
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def fetch_elsevier(doi, key):
    url = f'https://api.elsevier.com/content/article/doi/{urllib.parse.quote(doi)}'
    req = urllib.request.Request(url, headers={'X-ELS-APIKey': key, 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode('utf-8', errors='replace'))
    cd = data.get('full-text-retrieval-response', {}).get('coredata', {})
    return norm(cd.get('dc:description', ''))

def fetch_openalex(doi):
    url = f'https://api.openalex.org/works/https://doi.org/{urllib.parse.quote(doi)}'
    req = urllib.request.Request(url, headers={'User-Agent': 'MechColl/1.0', 'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = json.loads(resp.read().decode('utf-8', errors='replace'))
    inv = data.get('abstract_inverted_index')
    if not inv: return ''
    pos = {}
    for w, idxs in inv.items():
        if isinstance(idxs, list):
            for i in idxs:
                if isinstance(i, int): pos[i] = str(w)
    return norm(' '.join(pos[i] for i in sorted(pos)))

def main():
    keys = load_api_keys()
    if not keys:
        print("ERROR: No API keys. Set ELSEVIER_API_KEY env var or api_keys.json")
        return 1
    meta = json.loads(META.read_text('utf-8'))
    todo = []
    for r in meta:
        if r.get('processingStatus') not in ('included', 'conversion_failed'): continue
        if norm(r.get('abstract', '')): continue
        if r.get('doi'): todo.append(r)
    print(f'Need abstracts: {len(todo)}')
    changed = 0
    for i, r in enumerate(todo):
        doi = r['doi']; title = (r.get('title','') or '')[:50]
        print(f'[{i+1}/{len(todo)}] {title}...', end=' ', flush=True)
        abstract = ''
        if 'elsevier' in keys:
            try: abstract = fetch_elsevier(doi, keys['elsevier'])
            except: pass
        if not abstract:
            try: abstract = fetch_openalex(doi)
            except: pass
        if abstract and len(abstract) > 40:
            r['abstract'] = abstract; r['abstractSource'] = 'elsevier-api' if 'elsevier' in keys else 'openalex'
            changed += 1; print(f'OK ({len(abstract)} chars)')
        else: print('NOT FOUND')
        if changed % 10 == 0 and changed:
            META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
        time.sleep(0.8)
    if changed:
        META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nDone: {changed}/{len(todo)}')
    return 0

if __name__ == '__main__':
    import sys; sys.exit(main())

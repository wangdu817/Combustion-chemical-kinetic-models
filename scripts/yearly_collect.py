#!/usr/bin/env python3
"""Collect mechanisms for one year: metadata → probe → download → process → abstracts → PDFs → clean"""
import json, re, os, sys, time, urllib.request, urllib.parse, shutil, subprocess
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
PYTHON = os.environ.get('MECH_COLLECTION_PYTHON', sys.executable)
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
OUT = REPO / 'combustion_and_flame_mechanisms' / '_raw' / f'{sys.argv[1]}_volumes' if len(sys.argv) > 1 else None

def run(cmd, *args):
    full = [PYTHON, str(REPO / 'scripts' / 'collect_cf2026.py'), cmd] + list(args)
    print(f'  Running: collect_cf2026.py {cmd} {" ".join(args)}')
    result = subprocess.run(full, capture_output=True, text=True, timeout=14400)
    if result.returncode != 0:
        print(f'  ERROR: {result.stderr[-200:]}')
    return result.returncode

def run_script(script, *args):
    full = [PYTHON, str(REPO / 'scripts' / script)] + list(args)
    print(f'  Running: {script} {" ".join(args)}')
    result = subprocess.run(full, capture_output=True, text=True, timeout=14400)
    return result.returncode

def main():
    year = sys.argv[1]
    print(f'\n=== Collecting {year} mechanisms ===')
    
    # Step 1: Fetch metadata from Crossref
    print(f'[1/7] Fetching metadata from Crossref...')
    months = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    total = None; offset = 0; rows = 100; items = []
    OUT.mkdir(parents=True, exist_ok=True)
    
    while True:
        url = (f'https://api.crossref.org/works?filter=issn:0010-2180,'
               f'from-pub-date:{year}-01-01,until-pub-date:{year}-12-31'
               f'&rows={rows}&offset={offset}'
               f'&select=DOI,title,author,volume,page,issued,alternative-id')
        req = urllib.request.Request(url, headers={'User-Agent': 'MechColl/1.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
        msg = data['message']
        if total is None: total = msg['total-results']; print(f'  Total: {total}')
        items.extend(msg.get('items',[]))
        if len(items) >= total: break
        offset += rows; time.sleep(0.3)
    
    by_vol = {}
    for item in items:
        vol = item.get('volume','?'); by_vol.setdefault(vol, []).append(item)
    for vol in sorted(by_vol, key=lambda x: int(x) if x.isdigit() else 0):
        recs = []
        for item in by_vol[vol]:
            doi = item.get('DOI',''); aids = item.get('alternative-id',[])
            pii = next((a for a in aids if a.startswith('S00102180')), '')
            title = (item.get('title') or [''])[0]
            issued = item.get('issued',{}).get('date-parts',[[int(year)]])[0]
            m = months[issued[1]] if len(issued)>1 and issued[1]<=12 else ''
            authors = [f"{a.get('given','')} {a.get('family','')}".strip() for a in item.get('author',[]) if a.get('family')]
            recs.append(dict(year=str(issued[0]),volume=vol,month=m,title=title,authors=authors,
                            doi=doi,pii=pii,articleNumber=item.get('page',''),
                            url=f'https://www.sciencedirect.com/science/article/pii/{pii}' if pii else '',
                            issuePdfLink=''))
        (OUT / f'volume_{vol}.json').write_text(json.dumps(recs, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'  Volume {vol}: {len(recs)}')
    print(f'  Done: {len(items)} articles')
    
    # Step 2: Import
    print(f'[2/7] Importing metadata...')
    rc = run('import-sciencedirect-metadata', '--year', year, '--source-dir', str(OUT))
    
    # Step 3: Probe + download only (process runs once at end for all years)
    print(f'[3/5] Probing supplements (parallel, all cores)...')
    rc = run('probe-supplements', '--year', year, '--max-mmc', '12')
    
    print(f'[4/5] Downloading supplements...')
    rc = run('download-supplements', '--year', year)
    
    # Step 4: PDFs (only if ≤2021)
    print(f'[5/5] Downloading PDFs...')
    if int(year) <= 2021:
        rc = run_script('scihub_dl.py')
    else:
        print('  Skipped PDFs (year > 2021)')
    
    # Clean non-mechanism downloads
    print(f'Cleaning downloads...')
    m = json.loads(META.read_text('utf-8'))
    mech_piis = set()
    for r in m:
        if r.get('processingStatus') in ('included','conversion_failed'):
            p = r.get('pii','')
            if p: mech_piis.add(p)
    dl_dir = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'downloads'
    kept = deleted = 0
    for f in dl_dir.iterdir():
        if not f.is_file(): continue
        if any(f.name.startswith(pii) for pii in mech_piis):
            kept += 1
        else:
            f.unlink(); deleted += 1
    
    # Clean _processing for excluded articles
    for pp in (REPO / 'combustion_and_flame_mechanisms').glob(f'*/{year}/*/_processing'):
        if str(pp.parent) not in {r.get('processingFolder','') for r in m if r.get('processingStatus') in ('included','conversion_failed')}:
            shutil.rmtree(pp, ignore_errors=True)
    
    print(f'Done: {kept} kept, {deleted} deleted from downloads')
    print(f'=== {year} complete ===')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python yearly_collect.py YEAR')
        sys.exit(1)
    main()

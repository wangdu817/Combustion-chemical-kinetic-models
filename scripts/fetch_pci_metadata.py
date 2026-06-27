#!/usr/bin/env python3
"""
Fetch Proceedings of the Combustion Institute metadata from Crossref API
and write volume JSON files compatible with collect_cf2026.py import.

Output: combustion_and_flame_mechanisms/_raw/20XX_volumes_PCI/volume_N.json
"""
import json, time, urllib.request, urllib.error, re, os
from pathlib import Path

ISSN = '1540-7489'
REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path.cwd()))
RAW = REPO / 'combustion_and_flame_mechanisms' / '_raw'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (mechanism-collector; mailto:179152696@qq.com) Crossref-API/1.0'
}

def fetch_year(year):
    out_dir = RAW / f'{year}_volumes_PCI'
    out_dir.mkdir(parents=True, exist_ok=True)
    
    all_items = []
    cursor = '*'
    page = 0
    
    while True:
        url = (f'https://api.crossref.org/works'
               f'?filter=issn:{ISSN},from-pub-date:{year}-01-01,until-pub-date:{year}-12-31'
               f'&rows=100&cursor={cursor}')
        
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read())
        except Exception as e:
            print(f'  Error at cursor {cursor[:20]}...: {e}')
            time.sleep(5)
            continue
        
        items = data['message']['items']
        all_items.extend(items)
        page += 1
        total = data['message']['total-results']
        print(f'  Page {page}: {len(all_items)}/{total} items')
        
        cursor = data['message'].get('next-cursor')
        if not cursor or len(items) < 100:
            break
        
        time.sleep(0.3)  # Be nice to Crossref
    
    # Group by volume
    months = {'1': 'Jan','2': 'Feb','3': 'Mar','4': 'Apr','5': 'May','6': 'Jun',
              '7': 'Jul','8': 'Aug','9': 'Sep','10': 'Oct','11': 'Nov','12': 'Dec'}
    
    by_volume = {}
    for item in all_items:
        vol = str(item.get('volume', '?') or '?')
        if vol not in by_volume:
            by_volume[vol] = []
        
        doi = item.get('DOI','')
        aids = item.get('alternative-id',[])
        pii = next((a for a in aids if a.startswith('S')), '')
        title = (item.get('title') or [''])[0]
        issued = item.get('issued',{}).get('date-parts',[[int(year)]])[0]
        m = months.get(str(issued[1]),'') if len(issued)>1 and issued[1]<=12 else ''
        authors = [f"{a.get('given','')} {a.get('family','')}".strip() 
                   for a in item.get('author',[]) if a.get('family')]
        
        by_volume[vol].append(dict(
            year=str(issued[0]), volume=vol, month=m, title=title,
            authors=authors, doi=doi, pii=pii,
            articleNumber=item.get('page',''),
            url=f'https://www.sciencedirect.com/science/article/pii/{pii}' if pii else ''
        ))
    
    # Write volume JSONs
    for vol, recs in sorted(by_volume.items()):
        fname = out_dir / f'volume_{vol}.json'
        fname.write_text(json.dumps(recs, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f'  Volume {vol}: {len(recs)} articles')
    
    print(f'  Done: {len(all_items)} total')
    return out_dir

if __name__ == '__main__':
    import sys
    years = sys.argv[1:] if len(sys.argv) > 1 else [str(y) for y in range(2008, 2027)]
    for y in years:
        print(f'\n=== PCI {y} ===')
        fetch_year(y)

#!/usr/bin/env python3
"""Sci-Hub PDF download via sci.bban.top CDN (no captcha needed).
Only downloads articles from 2021 and earlier.
PDFs are saved alongside mechanism files with matching naming.
"""
import json, re, os, time, urllib.request, urllib.error
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))

# Helpers matching collect_cf2026 naming convention
def slugify(v, n=80):
    v = re.sub(r'<[^>]+>', '', (v or '').lower())
    v = re.sub(r'[^a-z0-9]+', '_', v); v = re.sub(r'_+', '_', v).strip('_')
    return (v[:n].strip('_') or 'unknown')

def surname(a):
    a = re.sub(r'<[^>]+>', '', str(a or '')).strip(); a = re.sub(r'\s+', ' ', a)
    if not a: return 'unknown'
    if ',' in a: return a.split(',', 1)[0].strip() or 'unknown'
    tokens = [t for t in re.split(r'\s+', a) if t]
    return tokens[-1] if tokens else 'unknown'

FUEL_P = [(r'NH\s*3|ammonia','ammonia'),(r'n-dodecane|dodecane','n_dodecane'),
    (r'methane|CH\s*4','methane'),(r'hydrogen|H\s*2','hydrogen'),
    (r'ethylene|C\s*2\s*H\s*4','ethylene'),(r'propane','propane'),
    (r'n-heptane|heptane','n_heptane'),(r'methanol','methanol'),
    (r'dimethyl ether|DME','dimethyl_ether'),(r'n-butane|butane','n_butane'),
    (r'RP-?3','rp3'),(r'acetylene','acetylene')]

def fuel(r):
    t = str(r.get('title',''))+' '+str(r.get('abstract',''))
    labels = []
    for p,lb in FUEL_P:
        if re.search(p,t,re.I) and lb not in labels: labels.append(lb)
    return '_'.join(labels[:3]) or 'unknown_fuel'

def ryear(r):
    for k in ('year','publicationYear'):
        v = str(r.get(k,'') or '').strip()
        if re.fullmatch(r'\d{4}',v): return v
    return 'unknown'

def aid(r):
    if r.get('articleNumber'): return str(r['articleNumber'])
    m = re.search(r'(1\d{5})',(r.get('doi','') or '').strip().lower())
    if m: return m.group(1)
    p = r.get('pii',''); return p[-8:] if p else 'article'

def pdf_name(r):
    fu = r.get('fuelType') or fuel(r); y = ryear(r)
    au = r.get('authors',[])
    fa = au.split(',')[0].strip() if isinstance(au,str) else (str(au[0]).strip() if au else 'unknown')
    return f'{slugify(surname(fa),24)}_{y}_{slugify(fu,60)}_{aid(r)}.pdf'

def main():
    meta = json.loads(META.read_text('utf-8'))
    
    # Collect ≤2021 articles with mechanisms
    todo = []
    for r in meta:
        if r.get('processingStatus') not in ('included','conversion_failed'): continue
        y = ryear(r)
        if not y.isdigit() or int(y) > 2021: continue
        
        nm = pdf_name(r)
        folder = r.get('processingFolder','')
        target = Path(folder) / nm if folder else ROOT / '_raw' / 'pdfs' / nm
        
        if target.exists() and target.stat().st_size > 5000:
            continue  # Already have it
        
        todo.append((r, target))
    
    print(f'≤2021 articles: {len(todo)} PDFs needed')
    if not todo:
        print("All done!"); return
    
    ok = 0; fail = 0
    for i, (r, target) in enumerate(todo):
        doi = r['doi']; year = ryear(r)
        title = (r.get('title','') or '')[:55]
        url = f'https://sci.bban.top/pdf/{doi}.pdf?download=true'
        
        print(f'[{i+1}/{len(todo)}] [{year}] {title}...', end=' ', flush=True)
        
        try:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
                'Referer': 'https://sci-hub.ren/'
            })
            with urllib.request.urlopen(req, timeout=20) as resp:
                content = resp.read()
            
            if content[:4] == b'%PDF' and len(content) > 5000:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
                r['paperPdfLocal'] = str(target)
                r['paperPdfSource'] = 'sci-hub-bban'
                ok += 1
                print(f'OK ({len(content)/1024:.0f} KB)')
            else:
                fail += 1
                print('NOT PDF')
        except urllib.error.HTTPError as e:
            fail += 1
            print(f'HTTP {e.code}')
        except Exception as e:
            fail += 1
            print(f'ERR: {str(e)[:40]}')
        
        # Save metadata every 10
        if ok % 10 == 0 and ok > 0:
            META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
        
        time.sleep(0.5)  # rate limit
    
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nDone: {ok} OK, {fail} failed, {ok+fail} total')

if __name__ == '__main__':
    main()

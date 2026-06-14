#!/usr/bin/env python3
"""Download PDFs via Elsevier API - no captcha, no VNC needed."""
import json, re, os, time, urllib.request, urllib.parse
from pathlib import Path

API_KEY='d3c761...789c'
REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))

def slugify(v, n=80):
    v = re.sub(r'<[^>]+>', '', (v or '').lower())
    v = re.sub(r'[^a-z0-9]+', '_', v); v = re.sub(r'_+', '_', v).strip('_')
    return (v[:n].strip('_') or 'unknown')

def surname(a):
    a = re.sub(r'<[^>]+>', '', str(a or '')).strip(); a = re.sub(r'\s+', ' ', a)
    if not a: return 'unknown'
    if ',' in a: return a.split(',', 1)[0].strip() or 'unknown'
    return [t for t in re.split(r'\s+', a) if t][-1] if [t for t in re.split(r'\s+', a) if t] else 'unknown'

FUEL_P = [(r'NH\s*3|ammonia', 'ammonia'), (r'n-dodecane|dodecane', 'n_dodecane'),
    (r'methane|CH\s*4', 'methane'), (r'hydrogen|H\s*2', 'hydrogen'),
    (r'ethylene|C\s*2\s*H\s*4', 'ethylene'), (r'propane', 'propane'),
    (r'n-heptane|heptane', 'n_heptane'), (r'methanol', 'methanol'),
    (r'dimethyl ether|DME', 'dimethyl_ether'), (r'n-butane|butane', 'n_butane'),
    (r'RP-?3', 'rp3'), (r'acetylene', 'acetylene')]

def fuel(r):
    t = str(r.get('title', '')) + ' ' + str(r.get('abstract', ''))
    l = []
    for p, lb in FUEL_P:
        if re.search(p, t, re.I) and lb not in l: l.append(lb)
    return '_'.join(l[:3]) or 'unknown_fuel'

def r_year(r):
    for k in ('year', 'publicationYear'):
        v = str(r.get(k, '') or '').strip()
        if re.fullmatch(r'\d{4}', v): return v
    return 'unknown'

def art_id(r):
    if r.get('articleNumber'): return str(r['articleNumber'])
    m = re.search(r'(1\d{5})', (r.get('doi', '') or '').strip().lower())
    if m: return m.group(1)
    p = r.get('pii', ''); return p[-8:] if p else 'article'

def pdf_name(r):
    fu = r.get('fuelType') or fuel(r); y = r_year(r)
    au = r.get('authors', [])
    fa = au.split(',')[0].strip() if isinstance(au, str) else (str(au[0]).strip() if au else 'unknown')
    return f'{slugify(surname(fa), 24)}_{y}_{slugify(fu, 60)}_{art_id(r)}.pdf'

def download(doi, dest):
    """Download PDF via Elsevier API."""
    url = f'https://api.elsevier.com/content/article/doi/{urllib.parse.quote(doi)}'
    req = urllib.request.Request(url, headers={
        'X-ELS-APIKey': API_KEY,
        'Accept': 'application/pdf'
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read()
        if content[:4] == b'%PDF':
            dest.write_bytes(content)
            return len(content)
        else:
            return 0
    except urllib.error.HTTPError as e:
        return -e.code
    except Exception as e:
        return 0

def main():
    meta = json.loads(META.read_text('utf-8'))
    
    need = []
    for r in meta:
        if r.get('processingStatus') not in ('included', 'conversion_failed'):
            continue
        nm = pdf_name(r)
        f = r.get('processingFolder', '')
        if f and (Path(f) / nm).exists(): continue
        if (ROOT / '_raw' / 'pdfs' / nm).exists(): continue
        need.append(r)
    
    if not need:
        print("All PDFs downloaded!")
        return
    
    print(f'{len(need)} PDFs needed. Downloading via Elsevier API...\n')
    
    ok = 0; fail = 0; ratelimit = 0
    
    for i, r in enumerate(need):
        doi = r['doi']
        title = (r.get('title', '') or '')[:55]
        nm = pdf_name(r)
        f = r.get('processingFolder', '')
        dest = Path(f) / nm if f else ROOT / '_raw' / 'pdfs' / nm
        dest.parent.mkdir(parents=True, exist_ok=True)
        
        print(f'[{i+1}/{len(need)}] {title}...', end=' ', flush=True)
        
        # Download
        size = download(doi, dest)
        
        if size > 0:
            ok += 1
            print(f'OK ({size/1024:.0f} KB)')
        elif size == -429:
            ratelimit += 1
            print(f'RATE LIMITED, waiting 10s...')
            time.sleep(10)
            size = download(doi, dest)
            if size > 0:
                ok += 1; print(f'  OK after retry')
            else:
                fail += 1; print(f'  still failed')
        else:
            fail += 1
            print(f'FAILED (code={size})')
        
        # Rate limit: 3 requests per second max
        time.sleep(0.4)
        
        # Save metadata every 10
        if ok % 10 == 0:
            r['paperPdfLocal'] = str(dest)
            META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    
    # Final save
    for r in need:
        nm = pdf_name(r)
        f = r.get('processingFolder', '')
        dest = Path(f) / nm if f else ROOT / '_raw' / 'pdfs' / nm
        if dest.exists():
            r['paperPdfLocal'] = str(dest)
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    
    print(f'\nDone: {ok} OK, {fail} failed, {ratelimit} rate-limited')

if __name__ == '__main__':
    main()

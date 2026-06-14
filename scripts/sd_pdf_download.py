#!/usr/bin/env python3
"""
Direct PDF download from ScienceDirect via logged-in VNC Chrome.
Uses xdotool to navigate to article pages and click PDF buttons.
No captchas needed - uses your institutional login session.
"""
import json, re, os, subprocess, time, shutil
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))
DISPLAY = ':99'
SD = 'https://www.sciencedirect.com/science/article/pii/'

def slugify(v, n=80):
    v = re.sub(r'<[^>]+>','',(v or '').lower()); v = re.sub(r'[^a-z0-9]+','_',v); v = re.sub(r'_+','_',v).strip('_')
    return (v[:n].strip('_') or 'unknown')

def surname(a):
    a = re.sub(r'<[^>]+>','',str(a or '')).strip(); a = re.sub(r'\s+',' ',a)
    if not a: return 'unknown'
    if ',' in a: return a.split(',',1)[0].strip() or 'unknown'
    t = [t for t in re.split(r'\s+',a) if t]; return t[-1] if t else 'unknown'

def art_id(r):
    if r.get('articleNumber'): return str(r['articleNumber'])
    m = re.search(r'(1\d{5})',(r.get('doi','') or '').strip().lower())
    if m: return m.group(1)
    p = r.get('pii',''); return p[-8:] if p else 'article'

def r_year(r):
    for k in ('year','publicationYear'):
        v = str(r.get(k,'') or '').strip()
        if re.fullmatch(r'\d{4}',v): return v
    return 'unknown'

FUEL_P = [(r'NH\s*3|ammonia','ammonia'),(r'n-dodecane|dodecane','n_dodecane'),
    (r'methane|CH\s*4','methane'),(r'hydrogen|H\s*2','hydrogen'),
    (r'ethylene|C\s*2\s*H\s*4','ethylene'),(r'propane','propane'),
    (r'n-heptane|heptane','n_heptane'),(r'methanol','methanol'),
    (r'dimethyl ether|DME','dimethyl_ether'),(r'n-butane|butane','n_butane'),
    (r'RP-?3','rp3'),(r'acetylene','acetylene')]
def fuel(r):
    t = str(r.get('title',''))+' '+str(r.get('abstract',''))
    l = []; [l.append(lb) for p,lb in FUEL_P if re.search(p,t,re.I) and lb not in l]
    return '_'.join(l[:3]) or 'unknown_fuel'

def pdf_name(r):
    fu = r.get('fuelType') or fuel(r); y = r_year(r)
    au = r.get('authors',[])
    if isinstance(au,str): fa = au.split(',')[0].strip()
    elif au: fa = str(au[0]).strip()
    else: fa = 'unknown'
    return f'{slugify(surname(fa),24)}_{y}_{slugify(fu,60)}_{art_id(r)}.pdf'

def xdo(cmd):
    env = os.environ.copy(); env['DISPLAY'] = DISPLAY
    return subprocess.run(cmd, capture_output=True, text=True, timeout=8, env=env)

def main():
    meta = json.loads(META.read_text('utf-8'))
    
    need = []
    for r in meta:
        if r.get('processingStatus') not in ('included','conversion_failed'): continue
        nm = pdf_name(r)
        f = r.get('processingFolder','')
        found = False
        if f and (Path(f)/nm).exists(): found = True
        if not found and (ROOT/'_raw'/'pdfs'/nm).exists(): found = True
        if not found: need.append(r)
    
    if not need:
        print("All PDFs downloaded!"); return
    
    print(f'{len(need)} PDFs needed.')
    print('Make sure VNC Chrome is logged into ScienceDirect.')
    print('Press Ctrl+C to stop anytime.\n')
    
    dl = Path.home() / 'Downloads'
    dl.mkdir(exist_ok=True)
    
    ok = 0; skip = 0
    
    for i, r in enumerate(need):
        pii = r.get('pii','')
        if not pii:
            skip += 1; continue
        
        title = (r.get('title','') or '')[:55]
        nm = pdf_name(r)
        folder = r.get('processingFolder','')
        dest = (Path(folder) / nm) if folder else (ROOT / '_raw' / 'pdfs' / nm)
        dest.parent.mkdir(parents=True, exist_ok=True)
        
        url = f'{SD}{pii}'
        print(f'[{i+1}/{len(need)}] {title}')
        
        # Open SD article in VNC Chrome
        subprocess.Popen(
            ['google-chrome-stable', '--no-sandbox', '--disable-gpu', url],
            env={**os.environ, 'DISPLAY': DISPLAY},
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        time.sleep(3)
        
        # Focus Chrome
        xdo(['xdotool', 'search', '--class', 'Google-chrome', 'windowactivate'])
        time.sleep(1)
        
        # Strategy: ScienceDirect has a "View PDF" link or the page redirects to PDF
        # Try Ctrl+Shift+P (often opens PDF) or Tab to PDF link
        # Or navigate directly to PDF URL pattern
        # The PDF URL follows: /article/pii/{PII}/pdfft?md5=...
        
        # Try the PDF URL directly first - this often works if logged in
        pdf_url = f'{SD}{pii}/pdfft'
        subprocess.Popen(
            ['google-chrome-stable', '--no-sandbox', '--disable-gpu', pdf_url],
            env={**os.environ, 'DISPLAY': DISPLAY},
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        time.sleep(2)
        
        # Try to save - Ctrl+S
        xdo(['xdotool', 'search', '--class', 'Google-chrome', 'windowactivate'])
        time.sleep(0.5)
        xdo(['xdotool', 'key', 'ctrl+s'])
        time.sleep(1)
        xdo(['xdotool', 'key', 'Return'])  # Confirm save dialog
        time.sleep(2)
        
        # Check for downloaded PDF
        downloaded = None
        for pdf in sorted(dl.glob('*.pdf'), key=lambda p: p.stat().st_mtime, reverse=True):
            age = time.time() - pdf.stat().st_mtime
            if age < 15 and pdf.stat().st_size > 5000:
                downloaded = pdf; break
        
        if downloaded and not dest.exists():
            shutil.move(str(downloaded), str(dest))
            ok += 1
            print(f'  OK ({dest.stat().st_size:,} bytes)')
        elif dest.exists():
            ok += 1
            print(f'  OK (already exists)')
        else:
            skip += 1
            print(f'  SKIP (no PDF)')
        
        # Rate limit to avoid ScienceDirect blocking
        time.sleep(3)
    
    print(f'\nDone: {ok} downloaded, {skip} skipped')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Sci-Hub PDF download via VNC Chrome + xdotool.
User solves ONE captcha, script handles the rest.

Method:
1. Open sci-hub.ren in VNC Chrome
2. User solves captcha
3. For each DOI: types DOI into sci-hub, clicks Open, waits for PDF, saves
"""
import json, re, os, subprocess, time, shutil
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))
DISPLAY = ':99'
SH = 'https://sci-hub.ren/'

def xdo(cmd):
    env = os.environ.copy(); env['DISPLAY'] = DISPLAY
    return subprocess.run(cmd, capture_output=True, text=True, timeout=8, env=env)

def main():
    meta = json.loads(META.read_text('utf-8'))
    
    # Collect: try bban.top first (fast, no captcha), then sci-hub.ren (needs captcha)
    need = []
    for r in meta:
        if r.get('processingStatus') not in ('included','conversion_failed'): continue
        doi = r['doi']; year = r.get('year','')
        # Skip if already has PDF
        # ... (check existing PDFs)
        need.append(r)
    
    print(f'{len(need)} PDFs needed.')
    print('\nStep 1: try sci.bban.top (no captcha, pre-2022 only)')
    
    dl_dir = Path.home() / 'Downloads'
    ok_bban = 0
    
    for i, r in enumerate(need):
        doi = r['doi']
        url = f'https://sci.bban.top/pdf/{doi}.pdf?download=true'
        dest = Path(r.get('processingFolder','')) / f'scihub_{r["doi"].replace("/","_")}.pdf'
        
        try:
            import urllib.request
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0',
                'Referer': 'https://sci-hub.ren/'
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                content = resp.read()
            if content[:4] == b'%PDF' and len(content) > 5000:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(content)
                ok_bban += 1
                print(f'  [{i+1}] OK (bban)')
        except:
            pass
        time.sleep(0.5)
    
    print(f'bban.top: {ok_bban}/{len(need)}')
    
    # Step 2: For remaining, use VNC + sci-hub.ren
    remaining = [r for r in need if not Path(r.get('processingFolder','')) / f'scihub_{r["doi"].replace("/","_")}.pdf']
    if not remaining:
        print("All done!")
        return
    
    print(f'\nStep 2: sci-hub.ren via VNC ({len(remaining)} articles)')
    print('Opening sci-hub.ren in VNC Chrome...')
    
    subprocess.Popen(['google-chrome-stable','--no-sandbox','--disable-gpu',SH],
                     env={**os.environ,'DISPLAY':DISPLAY},
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)
    input('Solve the captcha in VNC Chrome, then press ENTER here... ')
    
    ok_sh = 0
    for i, r in enumerate(remaining):
        doi = r['doi']; title = (r.get('title','') or '')[:50]
        print(f'\n[{i+1}/{len(remaining)}] {title}')
        
        # Focus Chrome, Ctrl+L to address bar
        xdo(['xdotool','search','--class','Google-chrome','windowactivate'])
        time.sleep(0.5)
        xdo(['xdotool','key','ctrl+l'])
        time.sleep(0.3)
        
        # Type sci-hub URL + DOI
        xdo(['xdotool','type',SH + doi])
        time.sleep(0.3)
        xdo(['xdotool','key','Return'])
        
        # Wait for page load
        time.sleep(4)
        
        # Try to find and click the download/save link
        # Sci-hub.ren has an embed/iframe with the PDF
        # We can directly try to download from the PDF URL
        
        # Check Downloads for new PDF
        before = set(dl_dir.glob('*.pdf'))
        time.sleep(2)
        after = set(dl_dir.glob('*.pdf'))
        new_pdfs = after - before
        
        if new_pdfs:
            src = list(new_pdfs)[0]
            dest = Path(r.get('processingFolder','')) / f'scihub_{doi.replace("/","_")}.pdf'
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dest))
            ok_sh += 1
            print(f'  OK')
        else:
            print(f'  SKIP (no download detected)')
        
        time.sleep(2)
    
    print(f'\nDone: bban={ok_bban}, sci-hub={ok_sh}, total={ok_bban+ok_sh}/{len(need)}')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Sci-Hub batch download using VNC Chrome session.
After user solves FIRST captcha, uses xdotool to navigate and download PDFs.
For articles that trigger captcha again, skips them.
"""
import json, re, os, subprocess, time, shutil
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))
DISPLAY = ':99'
SCI_HUB = 'https://sci-hub.ru/'

def slugify(value, max_len=80):
    value = re.sub(r'<[^>]+>', '', value or '').lower()
    value = re.sub(r'[^a-z0-9]+', '_', value); value = re.sub(r'_+', '_', value).strip('_')
    return (value[:max_len].strip('_') or 'unknown')

def first_author_surname(author):
    author = re.sub(r'<[^>]+>', '', author or '').strip(); author = re.sub(r'\s+', ' ', author)
    if not author: return 'unknown'
    if ',' in author: return author.split(',', 1)[0].strip() or 'unknown'
    tokens = [t for t in re.split(r'\s+', author) if t]
    return tokens[-1] if tokens else 'unknown'

def article_id(record):
    if record.get('articleNumber'): return str(record['articleNumber'])
    m = re.search(r'(1\d{5})', (record.get('doi','') or '').strip().lower())
    if m: return m.group(1)
    pii = record.get('pii') or ''; return pii[-8:] if pii else 'article'

def record_year(record):
    for key in ('year','publicationYear'):
        v = str(record.get(key,'') or '').strip()
        if re.fullmatch(r'\d{4}', v): return v
    return 'unknown'

FUEL_PATTERNS = [
    (r'NH\s*3|ammonia', 'ammonia'), (r'n-dodecane|dodecane', 'n_dodecane'),
    (r'methane|CH\s*4', 'methane'), (r'hydrogen|H\s*2', 'hydrogen'),
    (r'ethylene|C\s*2\s*H\s*4', 'ethylene'), (r'propane', 'propane'),
    (r'n-heptane|heptane', 'n_heptane'), (r'methanol', 'methanol'),
    (r'dimethyl ether|DME', 'dimethyl_ether'), (r'n-butane|butane', 'n_butane'),
    (r'RP-?3', 'rp3'), (r'acetylene', 'acetylene'),
]
def detect_fuel(record):
    text = str(record.get('title','')) + ' ' + str(record.get('abstract',''))
    labels = []; [labels.append(l) for p,l in FUEL_PATTERNS if re.search(p,text,re.I) and l not in labels]
    return '_'.join(labels[:3]) if labels else 'unknown_fuel'

def get_pdf_filename(record):
    fuel = record.get('fuelType') or detect_fuel(record); year = record_year(record)
    authors = record.get('authors', [])
    if isinstance(authors,str): fa = authors.split(',')[0].strip()
    elif authors: fa = str(authors[0]).strip()
    else: fa = 'unknown'
    return f'{slugify(first_author_surname(fa),24)}_{year}_{slugify(fuel,60)}_{article_id(record)}.pdf'

def xdo(cmd):
    env = os.environ.copy(); env['DISPLAY'] = DISPLAY
    return subprocess.run(cmd, capture_output=True, text=True, timeout=10, env=env)

def click_save(display):
    """Try to click Sci-Hub save button via xdotool."""
    # Try common button positions/selectors
    for _ in range(3):
        xdo(['xdotool', 'key', 'Tab']); time.sleep(0.15)
    xdo(['xdotool', 'key', 'Return']); time.sleep(1.5)

def check_download(dl_dir):
    """Check if a new PDF appeared in Downloads."""
    for pdf in sorted(dl_dir.glob('*.pdf'), key=lambda p: p.stat().st_mtime, reverse=True):
        if time.time() - pdf.stat().st_mtime < 60:
            return pdf
    return None

def main():
    meta = json.loads(META.read_text('utf-8'))
    
    need = []
    for r in meta:
        if r.get('processingStatus') not in ('included','conversion_failed'): continue
        pdf_name = get_pdf_filename(r)
        folder = r.get('processingFolder','')
        found = False
        if folder and (Path(folder)/pdf_name).exists(): found = True
        if not found and (ROOT/'_raw'/'pdfs'/pdf_name).exists(): found = True
        if not found: need.append(r)
    
    if not need:
        print("No PDFs needed!"); return
    
    print(f'{len(need)} PDFs needed.')
    print(f'Using VNC Chrome on {DISPLAY}')
    print('Press Ctrl+C to stop at any time.\n')
    
    dl_dir = Path.home() / 'Downloads'
    dl_dir.mkdir(exist_ok=True)
    before_files = set(dl_dir.glob('*.pdf'))
    
    count = 0
    skipped = 0
    
    for i, r in enumerate(need):
        doi = r['doi']
        title = (r.get('title','') or '')[:55]
        pdf_name = get_pdf_filename(r)
        folder = r.get('processingFolder','')
        
        print(f'[{i+1}/{len(need)}] {title}')
        
        # Open Sci-Hub DOI in Chrome
        url = f'{SCI_HUB}{doi}'
        subprocess.Popen(
            ['google-chrome-stable', '--no-sandbox', '--disable-gpu', url],
            env={**os.environ, 'DISPLAY': DISPLAY},
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        time.sleep(3)
        
        # Try to activate Chrome
        xdo(['xdotool', 'search', '--class', 'Google-chrome', 'windowactivate'])
        time.sleep(1)
        
        # Click save button
        click_save(DISPLAY)
        time.sleep(2)
        
        # Check for downloaded PDF
        downloaded = None
        for pdf in sorted(dl_dir.glob('*.pdf'), key=lambda p: p.stat().st_mtime, reverse=True):
            if pdf not in before_files and time.time() - pdf.stat().st_mtime < 30:
                downloaded = pdf
                break
        
        if downloaded:
            dest = Path(folder) / pdf_name if folder else ROOT / '_raw' / 'pdfs' / pdf_name
            dest.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.move(str(downloaded), str(dest))
                count += 1
                before_files.add(dest)
                print(f'  OK -> {pdf_name}')
            except:
                print(f'  MOVE FAILED')
        else:
            print(f'  SKIP (no PDF detected)')
            skipped += 1
        
        # Rate limit
        time.sleep(2)
    
    print(f'\nDone. Downloaded: {count}/{len(need)}. Skipped: {skipped}.')
    print('Re-run to retry skipped articles.')

if __name__ == '__main__':
    main()

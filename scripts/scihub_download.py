#!/usr/bin/env python3
"""
Semi-automated Sci-Hub PDF download via VNC Chrome.
User solves captcha once in VNC, then this script automates the remaining downloads.
"""
import json, re, os, subprocess, time
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))
DISPLAY = ':99'
CHROME = 'google-chrome-stable'
SCI_HUB = 'https://sci-hub.ru/'

# Reuse helpers from list_scihub_urls
def slugify(value, max_len=80):
    value = re.sub(r'<[^>]+>', '', value or '').lower()
    value = re.sub(r'[^a-z0-9]+', '_', value)
    value = re.sub(r'_+', '_', value).strip('_')
    return (value[:max_len].strip('_') or 'unknown')

def first_author_surname(author):
    author = re.sub(r'<[^>]+>', '', author or '').strip()
    author = re.sub(r'\s+', ' ', author)
    if not author: return 'unknown'
    if ',' in author: return author.split(',', 1)[0].strip() or 'unknown'
    tokens = [t for t in re.split(r'\s+', author) if t]
    return tokens[-1] if tokens else 'unknown'

def article_id(record):
    if record.get('articleNumber'): return str(record['articleNumber'])
    doi = (record.get('doi', '') or '').strip().lower()
    m = re.search(r'(1\d{5})', doi)
    if m: return m.group(1)
    return 'article'

def record_year(record):
    for key in ('year', 'publicationYear'):
        v = str(record.get(key, '') or '').strip()
        if re.fullmatch(r'\d{4}', v): return v
    return 'unknown'

FUEL_PATTERNS = [
    (r'NH\s*3|ammonia', 'ammonia'), (r'n-dodecane|dodecane', 'n_dodecane'),
    (r'methane|CH\s*4', 'methane'), (r'hydrogen|H\s*2', 'hydrogen'),
    (r'ethylene|C\s*2\s*H\s*4', 'ethylene'), (r'propane', 'propane'),
    (r'n-heptane|heptane', 'n_heptane'), (r'methanol', 'methanol'),
    (r'dimethyl ether|DME', 'dimethyl_ether'), (r'ethanol', 'ethanol'),
    (r'acetone', 'acetone'), (r'n-butane|butane', 'n_butane'),
    (r'RP-?3', 'rp3'), (r'acetylene', 'acetylene'),
]

def detect_fuel(record):
    text = str(record.get('title', '')) + ' ' + str(record.get('abstract', ''))
    labels = []
    for pattern, label in FUEL_PATTERNS:
        if re.search(pattern, text, re.I) and label not in labels:
            labels.append(label)
    return '_'.join(labels[:3]) if labels else 'unknown_fuel'

def get_pdf_filename(record):
    fuel = record.get('fuelType') or detect_fuel(record)
    year = record_year(record)
    authors = record.get('authors', [])
    if isinstance(authors, str): fa = authors.split(',')[0].strip()
    elif authors: fa = str(authors[0]).strip()
    else: fa = 'unknown'
    surname = first_author_surname(fa)
    fuel_slug = slugify(fuel, 60)
    art = article_id(record)
    return f'{slugify(surname, 24)}_{year}_{fuel_slug}_{art}.pdf'

def run_xdotool(display, cmd):
    """Execute xdotool commands on the VNC display."""
    env = os.environ.copy()
    env['DISPLAY'] = display
    return subprocess.run(cmd, capture_output=True, text=True, timeout=10, env=env)

def main():
    meta = json.loads(META.read_text('utf-8'))
    
    # Collect articles needing PDFs
    need = []
    for r in meta:
        if r.get('processingStatus') not in ('included', 'conversion_failed'):
            continue
        pdf_name = get_pdf_filename(r)
        folder = r.get('processingFolder', '')
        found = False
        if folder:
            if (Path(folder) / pdf_name).exists(): found = True
        if not found and (ROOT / '_raw' / 'pdfs' / pdf_name).exists():
            found = True
        if not found:
            need.append(r)
    
    if not need:
        print("All PDFs already downloaded!")
        return
    
    print(f'{len(need)} PDFs needed.')
    print()
    print("=== INSTRUCTIONS ===")
    print("1. Connect VNC to localhost:5901")
    print("2. Chrome will open Sci-Hub")
    print("3. SOLVE THE CAPTCHA in the VNC browser")
    print("4. Once captcha is solved, this script auto-downloads PDFs")
    print()
    
    # Open Sci-Hub in VNC Chrome
    subprocess.Popen(
        [CHROME, '--no-sandbox', '--disable-gpu', SCI_HUB],
        env={**os.environ, 'DISPLAY': DISPLAY},
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    time.sleep(3)
    
    input("Press ENTER after captcha is solved in VNC Chrome... ")
    
    # Now auto-download each DOI
    count = 0
    for i, r in enumerate(need):
        doi = r['doi']
        title = (r.get('title', '') or '')[:50]
        pdf_name = get_pdf_filename(r)
        folder = r.get('processingFolder', '')
        
        print(f'\n[{i+1}/{len(need)}] {title}')
        
        # Focus Chrome window and open DOI
        run_xdotool(DISPLAY, ['xdotool', 'search', '--class', 'Google-chrome', 'windowactivate'])
        time.sleep(0.3)
        
        # Ctrl+L to focus address bar, type DOI + Enter
        run_xdotool(DISPLAY, ['xdotool', 'key', 'ctrl+l'])
        time.sleep(0.2)
        run_xdotool(DISPLAY, ['xdotool', 'type', SCI_HUB + doi])
        time.sleep(0.3)
        run_xdotool(DISPLAY, ['xdotool', 'key', 'Return'])
        
        # Wait for page to load
        print('  Loading...')
        time.sleep(3)
        
        # Try to detect PDF button and click it
        # Sci-Hub shows a SAVE button after the captcha
        run_xdotool(DISPLAY, ['xdotool', 'key', 'Tab'])  # Tab through to save button
        time.sleep(0.2)
        run_xdotool(DISPLAY, ['xdotool', 'key', 'Tab'])
        time.sleep(0.2)
        run_xdotool(DISPLAY, ['xdotool', 'key', 'Return'])  # Click save
        time.sleep(1)
        
        # Move downloaded PDF from ~/Downloads to article folder
        downloads = Path.home() / 'Downloads'
        recent_pdfs = sorted(downloads.glob('*.pdf'), key=lambda p: p.stat().st_mtime, reverse=True)
        if recent_pdfs:
            src = recent_pdfs[0]
            # Only move if downloaded in last 10 seconds
            if time.time() - src.stat().st_mtime < 10:
                dest = (Path(folder) / pdf_name) if folder else (ROOT / '_raw' / 'pdfs' / pdf_name)
                dest.parent.mkdir(parents=True, exist_ok=True)
                src.rename(dest)
                count += 1
                print(f'  Saved: {pdf_name}')
            else:
                print('  Download not detected')
        else:
            print('  No PDF found in Downloads')
        
        time.sleep(1)  # Rate limit
    
    print(f'\nDone. Downloaded: {count}/{len(need)} PDFs.')

if __name__ == '__main__':
    main()

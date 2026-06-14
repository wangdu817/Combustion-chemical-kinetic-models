#!/usr/bin/env python3
"""
Download article PDFs for mechanism folders.

Sources (in order):
  1. Unpaywall API — free, finds OA PDF URLs
  2. Sci-Hub — for pre-2021 articles only (requires browser captcha, see manual mode)

PDFs are saved to the same folder as mechanism files, named:
  {firstauthorsurname}_{year}_{fueltype}_{articlenumber}.pdf
"""
import json, re, time, html, os, urllib.request, urllib.parse, urllib.error
from pathlib import Path
from collections import defaultdict

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))
PDF_DIR = ROOT / '_raw' / 'pdfs'

UNPAYWALL_EMAIL = 'research@example.com'  # Replace with your email for rate limit
UA = 'MechColl/1.0'

# Sci-Hub domains known to work
SCI_HUB_DOMAINS = ['sci-hub.ru', 'sci-hub.ee', 'sci-hub.se', 'sci-hub.st']

def slugify(value, max_len=80):
    value = re.sub(r'<[^>]+>', '', value or '')
    value = value.lower()
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
    doi = (record.get('doi', '') or '').strip().replace('https://doi.org/', '').lower()
    match = re.search(r'(1\d{5})', doi)
    if match: return match.group(1)
    pii = record.get('pii') or ''
    return pii[-8:] if pii else 'article'

def record_year(record):
    for key in ('year', 'publicationYear', 'coverYear'):
        v = str(record.get(key, '') or '').strip()
        if re.fullmatch(r'\d{4}', v): return v
    return '2024'

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

def download_pdf(url, dest):
    """Download PDF from URL to destination."""
    req = urllib.request.Request(url, headers={'User-Agent': f'Mozilla/5.0 {UA}'})
    tmp = dest.with_suffix('.part')
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            content = resp.read()
        # Verify it's actually a PDF
        if content[:4] == b'%PDF':
            dest.write_bytes(content)
            if tmp.exists():
                tmp.unlink()
            return True
        else:
            print(f'    Not a PDF (header: {content[:20]})')
            return False
    except Exception as e:
        print(f'    Error: {e}')
        if tmp.exists():
            tmp.unlink()
        return False

def check_unpaywall(doi):
    """Check Unpaywall for OA PDF URL."""
    try:
        url = f'https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={UNPAYWALL_EMAIL}'
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8', errors='replace'))
        
        if data.get('is_oa', False):
            best = data.get('best_oa_location', {})
            pdf_url = best.get('url_for_pdf', '')
            host = best.get('host_type', '')
            return pdf_url, host
        return '', ''
    except Exception:
        return '', ''

def generate_scihub_urls(doi):
    """Generate list of Sci-Hub URLs to try."""
    return [f'https://{domain}/{doi}' for domain in SCI_HUB_DOMAINS] + \
           [f'https://{domain}/https://doi.org/{doi}' for domain in SCI_HUB_DOMAINS]

def main():
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    
    meta = json.loads(META.read_text('utf-8'))
    
    # Collect articles with mechanisms
    articles = []
    for r in meta:
        if r.get('processingStatus') not in ('included', 'conversion_failed'):
            continue
        doi = r.get('doi', '')
        if not doi:
            continue
        year = r.get('year', '')
        articles.append(r)
    
    # Check which already have PDFs
    need_pdf = []
    have_pdf = []
    for r in articles:
        pdf_name = os.path.basename(get_pdf_filename(r))
        # Check in the article folder AND the pdfs directory
        folder = r.get('processingFolder', '')
        found = False
        if folder:
            pdf_path = Path(folder) / pdf_name
            if pdf_path.exists() and pdf_path.stat().st_size > 100:
                have_pdf.append(r)
                found = True
        if not found:
            pdf_path = PDF_DIR / pdf_name
            if pdf_path.exists() and pdf_path.stat().st_size > 100:
                have_pdf.append(r)
                found = True
        if not found:
            need_pdf.append(r)
    
    print(f'Articles with mechanisms: {len(articles)}')
    print(f'Already have PDF: {len(have_pdf)}')
    print(f'Need PDF: {len(need_pdf)}')
    
    oa_downloaded = 0
    scihub_downloaded = 0
    manual_needed = []
    
    for i, r in enumerate(need_pdf):
        doi = r['doi']
        year = r.get('year', '')
        title = (r.get('title', '') or '')[:50]
        folder = r.get('processingFolder', '')
        
        pdf_name = get_pdf_filename(r)
        pdf_path = Path(folder) / pdf_name if folder else PDF_DIR / pdf_name
        
        print(f'\n[{i+1}/{len(need_pdf)}] [{year}] {title}...')
        
        # 1. Try Unpaywall for OA
        try:
            oa_url, oa_host = check_unpaywall(doi)
            if oa_url:
                print(f'  OA found at {oa_host}: {oa_url[:80]}')
                if download_pdf(oa_url, pdf_path):
                    r['paperPdfLocal'] = str(pdf_path)
                    r['paperPdfSource'] = f'unpaywall-{oa_host}'
                    oa_downloaded += 1
                    print(f'  Downloaded ({pdf_path.stat().st_size} bytes)')
                    time.sleep(1)
                    continue
        except Exception:
            pass
        
        # 2. For pre-2021, try Sci-Hub
        if int(year) if year.isdigit() else 0 >= 2021 or year == '2021':
            manual_needed.append(r)
            print(f'  Post-2021, not OA. Manual download needed.')
            continue
        
        scihub_worked = False
        for url in generate_scihub_urls(doi):
            try:
                print(f'  Trying Sci-Hub: {url[:60]}...', end=' ', flush=True)
                req = urllib.request.Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
                    'Accept': 'text/html,application/xhtml+xml'
                })
                with urllib.request.urlopen(req, timeout=20) as resp:
                    html = resp.read().decode('utf-8', errors='replace')
                
                # Look for PDF URL in page
                pdf_url = None
                # Pattern 1: embed/iframe with .pdf
                match = re.search(r'(?:src|href)=["\']([^"\']*?\.pdf[^"\']*?)["\']', html, re.I)
                if match:
                    pdf_url = match.group(1)
                    if pdf_url.startswith('/'):
                        # Relative URL, prepend domain
                        parsed = urllib.parse.urlparse(url)
                        pdf_url = f'{parsed.scheme}://{parsed.netloc}{pdf_url}'
                    elif pdf_url.startswith('//'):
                        pdf_url = f'https:{pdf_url}'
                
                # Pattern 2: direct button link
                if not pdf_url:
                    match = re.search(r'<button[^>]*onclick=["\']location\.href\s*=\s*["\']([^"\']+)["\']', html)
                    if match:
                        pdf_url = match.group(1)
                
                if pdf_url:
                    print(f'PDF found', end=' ', flush=True)
                    if download_pdf(pdf_url, pdf_path):
                        r['paperPdfLocal'] = str(pdf_path)
                        r['paperPdfSource'] = 'sci-hub'
                        scihub_worked = True
                        scihub_downloaded += 1
                        print(f'OK ({pdf_path.stat().st_size} bytes)')
                        break
                    else:
                        print('download failed')
                else:
                    # Check for captcha
                    if 'проверка' in html or 'captcha' in html.lower() or 'robot' in html.lower():
                        print('CAPTCHA')
                        break
                    print('no PDF found')
            except urllib.error.HTTPError as e:
                print(f'HTTP {e.code}')
                continue
            except Exception as e:
                print(f'Error: {e}')
                continue
        
        if not scihub_worked:
            manual_needed.append(r)
        
        time.sleep(2)  # Be gentle to Sci-Hub
    
    # Save metadata
    META.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    
    print(f'\n\n=== Summary ===')
    print(f'Already had PDF: {len(have_pdf)}')
    print(f'Downloaded via OA: {oa_downloaded}')
    print(f'Downloaded via Sci-Hub: {scihub_downloaded}')
    print(f'Need manual: {len(manual_needed)}')
    
    if manual_needed:
        manual_path = ROOT / 'manual_download_handoff.md'
        existing = manual_path.read_text() if manual_path.exists() else ''
        with manual_path.open('a') as f:
            f.write('\n## PDFs needed (manual Sci-Hub or ScienceDirect)\n\n')
            for r in manual_needed:
                doi = r['doi']
                year = r.get('year', '')
                title = r.get('title', '')[:80]
                folder = r.get('processingFolder', '')
                f.write(f"### {title}\n")
                f.write(f"- DOI: {doi}\n")
                f.write(f"- Year: {year}\n")
                f.write(f"- Sci-Hub: https://sci-hub.ru/{doi}\n")
                f.write(f"- ScienceDirect: {r.get('url', '')}\n")
                f.write(f"- Target: {folder}/{os.path.basename(get_pdf_filename(r))}\n\n")
        print(f'Manual list appended to manual_download_handoff.md')

if __name__ == '__main__':
    main()

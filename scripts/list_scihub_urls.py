#!/usr/bin/env python3
"""
Generate Sci-Hub URLs for manual PDF download.
After solving captcha and downloading PDFs to the right folder, re-run to verify.
"""
import json, os, re
from pathlib import Path

REPO = Path(os.environ.get('MECH_COLLECTION_WORKSPACE', Path(__file__).resolve().parents[1]))
META = REPO / 'combustion_and_flame_mechanisms' / '_raw' / 'article_metadata.json'
ROOT = Path(os.environ.get('MECH_COLLECTION_ROOT', REPO / 'combustion_and_flame_mechanisms'))

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

def main():
    meta = json.loads(META.read_text('utf-8'))
    
    articles = []
    for r in meta:
        if r.get('processingStatus') not in ('included', 'conversion_failed'):
            continue
        articles.append(r)
    
    need = []
    have = []
    for r in articles:
        pdf_name = get_pdf_filename(r)
        folder = r.get('processingFolder', '')
        found = False
        if folder:
            pdf_path = Path(folder) / pdf_name
            if pdf_path.exists() and pdf_path.stat().st_size > 1000:
                found = True
        if not found:
            pdf_path = ROOT / '_raw' / 'pdfs' / pdf_name
            if pdf_path.exists() and pdf_path.stat().st_size > 1000:
                found = True
        if found:
            have.append(r)
        else:
            need.append(r)
    
    print(f'Articles: {len(articles)} | Have PDF: {len(have)} | Need: {len(need)}')
    print()
    
    if need:
        print(f'=== Sci-Hub URLs for {len(need)} articles ===')
        print()
        for i, r in enumerate(need):
            doi = r['doi']
            year = r.get('year', '')
            title = r.get('title', '')[:80]
            pdf_name = get_pdf_filename(r)
            folder = r.get('processingFolder', '')
            target = (Path(folder) / pdf_name) if folder else (ROOT / '_raw' / 'pdfs' / pdf_name)
            
            print(f'{i+1}. {title}')
            print(f'   Sci-Hub: https://sci-hub.ru/{doi}')
            print(f'   Save as: {target.name}')
            print(f'   In folder: {target.parent}')
            print()

if __name__ == '__main__':
    main()

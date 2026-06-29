#!/usr/bin/env python3
"""Recover missing mechanism files from raw_downloads and fix mislabeled papers."""
import sys, json, re, shutil, subprocess, zipfile, tarfile, gzip, tempfile
from pathlib import Path
from collections import defaultdict

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import read_metadata, write_metadata, article_id

ROOT = REPO / 'combustion_and_flame_mechanisms'
records = read_metadata()

# Build aid → record map
aid_to_record = {}
for r in records:
    aid = article_id(r)
    aid_to_record[aid] = r

# Scan disk for all mechanism folders
folders_fixed = 0
re_extracted = 0
re_converted = 0
status_fixed = 0

CHEMKIN_EXTS = {'.inp', '.dat', '.txt', '.ck', '.chm', '.che', '.ski', '.mech'}
MECH_KEYWORDS = [b'ELEMENTS', b'SPECIES', b'REACTIONS', b'THERMO', b'END']

def looks_like_chemkin(filepath):
    """Check if file content looks like CHEMKIN."""
    try:
        with open(filepath, 'rb') as f:
            head = f.read(4096)
        return any(kw in head.upper() for kw in MECH_KEYWORDS)
    except:
        return False

def extract_archives(raw_dir, dest_dir):
    """Extract all zip/tar/gz archives from raw_dir to dest_dir."""
    extracted = []
    for f in sorted(raw_dir.iterdir()):
        if f.suffix.lower() == '.zip':
            try:
                with zipfile.ZipFile(f) as zf:
                    zf.extractall(dest_dir)
                extracted.append(f.name)
            except: pass
        elif f.suffix.lower() in ('.tar', '.gz', '.tgz'):
            try:
                if f.suffix == '.gz':
                    with gzip.open(f) as gf:
                        out = dest_dir / f.stem
                        out.write_bytes(gf.read())
                extracted.append(f.name)
            except: pass
    return extracted

def find_chemkin_files(folder):
    """Find CHEMKIN files in folder recursively, excluding _processing."""
    mech_files = []
    for f in folder.rglob('*'):
        if '_processing' in f.parts or '__pycache__' in f.parts:
            continue
        if not f.is_file(): continue
        if f.suffix.lower() in CHEMKIN_EXTS and looks_like_chemkin(f):
            mech_files.append(f)
        elif f.suffix.lower() == '' and looks_like_chemkin(f):  # no extension
            mech_files.append(f)
    return mech_files

def re_extract_mechanism(record, aid):
    """Re-extract mechanism from raw_downloads."""
    # Find the folder on disk
    for folder in ROOT.glob(f'**/{aid}'):
        if folder.is_dir():
            break
    else:
        return None, "folder not found"
    
    raw = folder / '_processing' / 'raw_downloads'
    if not raw.exists():
        return None, "no raw_downloads"
    
    extracted_dir = folder / '_processing' / 'extracted'
    extracted_dir.mkdir(parents=True, exist_ok=True)
    
    # Extract all archives
    archives = extract_archives(raw, extracted_dir)
    if not archives:
        return None, "no archives to extract"
    
    # Find CHEMKIN files in extracted content
    mech_files = find_chemkin_files(extracted_dir)
    if not mech_files:
        # Also check raw text files
        for f in raw.iterdir():
            if f.suffix.lower() in ('.txt', '') and looks_like_chemkin(f):
                dest = folder / f.name
                shutil.copy2(f, dest)
                mech_files.append(dest)
    
    # Identify chem.inp, therm.dat, tran.dat
    chem_inp = None
    therm_dat = None
    tran_dat = None
    
    for mf in mech_files:
        content = mf.read_bytes()[:4096].upper()
        if b'ELEMENTS' in content or b'SPECIES' in content:
            if not chem_inp or mf.stat().st_size > (chem_inp.stat().st_size if chem_inp else 0):
                chem_inp = mf
        if b'THERMO' in content or b'THERM' in content:
            if not therm_dat:
                therm_dat = mf
        if b'TRANSPORT' in content or b'AREA' in content:
            if not tran_dat:
                tran_dat = mf
    
    if not chem_inp:
        return None, f"no CHEMKIN files found among {len(mech_files)} candidates"
    
    # Copy/link to standard names
    if chem_inp and not (folder / 'chem.inp').exists():
        shutil.copy2(chem_inp, folder / 'chem.inp')
    if therm_dat and not (folder / 'therm.dat').exists():
        shutil.copy2(therm_dat, folder / 'therm.dat')
    if tran_dat and not (folder / 'tran.dat').exists():
        shutil.copy2(tran_dat, folder / 'tran.dat')
    
    return folder, f"restored: chem.inp={chem_inp is not None}, therm={therm_dat is not None}, tran={tran_dat is not None}"


# Phase 1: Fix mislabeled papers (status=mech but no mechanism possible)
print('=== Phase 1: Fix mislabeled papers ===')
for r in records:
    if r.get('processingStatus') not in ('included', 'conversion_failed'):
        continue
    aid = article_id(r)
    
    # Find folder
    for folder in ROOT.glob(f'**/{aid}'):
        if folder.is_dir():
            break
    else:
        continue
    
    raw = folder / '_processing' / 'raw_downloads'
    if not raw.exists() or not any(raw.iterdir()):
        continue
    
    # Check if all supplements are non-CHEMKIN (PDF, DOCX, XLSX only)
    has_archive = any(f.suffix.lower() in ('.zip','.tar','.gz') for f in raw.iterdir())
    has_text = any(f.suffix.lower() in ('.txt','.inp','.dat','') for f in raw.iterdir())
    
    if not has_archive and not has_text:
        # Only PDF/DOCX/XLSX — not a mechanism paper
        if not (folder / 'chem.inp').exists():
            r['processingStatus'] = 'excluded_no_mechanism_attachment'
            r['fuelType'] = 'unknown_fuel'
            status_fixed += 1
            if status_fixed <= 5:
                print(f'  Fixed: {str(r.get("title",""))[:50]}')

write_metadata(records)
print(f'  Status fixed: {status_fixed}')

# Phase 2: Re-extract from raw_downloads for papers missing chem.inp
print(f'\n=== Phase 2: Re-extract missing mechanisms ===')
for r in records:
    if r.get('processingStatus') not in ('included', 'conversion_failed'):
        continue
    aid = article_id(r)
    
    # Find folder
    for folder in ROOT.glob(f'**/{aid}'):
        if folder.is_dir():
            break
    else:
        continue
    
    if (folder / 'chem.inp').exists() and (folder / 'therm.dat').exists():
        continue  # Already has core files
    
    raw = folder / '_processing' / 'raw_downloads'
    if not raw.exists() or not any(raw.iterdir()):
        continue
    
    result, msg = re_extract_mechanism(r, aid)
    if result:
        re_extracted += 1
        if re_extracted <= 5:
            print(f'  Recovered: {folder.relative_to(ROOT)}')
            print(f'    {msg}')
    elif re_extracted < 5:
        print(f'  Failed: {folder.relative_to(ROOT)[:60]}: {msg}')

write_metadata(records)
print(f'  Re-extracted: {re_extracted}')

# Summary
print(f'\n=== Recovery Summary ===')
print(f'  Status fixed: {status_fixed}')
print(f'  Re-extracted: {re_extracted}')
# Check remaining issues
for r in records:
    if r.get('processingStatus') not in ('included', 'conversion_failed'):
        continue
    aid = article_id(r)
    for folder in ROOT.glob(f'**/{aid}'):
        if folder.is_dir():
            chem = (folder/'chem.inp').exists()
            therm = (folder/'therm.dat').exists()
            if not chem:
                re_extracted
    break

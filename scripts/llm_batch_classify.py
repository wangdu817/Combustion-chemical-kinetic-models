#!/usr/bin/env python3
"""Batch LLM fuel classification for unknown_fuel papers.
Reads llm_fuel_prompts.json, classifies each paper via LLM API,
writes results and updates metadata.
"""
import json, sys, os, urllib.request, time
from pathlib import Path

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))

# Load prompts
prompts = json.loads((REPO / 'llm_fuel_prompts.json').read_text('utf-8'))
print(f'Papers to classify: {len(prompts)}')

API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')
API_BASE = os.environ.get('DEEPSEEK_BASE_URL', 'https://api.deepseek.com')

if not API_KEY:
    print('ERROR: DEEPSEEK_API_KEY not set')
    sys.exit(1)

results = []
for i, p in enumerate(prompts):
    title = p['title']
    abstract = p['abstract'][:3000]
    
    prompt_text = f"""Paper title: {title}

Abstract: {abstract}

List ALL specific fuel compounds or fuel classes mentioned in this combustion chemistry paper.
Use standard chemical names: methane, ethane, propane, n-heptane, iso-octane, ethylene, acetylene, benzene, toluene, methanol, ethanol, dimethyl ether, ammonia, hydrogen, syngas, silane, RDX, CL-20, JP-10, jet fuel, gasoline, diesel, naphtha, surrogate, ester, aldehyde, ketone, furan, etc.

Output ONLY a JSON array: ["fuel1", "fuel2", ...]
If no specific fuel is identifiable, output: []"""

    payload = {
        'model': 'deepseek-chat',
        'messages': [
            {'role': 'system', 'content': 'You are a combustion chemistry expert. Identify fuel compounds precisely. Output ONLY valid JSON arrays.'},
            {'role': 'user', 'content': prompt_text},
        ],
        'temperature': 0,
        'max_tokens': 200,
    }
    
    try:
        req = urllib.request.Request(
            f'{API_BASE}/v1/chat/completions',
            data=json.dumps(payload).encode(),
            headers={
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json',
            }
        )
        resp = urllib.request.urlopen(req, timeout=30)
        data = json.loads(resp.read())
        content = data['choices'][0]['message']['content'].strip()
        
        # Extract JSON array
        import re
        match = re.search(r'\[.*?\]', content, re.DOTALL)
        fuels = json.loads(match.group(0)) if match else []
        
        results.append({**p, 'fuels_found': fuels})
        print(f'  [{i+1}/{len(prompts)}] {title[:60]}')
        print(f'    fuels: {fuels}')
    except Exception as e:
        print(f'  [{i+1}/{len(prompts)}] ERROR: {e}')
        results.append({**p, 'fuels_found': [], 'error': str(e)})
    
    time.sleep(0.5)  # rate limit

# Save results
out = REPO / 'llm_fuel_results.json'
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'\nResults saved to {out}')

# Now update metadata with found fuels
from collect_cf2026 import read_metadata, write_metadata, detect_fuel
records = read_metadata()
pii_map = {r.get('pii',''): r for r in records}

classified = 0
for r in results:
    if not r.get('fuels_found'):
        continue
    pii = r.get('pii', '')
    rec = pii_map.get(pii)
    if not rec:
        continue
    
    # Add found fuels to record as keywords for detect_fuel
    old_keywords = rec.get('keywords', '')
    fuel_keywords = ', '.join(r['fuels_found'])
    rec['keywords'] = old_keywords + (', ' if old_keywords else '') + fuel_keywords
    
    new_fuel = detect_fuel(rec)
    if new_fuel != 'unknown_fuel':
        rec['fuelType'] = new_fuel
        classified += 1
        print(f'  Classified: {new_fuel} <- {r["title"][:50]}')

if classified:
    write_metadata(records)
    print(f'\nClassified: {classified} papers')
    print('Re-run: python scripts/reclassify_fuel.py')

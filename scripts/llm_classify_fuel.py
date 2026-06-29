#!/usr/bin/env python3
"""LLM-based fuel classification for unknown_fuel papers.
Uses the existing LLM provider to identify fuel compounds from title+abstract.
"""
import sys, json, re
from pathlib import Path

REPO = Path('/home/icaurs/Combustion-chemical-kinetic-models')
sys.path.insert(0, str(REPO / 'scripts'))
from collect_cf2026 import read_metadata, write_metadata, detect_fuel, normalize_abstract

ROOT = REPO / 'combustion_and_flame_mechanisms'
records = read_metadata()

# Find unknown_fuel mechanism papers
unknown = [r for r in records if r.get('fuelType') == 'unknown_fuel'
           and r.get('processingStatus') in ('included', 'conversion_failed')]
print(f'Unknown fuel papers: {len(unknown)}')

# Build prompt examples
SYSTEM_PROMPT = """You are a combustion chemistry expert. Given a paper title and abstract, identify ALL specific fuel compounds or fuel classes mentioned. Output ONLY valid JSON: {"fuels": ["fuel1", "fuel2", ...]}. Use standard chemical names (methane, ethanol, n-heptane, ammonia, dimethyl ether, etc.). If no specific fuel is identifiable, output {"fuels": []}."""

# For each paper, prepare the prompt
papers_to_classify = []
for r in unknown:
    title = str(r.get('title', ''))
    abstract = normalize_abstract(r.get('abstract', ''))
    doi = r.get('doi', '')
    if not abstract:
        continue  # skip papers without abstracts
    papers_to_classify.append({
        'pii': r.get('pii', ''),
        'doi': doi,
        'title': title,
        'abstract': abstract[:3000],
        'record': r,
    })

print(f'Papers with abstracts (classifiable): {len(papers_to_classify)}')
print(f'Papers without abstracts (skip): {len(unknown) - len(papers_to_classify)}')

# Save prompts for batch processing
prompts_file = REPO / 'llm_fuel_prompts.json'
prompts_data = [{
    'pii': p['pii'],
    'doi': p['doi'],
    'title': p['title'],
    'abstract': p['abstract'],
} for p in papers_to_classify]
prompts_file.write_text(json.dumps(prompts_data, ensure_ascii=False, indent=2), encoding='utf-8')

print(f'\nSaved {len(prompts_data)} prompts to {prompts_file}')
print()
print('Sample prompt:')
sample = prompts_data[0]
print(f'  System: {SYSTEM_PROMPT[:80]}...')
print('  User: Title: ' + sample['title'][:80])
print('        Abstract: ' + sample['abstract'][:120] + '...')

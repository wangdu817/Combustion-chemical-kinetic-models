#!/usr/bin/env python3
"""
Fetch all 2022 C&F articles from Crossref using curl for reliability.
Saves raw responses then processes into volume JSONs.
"""
import json, subprocess, sys, time
from pathlib import Path

ROOT = Path("/home/ubuntu/Combustion-chemical-kinetic-models/combustion_and_flame_mechanisms")
OUTDIR = ROOT / "_raw" / "2022_volumes"
OUTDIR.mkdir(parents=True, exist_ok=True)
CACHEDIR = ROOT / "_raw" / "2022_cache"
CACHEDIR.mkdir(parents=True, exist_ok=True)

ISSN = "0010-2180"
ROWS = 50

all_articles = []
cursor = "*"
page = 0

while page < 30:
    page += 1
    cache_file = CACHEDIR / f"page_{page:03d}.json"
    
    # Use cached response if available
    if cache_file.exists():
        data = json.loads(cache_file.read_text())
        print(f"Page {page}: from cache", flush=True)
    else:
        from urllib.parse import quote
        url = (f"https://api.crossref.org/works?"
               f"filter=issn:{ISSN},from-pub-date:2022-01-01,until-pub-date:2022-12-31"
               f"&rows={ROWS}&cursor={quote(cursor, safe='*')}"
               f"&sort=published&order=asc")
        
        print(f"Page {page}: fetching...", end=" ", flush=True)
        
        for attempt in range(3):
            try:
                result = subprocess.run(
                    ["curl", "-s", "-m", "120", "-o", str(cache_file), url],
                    capture_output=True, text=True, timeout=130
                )
                if cache_file.stat().st_size > 100:
                    data = json.loads(cache_file.read_text())
                    break
                else:
                    print(f"(empty, retry {attempt+1})", end=" ", flush=True)
                    time.sleep(2)
            except Exception as e:
                print(f"(err: {e}, retry {attempt+1})", end=" ", flush=True)
                time.sleep(2)
        else:
            print("FAILED", flush=True)
            break
    
    msg = data.get("message", {})
    items = msg.get("items", [])
    total = msg.get("total-results", 0)
    next_cursor = msg.get("next-cursor", "")
    
    all_articles.extend(items)
    print(f"{len(items)} items (total: {len(all_articles)}/{total})", flush=True)
    
    if not next_cursor or len(items) == 0:
        print("No more pages.", flush=True)
        break
    cursor = next_cursor
    time.sleep(0.3)

print(f"\nDownloaded {len(all_articles)} articles in {page} pages", flush=True)

# Group by volume
by_volume = {}
for item in all_articles:
    vol = str(item.get("volume", "unknown"))
    by_volume.setdefault(vol, []).append(item)

for vol in sorted(by_volume.keys()):
    articles = []
    for item in by_volume[vol]:
        pub = item.get("published-print") or item.get("published-online") or {}
        dp = pub.get("date-parts", [[None, None]])[0]
        articles.append({
            "year": dp[0] or 2022,
            "volume": vol,
            "month": dp[1],
            "title": (item.get("title") or [""])[0] or "",
            "authors": [f"{a.get('given','')} {a.get('family','')}".strip() 
                       for a in item.get("author", [])],
            "doi": item.get("DOI", ""),
            "pii": "",
            "articleNumber": item.get("article-number", ""),
            "url": f"https://doi.org/{item.get('DOI','')}" if item.get("DOI") else "",
            "issuePdfLink": "",
        })
    
    outpath = OUTDIR / f"volume_{vol}.json"
    outpath.write_text(json.dumps(articles, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved volume_{vol}.json: {len(articles)} articles", flush=True)

print(f"\nDone: {len(by_volume)} volumes", flush=True)

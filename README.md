# Combustion and Flame 2026 Mechanism Collection

This repository contains the automation script and lightweight metadata for the
Combustion and Flame 2026 reaction-mechanism supplement collection.

Large downloaded supplements, extracted mechanism payloads, and `ckinterp`
outputs are intentionally ignored by Git. They remain in the local workspace
under `combustion_and_flame_2026_mechanisms/`.

Main entry points:

- `scripts/collect_cf2026.py`: collection post-processing and metadata tooling.
- `combustion_and_flame_2026_mechanisms/collection_index.csv`: collection index.
- `combustion_and_flame_2026_mechanisms/manual_download_handoff.md`: manual download queue.
- `combustion_and_flame_2026_mechanisms/_raw/article_metadata.json`: harvested article metadata.

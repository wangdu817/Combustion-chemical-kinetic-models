# Combustion and Flame Mechanism Collection

This repository contains the automation script and lightweight metadata for the
Combustion and Flame reaction-mechanism supplement collection.


Main entry points:

- `scripts/collect_cf2026.py`: collection post-processing and metadata tooling.
- `requirements.txt` / `environment.yml`: Python dependency definitions for pip or Conda.
- `combustion_and_flame_mechanisms/collection_index.csv`: collection index.
- `combustion_and_flame_mechanisms/manual_download_handoff.md`: manual download queue.
- `combustion_and_flame_mechanisms/_raw/article_metadata.json`: harvested article metadata and resumable per-article state.
- `docs/reproduce_mechanism_collection.md`: cross-platform workflow, package requirements, manual browser handoff points, and optional agent-assisted steps.

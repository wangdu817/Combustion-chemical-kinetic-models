# Combustion and Flame Mechanism Collection

Reaction mechanism supplementary files from *Combustion and Flame* and *Proceedings of the Combustion Institute*,
collected, extracted, and validated with Cantera.

## Collection Statistics

| Category | Papers | Description |
|----------|--------|-------------|
| Hydrocarbon | 304 | Alkanes, alkenes, aromatics, cycloalkanes |
| Oxygenated | 195 | Alcohols, ethers, esters, ketones, aldehydes, furans |
| Nitrogen-containing | 143 | Ammonia, NOx, amines, nitriles, energetic materials |
| Surrogate / Practical | 72 | Gasoline, diesel, jet fuel, naphtha, RP-3, SAF, biofuel, PRF/TRF |
| Metal | 10 | Iron, aluminum, magnesium, silane |
| Fluorine | 1 | Refrigerants (R32, HCFO) |
| **Total** | **725** | |

### Per-Year Mechanism Counts

| Year | Mechanisms | Year | Mechanisms |
|------|-----------|------|-----------|
| 2009 | 12 | 2018 | 14 |
| 2010 | 2 | 2019 | 38 |
| 2011 | 14 | 2020 | 24 |
| 2012 | 13 | 2021 | 60 |
| 2013 | 21 | 2022 | 56 |
| 2014 | 16 | 2023 | 86 |
| 2015 | 42 | 2024 | 67 |
| 2016 | 24 | 2025 | 73 |
| 2017 | 31 | 2026 | 46 |

## Repository Structure

```
combustion_and_flame_mechanisms/
├── hydrocarbon/         # 304 mechanisms
│   └── {fuel}/{year}/{author}_{year}_{fuel}_{id}/
│       ├── chem.inp, therm.dat, tran.dat
│       ├── mechanism.yaml
│       └── mechanism_summary.md
├── oxygenated/          # 195 mechanisms
├── nitrogen/            # 143 mechanisms
├── surrogate/           # 72 mechanisms
├── metal/               # 10 mechanisms
├── fluorine/            # 1 mechanism
├── _raw/                # article metadata, volume JSONs, downloads
├── candidate_index.json # full candidate inventory (2082 entries)
└── year_fuel_index.json # per-year category statistics
```

Each mechanism folder contains:
- `chem.inp` — CHEMKIN-format reaction mechanism
- `therm.dat` — thermodynamic data
- `tran.dat` — transport data (when available)
- `mechanism.yaml` — Cantera-converted YAML
- `mechanism_summary.md` — paper metadata and processing notes

## Index Files

- **candidate_index.json** — All 2082 candidate articles with year, DOI, title, processing status, fuel type, element category, and disk paths
- **year_fuel_index.json** — Per-year statistics by fuel category

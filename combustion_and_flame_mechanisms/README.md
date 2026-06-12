# Combustion and Flame mechanism collection

This collection is organized for user lookup by fuel type first:

```text
combustion_and_flame_mechanisms/
  fuel_type/
    year/
      firstauthorsurname_year_fueltype_articlenumber/
        mechanism_summary.md
        chem.inp
        therm.dat
        tran.dat
        mechanism.yaml
        _processing/
```

Visible paper folders keep the summary and standardized mechanism files at the top level. Raw downloads, recursive extraction outputs, conversion logs, and other processing artifacts are stored in each paper folder's `_processing/` subfolder.

Machine-readable collection-level files:

- `collection_index.csv`: article-level index and mechanism processing status.
- `manual_download_handoff.md`: items that still need manual PDF or attachment access.
- `_raw/article_metadata.json`: harvested article metadata plus resumable probe, download, and processing state.

The processing script is designed for endpoint continuation. By default it reuses terminal per-article states and existing paper folders instead of repeating web access, downloads, recursive extraction, or Cantera preprocessing. Use `--force` only when a specific step needs to be rerun.

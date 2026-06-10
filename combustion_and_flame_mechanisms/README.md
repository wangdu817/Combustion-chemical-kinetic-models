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
```

Visible paper folders are kept intentionally small. They contain the summary and standardized mechanism files only. Raw downloads, recursive extraction outputs, conversion logs, and other processing artifacts are stored under `_processing_archive/`.

Machine-readable collection-level files:

- `collection_index.csv`: article-level index and mechanism processing status.
- `manual_download_handoff.md`: items that still need manual PDF or attachment access.
- `_raw/article_metadata.json`: harvested article metadata used by the processing script.

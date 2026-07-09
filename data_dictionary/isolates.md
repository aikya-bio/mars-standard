# Data Dictionary: harmonised.isolates

One row per clinical isolate.

| Field | Type | Status | Description |
|---|---|---|---|
| `isolate_id` | TEXT | Mandatory | Unique ID within source dataset |
| `source_dataset` | TEXT | Mandatory | MARS dataset registry ID |
| `loaded_at` | TIMESTAMPTZ | Mandatory | UTC timestamp of data load |
| `ncbi_taxonomy_id` | INTEGER | Mandatory | NCBI Taxonomy ID for organism |
| `organism_name_standard` | TEXT | Mandatory | Cleaned binomial species name |
| `gram_type` | TEXT | Mandatory | Gram-negative / Gram-positive / Fungal / Mycobacteria / Unknown |
| `organism_group` | TEXT | Recommended | Enterobacterales / Non-fermenters / Streptococci / Candida / etc. |
| `country_iso` | CHAR(2) | Mandatory | ISO 3166-1 alpha-2 |
| `region_un_m49` | TEXT | Recommended | UN M49 region name |
| `year_collected` | SMALLINT | Mandatory | YYYY |
| `specimen_type` | TEXT | Recommended | Blood / Urine / Respiratory / Wound / Other / Unknown |
| `facility_type` | TEXT | Recommended | ICU / General Ward / Community / Unknown |
| `age_group` | TEXT | Recommended | 0–2 / 3–17 / 18–64 / 65+ / Unknown |
| `gender` | TEXT | Recommended | M / F / Unknown |
| `nosocomial` | BOOLEAN | Optional | Hospital-acquired vs community |
| `infection_type` | TEXT | Optional | BSI / UTI / Pneumonia / Wound / IAI / Unknown |
| `subtype` | TEXT | Optional | MDR / XDR / Pre-XDR / MRSA / VRSA |
| `has_genotype_data` | BOOLEAN | Mandatory | TRUE if genotype_observations rows exist |
| `metadata` | JSONB | Optional | Non-standard fields, queryable overflow |

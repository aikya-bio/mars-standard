# Data Dictionary: harmonised.mic_observations

One row per drug tested per isolate. An isolate tested against 20 drugs produces 20 rows.

| Field | Type | Status | Description |
|---|---|---|---|
| `isolate_id` | TEXT | Mandatory | Foreign key to isolates |
| `source_dataset` | TEXT | Mandatory | MARS dataset registry ID |
| `chembl_id` | TEXT | Mandatory | ChEMBL compound identifier |
| `drug_name_standard` | TEXT | Mandatory | ChEMBL preferred name |
| `drug_class` | TEXT | Recommended | Beta-lactam / Fluoroquinolone / Aminoglycoside / etc. |
| `aware_category` | TEXT | Recommended | Access / Watch / Reserve / Unknown |
| `mic_numeric` | DECIMAL | Mandatory | Normalised MIC value |
| `mic_qualifier` | TEXT | Mandatory | = / > / < / >= / <= |
| `interpretation_raw` | TEXT | Optional | Original S/I/R as in source data |
| `interpretation_standard` | TEXT | Recommended | S / I / R / Unknown |
| `breakpoint_system` | TEXT | Recommended | CLSI / EUCAST / Unknown |
| `breakpoint_version` | TEXT | Optional | e.g. EUCAST 2023, CLSI 2022 |

# Data Dictionary: harmonised.isolates

One row per clinical isolate.

| Field | Type | Status | Description |
|---|---|---|---|
| `isolate_id` | TEXT | Mandatory | Unique ID within source dataset |
| `source_dataset` | TEXT | Mandatory | Identifier of the source dataset (free text, e.g. `Demo-Dataset-2026`) |
| `loaded_at` | TIMESTAMPTZ | Mandatory | UTC timestamp of data load |
| `ncbi_taxonomy_id` | INTEGER | Mandatory | NCBI Taxonomy ID for organism |
| `organism_name_standard` | TEXT | Mandatory | Cleaned binomial species name |
| `gram_type` | TEXT | Mandatory | Gram-negative / Gram-positive / Fungal / Mycobacteria / Unknown |
| `organism_group` | TEXT | Recommended | Enterobacterales / Non-fermenters / Streptococci / Staphylococci / Enterococci / Candida / Other / Unknown |
| `country_iso` | CHAR(2) | Mandatory | ISO 3166-1 alpha-2 |
| `region_un_m49` | TEXT | Recommended | UN M49 region name |
| `year_collected` | SMALLINT | Mandatory | YYYY |
| `specimen_type` | TEXT | Recommended | Blood / Urine / Respiratory / Wound / CSF / Skin/Soft Tissue / Intra-abdominal / Bone/Joint / Eye / Stool / Genital / Other / Unknown |
| `facility_type` | TEXT | Recommended | ICU / General Ward / Community / Outpatient / Long-term Care / Unknown |
| `age_group` | TEXT | Recommended | GLASS-aligned bands: `<1`, `1–4`, `5–14`, `15–24`, `25–34`, `35–44`, `45–54`, `55–64`, `65–74`, `75–84`, `85+`, or `Unknown`. Legacy bands (deprecated): `0–2`, `3–17`, `18–64`, `65+` |
| `gender` | TEXT | Recommended | M / F / O / Unknown |
| `nosocomial` | BOOLEAN | Optional | Hospital-acquired (TRUE) vs community-acquired (FALSE) |
| `infection_type` | TEXT | Optional | BSI / UTI / Pneumonia / Wound / IAI / HAP / SSTI / Other / Unknown |
| `subtype` | TEXT | Optional | MDR / XDR / Pre-XDR / MRSA / VRSA |
| `has_genotype_data` | BOOLEAN | Mandatory | TRUE if genotype_observations rows exist |
| `metadata` | JSONB | Optional | Non-standard fields, queryable overflow |
| `patient_key` | TEXT | Optional | Pseudonymous patient key (see Privacy and Identifier Guidelines below) |
| `specimen_type_raw` | TEXT | Optional | Original source specimen code or label verbatim (e.g. `LOWRESP`, `bl`). Source code/label only, never free-text clinical notes |
| `age_group_raw` | TEXT | Optional | Original source age group code or verbatim age string (e.g. `01<04`, `ped`, `42y`). Source code/label only, never free-text clinical notes |
| `infection_origin` | TEXT | Optional | Community / Hospital / Unknown |

## Infection Origin and Nosocomial Consistency Rule
`nosocomial` and `infection_origin` provide complementary representations of infection acquisition. When both `nosocomial` and `infection_origin` are present and `infection_origin` is not `Unknown`, they must agree:
- `infection_origin = 'Hospital'` <-> `nosocomial = true`
- `infection_origin = 'Community'` <-> `nosocomial = false`

When `infection_origin = 'Unknown'`, or when either field is null/omitted, no consistency conflict exists. This rule is enforced by a SQL CHECK constraint in PostgreSQL and SQLite, and via conditional (`if`/`then`) validation in the JSON schema.

## Age Scheme Note
MARS v0.4 aligns age groups with the 11 WHO GLASS age bands (`<1`, `1–4`, `5–14`, `15–24`, `25–34`, `35–44`, `45–54`, `55–64`, `65–74`, `75–84`, `85+`, plus `Unknown`), using typographic en-dashes (`–`, U+2013). Legacy v0.1–v0.3 age bands (`0–2`, `3–17`, `18–64`, `65+`) remain valid for backwards compatibility but are now deprecated (`deprecated = TRUE`).

A dataset should use one scheme throughout. Old and new bands overlap (for example `65+` vs `65–74`, `75–84`, `85+`), so mixed data cannot be summarised by band. No automatic old-to-new mapping is performed.

## Patient Key and Privacy Guidelines
`patient_key` is an optional pseudonymous patient key.
- Unique within `source_dataset` where the data have been deduplicated; a repeat value, if present, indicates the same patient.
- There is NO database UNIQUE constraint on `patient_key`.
- It must not be a direct identifier (no patient names, national identity numbers, or medical record numbers as-is).
- If derived from an underlying patient identifier, derive it with a keyed hash using a secret salt (for example HMAC-SHA256) held securely by the data owner.
- There is no episode key in MARS.
- MARS does not require `patient_key`.

## Raw Fields Guidelines
The `*_raw` fields (`specimen_type_raw`, `age_group_raw`, alongside `mic_raw` and `interpretation_raw`) capture the original source code or label verbatim to preserve provenance and auditability when mapping to MARS controlled vocabularies. These fields must contain only the source code or categorical label, never free-text clinical notes, narratives, or identifiable clinical commentary.

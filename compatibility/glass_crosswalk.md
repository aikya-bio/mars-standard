# WHO GLASS Compatibility

GLASS is an aggregate reporting system, while MARS operates at the isolate level. Data in MARS format can be aggregated to the counts GLASS requests; this table indicates how MARS fields relate to GLASS concepts. It is indicative, not a validated submission mapping.

| MARS Field | GLASS Concept | Notes |
|---|---|---|
| `organism_name_standard` | Target pathogen | Filter isolates based on GLASS priority pathogens. |
| `specimen_type` | Specimen source | Blood, Urine, Stool, Genital swabs are commonly requested by GLASS. |
| `drug_name_standard` | Target antibacterial | Aggregate counts per target drug. |
| `interpretation_standard` | S / I / R counts | Group by this field to generate the aggregate counts required by GLASS. |
| `gender`, `age_group` | Demographics | Used to segment aggregate reporting if required. |

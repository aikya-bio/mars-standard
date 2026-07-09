# hAMRonization Compatibility

Outputs from hAMRonization (a PHA4GE tool for standardising AMR prediction tool results) map directly into the MARS `genotype_observations` table.

| hAMRonization Output Field | MARS Field (`harmonised.genotype_observations`) | Notes |
|---|---|---|
| `gene_name` | `gene_name_standard` | |
| `reference_database_id` | `gene_aro_id` | Ensure the reference database used was CARD/ARO. |
| `type` | `phenotypic_class` | |

# PHA4GE Compatibility

MARS is explicitly designed to be compatible with PHA4GE minimal metadata conventions. A dataset that follows PHA4GE can be made MARS-compliant with minimal additional work.

| MARS Field | PHA4GE Equivalent | Notes |
|---|---|---|
| `ncbi_taxonomy_id` | `organism` (NCBI Taxonomy term) | PHA4GE uses ontology terms, MARS uses numeric IDs; both reference NCBI Taxonomy. |
| `country_iso` | `geo_loc_name_country` | PHA4GE uses country name, MARS uses ISO 3166 alpha-2. |
| `year_collected` | `collection_date` | PHA4GE captures full date, MARS requires year only. |
| `specimen_type` | `anatomical_material` + `body_product` | PHA4GE is more granular; MARS simplifies to controlled vocabulary. |
| `gene_aro_id` | `antimicrobial_resistance` (AMR gene) | Both reference ARO. |
| `hgvs_notation` | `genetic_characteristics` | Equivalent concept, different format. |

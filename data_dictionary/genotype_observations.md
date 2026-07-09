# Data Dictionary: harmonised.genotype_observations

One row per resistance gene per isolate. Only populated where gene-level data exists.

| Field | Type | Status | Description |
|---|---|---|---|
| `isolate_id` | TEXT | Mandatory | Foreign key to isolates |
| `source_dataset` | TEXT | Mandatory | MARS dataset registry ID |
| `gene_aro_id` | TEXT | Recommended | ARO identifier |
| `gene_name_standard` | TEXT | Recommended | Standard gene name from ARO |
| `phenotypic_class` | TEXT | Recommended | ESBL / MBL / Carbapenemase / Cephalosporinase |
| `betalactamase_status` | TEXT | Optional | POS / NEG / Unknown |
| `hgvs_notation` | TEXT | Optional | HGVS-formatted variant notation |
| `variant_type` | TEXT | Optional | nucleotide / amino_acid / Unknown |
| `raw_notation` | TEXT | Optional | Original notation from source dataset |

# hAMRonization Compatibility

Outputs from hAMRonization (a PHA4GE tool for standardising AMR gene detection and prediction results) map into the MARS `genotype_observations` and `isolates` tables.

> **Notice:** This crosswalk is indicative, not a validated mapping. Implementation teams should verify mapping rules against their specific workflow and pipeline outputs.

**Source reference:** hAMRonization specification v1.3.1 (repository `pha4ge/hAMRonization`, commit `ae54bb4`, 2026-08-10, `docs/hAMRonization_specification_details.csv`).

## Field Mapping Overview

| hAMRonization Field | MARS Target Field | Notes |
|---|---|---|
| `input_file_name` | `harmonised.isolates.isolate_id` / `harmonised.genotype_observations.isolate_id` | Primary join key linking genotypic predictions to the clinical isolate record. |
| `gene_symbol` | `harmonised.genotype_observations.gene_name_standard` | Short gene symbol (e.g. `catA1`, `blaOXA-101`). If `gene_symbol` is absent, fallback to `gene_name` (the long descriptive name, e.g. `type A-1 chloramphenicol O-acetyltransferase`). |
| `reference_accession` | `harmonised.genotype_observations.gene_aro_id` | Persistent accession of reference database entry. Map directly to `gene_aro_id` only when `reference_database_id` is CARD; for other databases (e.g. NCBI, ResFinder), map to CARD/ARO via an ARO lookup table and log the decision in `crosswalk_log`. |
| `genetic_variation_type` | `harmonised.genotype_observations.variant_type` | Controlled variation type defined in `hAMRonization/constants.py` (commit `ae54bb4`): `protein_variant_detected` maps to `amino_acid`; `nucleotide_variant_detected` maps to `nucleotide`; `gene_presence_detected` maps to `Unknown`. Note: earlier drafts claimed an output field named `type` existed; `type` is an input column in some upstream tools that hAMRonization parsers normalise and rename to `genetic_variation_type`. |
| `protein_mutation` / `nucleotide_mutation` | `harmonised.genotype_observations.hgvs_notation` | Sequence changes reported in standard HGVS format (e.g. `p.Ser450Leu` or `c.1349C>T`). Populated where variant-level mutations are detected. |
| *(no direct equivalent)* | `harmonised.genotype_observations.phenotypic_class` | hAMRonization v1.3.1 has no direct equivalent for `phenotypic_class`. The specification provides `drug_class` and `resistance_mechanism`, which are related biological concepts but not functionally equivalent; implementers may derive `phenotypic_class` via CARD ARO ontology lookups. |

## Notes on Schema Compatibility
All referenced MARS target fields (`isolate_id`, `gene_name_standard`, `gene_aro_id`, `variant_type`, `hgvs_notation`, and `phenotypic_class`) are verified to exist in the MARS v0.4 schema (`harmonised.genotype_observations` and `harmonised.isolates`).

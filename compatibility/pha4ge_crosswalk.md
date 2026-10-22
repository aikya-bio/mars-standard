# PHA4GE Compatibility

This document maps the fields that MARS has in common with the PHA4GE Minimal Pathogen Agnostic Contextual Data Specification. The mapping is indicative, not a validated mapping. It covers the overlapping fields only; the PHA4GE specification does not define AMR gene, sequence variant or susceptibility-result fields.

Source: Minimal Pathogen Agnostic Contextual Data Specification, PHA4GE Data Structures Working Group, github.com/pha4ge/minimal-pathogen-agnostic-contextual-data-specification, commit `0390611` (2023-05-03). One row also draws on the GRDI-AMR One Health Contextual Data Specification (github.com/cidgoh/GRDI_AMR_One_Health, commit `001f7fc`, reference guide v14.5.4), marked below.

| MARS Field | PHA4GE field (ontology ID) | Relation | Notes |
|---|---|---|---|
| `ncbi_taxonomy_id`, `organism_name_standard` | Organism (GENEPIO:0001191) | equivalent concept | The specification recommends an ontology such as NCBI Taxonomy and the species name. MARS stores the numeric NCBI Taxonomy ID and a cleaned binomial. |
| `country_iso` | geo_loc name (country) (GENEPIO:0001181) | equivalent concept | The specification uses permitted values from an ontology such as GAZ and states they are equivalent to ISO 3166-1. MARS stores ISO 3166-1 alpha-2. |
| `year_collected` | Sample collection date (GENEPIO:0001174) | related | The specification uses ISO 8601 (YYYY-MM-DD) and recommends day-level dates. MARS keeps the year only; derive it from the date. |
| `isolate_id` | Specimen collector sample ID (GENEPIO:0001123) | related | It identifies the sample, not the isolate; it can serve as the source of `isolate_id` only where each sample yields one isolate. The specification notes it can be PHI. |
| `patient_key` | Specimen source ID (GENEPIO:0100696) | related | Defined as the identifier of the host or environment the specimen came from (for example a case ID). The specification notes it can be PHI and suggests a hash ID for public-facing use; see the `patient_key` guidance in `data_dictionary/isolates.md`. |
| `specimen_type` | `anatomical_material` (GENEPIO:0001211) + `body_product` (GENEPIO:0001216), **from GRDI-AMR, not the PHA4GE minimal specification** | related | GRDI-AMR defines these as controlled-term fields with more granular terms; MARS uses a 13-value vocabulary. No value-level mapping is provided here, and the mapping is many_to_one. GRDI-AMR is a One Health specification (data streams across human health, agriculture, the environment and food), so its pick lists are not specific to human clinical specimens. |

## Not covered
The PHA4GE minimal specification and the GRDI-AMR field guide define no field for AMR gene identifiers or sequence variants (HGVS). For genotype data see `compatibility/hamronization_crosswalk.md`.

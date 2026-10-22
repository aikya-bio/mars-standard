# PHA4GE Compatibility

This document maps the fields that MARS has in common with the PHA4GE Minimal Pathogen Agnostic Contextual Data Specification. The mapping is indicative, not a validated mapping. It covers the overlapping fields only; the PHA4GE specification does not define AMR gene, sequence variant or susceptibility-result fields.

Source: Minimal Pathogen Agnostic Contextual Data Specification, PHA4GE Data Structures Working Group, github.com/pha4ge/minimal-pathogen-agnostic-contextual-data-specification, commit `0390611` (2023-05-03). One row also draws on the GRDI-AMR One Health Contextual Data Specification (github.com/cidgoh/GRDI_AMR_One_Health, commit `001f7fc`, reference guide v14.5.4), marked below.

| MARS Field | PHA4GE field (ontology ID) | Relation | Notes |
|---|---|---|---|
| `isolate_id` | `Specimen collector sample ID` (`GENEPIO:0001123`) | equivalent | User-defined sample identifier assigned by primary laboratory or collector. |
| `patient_key` | `Specimen source ID` (`GENEPIO:0100696`) | equivalent | Identifier for host or subject to allow case deduplication; pseudonymous in MARS. |
| `country_iso` | `geo_loc name (country)` (`GENEPIO:0001181`) | equivalent | PHA4GE uses country names; MARS standardises to ISO 3166-1 alpha-2 codes. |
| `region_un_m49` | `geo_loc name (state/province/region)` (`GENEPIO:0001185`) | broader | PHA4GE records sub-national administrative regions; MARS records UN M49 macro-geographical regions. |
| `year_collected` | `Sample collection date` (`GENEPIO:0001174`) | broader | PHA4GE records full date (ISO 8601 YYYY-MM-DD); MARS records collection year only (YYYY). |
| `ncbi_taxonomy_id`, `organism_name_standard` | `Organism` (`GENEPIO:0001191`) | equivalent | Both reference NCBI Taxonomy; MARS provides numeric taxonomy ID and standard binomial species name. |
| `specimen_type` | `anatomical_material` (`GENEPIO:0001211`), `body_product` (`GENEPIO:0001216`)* | related | *Drawn from GRDI-AMR One Health specification. PHA4GE separates anatomical material and body products; MARS maps into controlled specimen categories with raw values retained in `specimen_type_raw`. |

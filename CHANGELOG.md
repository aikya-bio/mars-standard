# Changelog

All notable changes to the MARS standard are documented here.

Format: [Date] · [Version] · [Change Type] · [Affected Fields/Sections] · [Migration Notes]

## [v0.4.0] — 2026-10-22

**Status:** Pre-release · Specification
**Change type:** MINOR — additive schema fields, vocabulary expansions, alignment, and compatibility crosswalks

### Added
- Four optional nullable fields on `harmonised.isolates`: `infection_origin` (`Community`, `Hospital`, `Unknown`), `patient_key` (pseudonymous, non-unique), `specimen_type_raw`, and `age_group_raw` (source strings verbatim, typed as `["string", "null"]` in JSON schema)
- Consistency rule between `nosocomial` and `infection_origin`: when both are present and `infection_origin` is not `Unknown`, they must agree (`true` <-> `Hospital`, `false` <-> `Community`), enforced via SQL CHECK constraints (PostgreSQL and SQLite) and JSON schema conditional rules (`if`/`then`)
- 11 WHO GLASS-aligned age bands added to `vocabularies/age_group.csv` with typographic en-dashes (`<1`, `1–4`, `5–14`, `15–24`, `25–34`, `35–44`, `45–54`, `55–64`, `65–74`, `75–84`, `85+`)
- Gender code `O` ("Other / not captured by M or F") added to `vocabularies/gender.csv`
- Specimen types `Stool` ("Stool / faeces") and `Genital` ("Genital / urogenital swab") added to `vocabularies/specimen_type.csv` (13 controlled values total)
- Categorical crosswalk types (`specimen`, `age_group`, `gender`, `infection_origin`) added to `vocabularies/crosswalk_type.csv` and crosswalk schemas
- Template `crosswalk_tables/categorical_crosswalk_template.csv` with `loss` tracking (`none`, `many_to_one`, `no_equivalent`)
- Full WHO GLASS compatibility tables for specimen, gender, infection origin, and age groups in `compatibility/glass_crosswalk.md`
- PAHO Enhanced Surveillance crosswalk for Primary Phase bloodstream infections in `compatibility/paho_crosswalk.md`
- Sensitive field annotation and privacy mechanisms for `patient_key` in MCP tool and server specifications (`mcp/tool_annotation_spec.yaml`, `mcp/server_metadata_spec.yaml`)

### Changed
- Four legacy age bands (`0–2`, `3–17`, `18–64`, `65+`) in `vocabularies/age_group.csv` marked as deprecated (`deprecated = TRUE`) while remaining valid
- JSON schema enums aligned with SQL CHECK constraints: closed existing drift where `specimen_type`, `age_group`, `facility_type`, and `infection_type` were free strings in `schema/mars_schema.json`
- JSON schema: `nosocomial` now accepts null (`["boolean", "null"]`), matching the nullable SQL columns
- Data dictionary lists corrected in `data_dictionary/isolates.md` to reflect complete vocabulary lists for `specimen_type`, `facility_type`, `infection_type`, `gender`, and `age_group`
- hAMRonization crosswalk (`compatibility/hamronization_crosswalk.md`) rewritten against PHA4GE hAMRonization specification v1.3.1, correcting field mappings and clarifying that `type` is an input parser column rather than an output field

### Migration Notes
- Fully backwards compatible with MARS v0.3 datasets: all new fields are optional and nullable; existing v0.3 data loads into v0.4 schemas without modification.
- Datasets should use a single age scheme (either the current GLASS-aligned bands or the deprecated legacy bands); old and new age bands overlap (e.g. `65+` vs `65–74`, `75–84`, `85+`), so mixed age schemes cannot be summarised by band and no automatic old-to-new mapping is performed.

---

## [v0.3.0] — 2026-10-12

**Status:** Pre-release · Specification
**Change type:** MINOR — additive schema field, normative test vectors, repository scope clarification

### Added
- Optional nullable `mic_raw TEXT` added to `harmonised.mic_observations` across PostgreSQL, SQLite, and JSON schemas (`["string", "null"]`) to preserve original un-normalised source strings verbatim (e.g. fixed ratios, trailing annotations, float artifacts) · Affected field: `mic_raw`
- Normative MIC normalisation test vectors in `test_vectors/mic_normalisation.csv` and documentation in `test_vectors/README.md`
- Exact decimal arithmetic tolerance rule (0.0001, inclusive) for float artifacts on dilution grid, with boundary test vectors
- Explicit "Values that are not loaded" rule: inputs with reason `empty` or `non_numeric` write no row to `mic_observations`
- Informative reason codes table in `data_dictionary/mic_observations.md` documenting test vector classifications
- Explicit MIC normalisation rules documented in `data_dictionary/mic_observations.md`

### Changed
- Standardized historical reference code extent statements across documentation (`README.md`, `CONTRIBUTING.md`, `.gitignore`, `CHANGELOG.md`) to: "Reference code is preserved in Git history up to commit 4104456."
- Removed Apache 2.0 license badge from `README.md` and removed commit hash line from `CITATION.cff` pending formal release tagging
- Updated MCP server metadata example specification version to `0.3.0`

### Removed
- Reference implementation code removed from the specification repository (`reference_implementation/`), separating specification from tooling. Reference code is preserved in Git history up to commit 4104456. Reference tooling will be released separately.

### Migration Notes
- Additive schema change: existing databases remain compatible by adding nullable `mic_raw TEXT` to `harmonised.mic_observations`.

---

## [v0.2] — 2026-07-19

**Status:** Pre-release · Aikya internal development
**Change type:** MINOR — additive discovery infrastructure artefacts

### Added
- `use_case_library/mars_ucl_v0.1.yaml` — MARS Use Case Library (MUL): 16 seed AMR investigation use cases with full schema (`id`, `name`, `pillar`, `description`, `intent_signals`, `ontology_references`, `permitted_tools`, `data_requirements`, `not_suitable_for`, `example_queries`). Pillars: Predict & Validate (5), Prevent (4), Cure (5), General (2).
- `mcp/server_metadata_spec.yaml` — MARS MCP Server Metadata Minimum Standard v0.1. Authoritative template defining all REQUIRED and RECOMMENDED fields every MARS MCP server must declare at initialisation. Includes auto-generation logic and custodian review guidance.
- `mcp/tool_annotation_spec.yaml` — MARS MCP Tool Annotation Standard v0.1. Authoritative template for per-tool routing annotations. Includes complete reference annotations for all six standard MARS tools.

### Migration Notes
_Additive only. No changes to existing schema, vocabularies, or crosswalk tables._

---

## [v0.1] — 2026-07-08

**Status:** Pre-release · Aikya internal development  
**Change type:** Initial founding specification  

### Added
- Four-table core data model: `harmonised.isolates`, `harmonised.mic_observations`, `harmonised.genotype_observations`, `harmonised.crosswalk_log`
- Mandatory, Recommended, and Optional field classifications across all four tables
- Controlled vocabularies for: `gram_type`, `mic_qualifier`, `interpretation_standard`, `breakpoint_system`, `aware_category`, `betalactamase_status`, `variant_type`, `gender`, `specimen_type`, `facility_type`, `age_group`, `infection_type`, `organism_group`
- MIC normalisation standard (5-case normalisation rule)
- PHA4GE compatibility crosswalk (6 field mappings)
- hAMRonization compatibility crosswalk
- WHO GLASS aggregate compatibility crosswalk
- MCP manifest skeleton for agentic AI access
- Reference implementation stubs: `mic_normaliser.py`, `chembl_lookup.py`, `ncbi_taxonomy_lookup.py`, `aro_lookup.py`
- PostgreSQL and SQLite schema DDL
- JSON Schema representation
- Crosswalk templates: drug, organism, gene
- Maintainer-led governance (see GOVERNANCE.md)
- Semantic versioning policy

### Migration Notes
_N/A — founding version._

---

## [Unreleased]

### Changed
- README: neutral description of WHONET and OMOP; narrowed the "why MARS exists" statement
- `chembl_lookup.py`: abbreviation map relabelled as an illustrative subset; AWaRe now resolved by name against the WHO AWaRe 2023 list (`reference_implementation/third_party/`), replacing a name-pattern heuristic
- GLASS compatibility note reworded as indicative
- GOVERNANCE.md simplified to maintainer-led with open contribution

### Removed
- `server.mars_certification_tier` from `mcp/server_metadata_spec.yaml` and the example manifest, replaced by `server.agentic_readiness_score` (self-assessed, nullable) · Affected field(s): `mars_certification_tier`, `agentic_readiness_score`
- References to unreleased tooling in `mcp/server_metadata_spec.yaml`

---

## [Upcoming] — v1.0

**Planned:** First stable public release  
**Planned changes:**
- WHONET / BacLink crosswalk
- Full MCP manifest with live endpoint validation

---

> **Format for future entries:**
>
> ```
> ## [vX.Y.Z] — YYYY-MM-DD
> **Change type:** MAJOR | MINOR | PATCH
> ### Added / Changed / Deprecated / Removed / Fixed
> - Description · Affected field(s): `field_name`
> ### Migration Notes
> - If MAJOR: describe what implementations must update and how.
> ```

# Changelog

All notable changes to the MARS standard are documented here.

Format: [Date] · [Version] · [Change Type] · [Affected Fields/Sections] · [Migration Notes]

## [v0.3.0] — 2026-10-12

**Status:** Pre-release · Specification
**Change type:** MINOR — additive schema field, normative test vectors, repository scope clarification

### Added
- Optional nullable `mic_raw TEXT` added to `harmonised.mic_observations` across PostgreSQL, SQLite, and JSON schemas to preserve original un-normalised source strings verbatim (e.g. fixed ratios, trailing annotations, float artifacts) · Affected field: `mic_raw`
- Normative MIC normalisation test vectors in `test_vectors/mic_normalisation.csv` and documentation in `test_vectors/README.md`
- Explicit MIC normalisation rules documented in `data_dictionary/mic_observations.md`

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
- Zenodo DOI registration
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

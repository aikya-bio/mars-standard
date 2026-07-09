# Changelog

All notable changes to the MARS standard are documented here.

Format: [Date] · [Version] · [Change Type] · [Affected Fields/Sections] · [Migration Notes]

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
- Governance model (BDFL-style for v0.x)
- Semantic versioning policy

### Migration Notes
_N/A — founding version._

---

## [Upcoming] — v1.0

**Planned:** First stable public release  
**Planned changes:**
- Community governance model replaces BDFL-style
- Zenodo DOI registration
- Public release of certified dataset registry
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

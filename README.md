# MARS — Minimum AMR Surveillance Standard

[![Version](https://img.shields.io/badge/version-v0.4.1-blue)](CHANGELOG.md)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-pre--release-orange)](CHANGELOG.md)

> **MARS is an open community standard for isolate-level antimicrobial resistance surveillance data.**  
> It defines a minimal mandatory data model, canonical identifier mappings, controlled vocabularies, and MCP server-metadata and tool-annotation standards for agent access - all in one versioned, citable artefact.

**Created by [Aikya](https://aikya.bio) · Specification v0.4.1**

---

## What MARS Is

MARS does not define how data is *collected*. It defines how data is **represented and shared** for computational and agentic use.

Every MARS-compliant dataset exposes four normalised tables:

| Table | Grain | Purpose |
|---|---|---|
| `harmonised.isolates` | One row per clinical isolate | Core metadata, organism, geography, demography |
| `harmonised.mic_observations` | One row per drug per isolate | Phenotypic MIC data, AWaRe, breakpoints |
| `harmonised.genotype_observations` | One row per resistance gene per isolate | AMR gene/variant data, HGVS notation |
| `harmonised.crosswalk_log` | One row per mapping decision | Full audit trail of identifier harmonisation |

---

## Why MARS Exists

No open, versioned, isolate-level specification that any data holder can adopt, and that is designed for agentic AI access, currently exists for routine and industry surveillance data.

| Standard | What It Does | Relationship to MARS |
|---|---|---|
| WHO GLASS | Aggregate surveillance (countries submit resistance *rates*) | Downstream consumer; indicative value mapping for specimen, sex, age group and infection origin (see `compatibility/glass_crosswalk.md`) |
| PHA4GE | Minimal pathogen-agnostic contextual metadata for genomics | Field-level mapping for overlapping fields (see `compatibility/pha4ge_crosswalk.md`) |
| hAMRonization | Harmonises the output of AMR gene-detection tools | Upstream source for genotype observations; indicative field mapping (see `compatibility/hamronization_crosswalk.md`) |
| PAHO enhanced isolate-level protocol | Isolate-level AMR reporting protocol for the Americas (bloodstream infection phase) | Indicative crosswalk for the bloodstream phase (see `compatibility/paho_crosswalk.md`) |
| WHONET | Free laboratory software and BacLink conversion tool, with widely used organism, antibiotic and test code dictionaries | Upstream source for routine laboratory data; WHONET and BacLink files can be mapped into MARS |
| OMOP CDM | Common data model for EHR observational data | Designed for clinical records; a different unit of analysis from surveillance isolates |

The crosswalk documents are indicative. They were checked against the cited specifications and have not been reviewed by the maintainers of those specifications.

MARS fills the gap: **an open, isolate-level CDM designed for agentic AI access**.

---

## Founding Principles

| # | Principle | Description |
|---|---|---|
| 1 | **Isolate-level, not aggregate** | MARS operates at the individual clinical isolate level. GLASS handles aggregation. |
| 2 | **Built on community identifiers** | Uses NCBI Taxonomy, ARO, ChEMBL, and ISO 3166 - invents nothing new. |
| 3 | **Mappable from PHA4GE-aligned data** | Designed to be mappable from the overlapping fields of PHA4GE-aligned datasets. |
| 4 | **Mandatory minimum, optional enrichment** | Small mandatory core; optional fields unlock additional use cases. |
| 5 | **Designed for agent access** | The schema, identifiers and MCP server-metadata and tool-annotation standards are designed for LLM and agent use. This is a design intent that independent adopters have not yet validated. |
| 6 | **Open, versioned, and citable** | CC-BY 4.0 for artefacts (schema, data dictionary, vocabularies, crosswalks, test vectors). |

---

## How to Implement MARS

To implement MARS in a custom ETL pipeline, follow these steps:
1. **Download schema SQL** from [`schema/`](schema/) and create the four core tables in your database
2. **Download crosswalk templates** from [`crosswalk_tables/`](crosswalk_tables/) and populate with your identifier lookups (reference tooling will be released separately)
3. **Normalise MIC values** according to the specification in [`data_dictionary/mic_observations.md`](data_dictionary/mic_observations.md) and validate against [`test_vectors/`](test_vectors/) before loading (reference tooling will be released separately)
4. **Load harmonised data** into the four MARS tables

---

## Repository Structure

```
mars-standard/
├── LICENSE                            # CC-BY 4.0 (standard artefacts)
├── LICENSE_CODE
├── README.md
├── CHANGELOG.md
├── GOVERNANCE.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── schema/
│   ├── mars_schema.sql                # PostgreSQL DDL
│   ├── mars_schema_sqlite.sql         # SQLite equivalent
│   └── mars_schema.json               # JSON Schema
├── data_dictionary/
│   ├── isolates.md
│   ├── mic_observations.md
│   ├── genotype_observations.md
│   └── crosswalk_log.md
├── vocabularies/                      # Controlled vocabulary CSVs
├── crosswalk_tables/                  # Mapping templates (unpopulated)
├── compatibility/
│   ├── pha4ge_crosswalk.md
│   ├── hamronization_crosswalk.md
│   ├── glass_crosswalk.md
│   └── paho_crosswalk.md
├── test_vectors/                      # Normative MIC normalisation test vectors
│   ├── mic_normalisation.csv
│   └── README.md
├── use_case_library/                  # MARS Use Case Library (MUL)
│   └── mars_ucl_v0.1.yaml             # 16 seed AMR investigation use cases
└── mcp/                               # MCP discovery infrastructure specs
    ├── server_metadata_spec.yaml      # Server metadata minimum standard template
    └── tool_annotation_spec.yaml      # Tool annotation standard template
```



## Roadmap

### v0.1 — Founding Specification ✅
The core standard artefacts:
- ✅ Four-table data model (schema SQL + JSON Schema)
- ✅ Data dictionary — field-by-field definitions for all four tables
- ✅ Controlled vocabularies (15 CSV files)
- ✅ Crosswalk templates — drug, organism, gene
- ✅ Compatibility notes — PHA4GE, hAMRonization, WHO GLASS (indicative)
- Reference Python scripts: shipped in earlier versions; removed from this repository in v0.3.0 (reference tooling will be released separately)
- ✅ Governance, contribution, and versioning policy

### v0.2 — Discovery Infrastructure
MCP agent-routing and use case vocabulary:
- ✅ MARS Use Case Library (MUL) — 16 seed AMR investigation types (`use_case_library/mars_ucl_v0.1.yaml`)
- ✅ Server Metadata Standard — minimum declaration template for every MARS MCP server (`mcp/server_metadata_spec.yaml`)
- ✅ Tool Annotation Standard — per-tool routing signals for agent use case matching (`mcp/tool_annotation_spec.yaml`)

### v0.3 — Specification Harmonisation
- ✅ Add optional nullable `mic_raw` field across schemas
- ✅ Normative MIC normalisation rules and test vectors (`test_vectors/`)
- ✅ Complete separation of specification artefacts from implementation tooling

### v0.4 — Surveillance Alignment & Demographic Extensions
- ✅ Add optional isolate fields: `infection_origin`, `patient_key`, `specimen_type_raw`, `age_group_raw`
- ✅ Consistency enforcement between `nosocomial` and `infection_origin`
- ✅ WHO GLASS-aligned age bands (11 values), gender `O`, specimen types `Stool` and `Genital`
- ✅ Categorical crosswalks and loss tracking template
- ✅ Indicative WHO GLASS crosswalk and an indicative PAHO crosswalk (bloodstream infection phase only)
- ✅ Sensitive-field handling and privacy metadata for `patient_key` in MCP specifications

### v0.4.1 — Documentation correction (current)
- ✅ PHA4GE compatibility crosswalk corrected against the PHA4GE minimal specification, with one specimen row sourced to the GRDI-AMR specification (documentation only)

### Planned (no dates)
- EARS-Net crosswalk
- Disk-diffusion zone data and an episode key as optional fields
- Controlled vocabularies and gene fields for fungal and mycobacterial resistance mechanisms
- Release of reference tooling for normalisation, identifier lookups and harmonisation reporting
- Validation of the MCP server-metadata and tool-annotation standards against live agent workflows

### v1.0 — First Stable Public Release (planned)
- WHONET / BacLink crosswalk (planned)
- MCP conformance validation against live endpoints (planned)

---

## Ecosystem & AI Readiness

MARS is designed for use by AI agents. This is a design intent; agent workflows have not yet been validated by independent adopters.
- **Small, documented schema:** four tables with documented fields and controlled values, so a query can be written against the schema without guessing what a field means.
- **Canonical IDs over strings:** Agents can use NCBI Taxonomy and ChEMBL IDs, avoiding fuzzy string matching errors.
- **Controlled vocabularies:** Published CSV files list the allowed values for categorical fields.
- **Use Case Library:** The [MARS Use Case Library](use_case_library/mars_ucl_v0.1.yaml) defines 16 structured AMR investigation types with intent signals, so agents can route queries to the right tool.
- **Discovery metadata:** An MCP server over a MARS dataset declares structured metadata (what data it holds, which use cases it supports, what it cannot do, and which fields are sensitive), so an agent can choose a server before calling any tool.

**MCP Discovery Infrastructure**
The MCP specifications (server metadata standard and tool annotation standard) live in this repo as the authoritative artefacts.

Implementers write their own discovery metadata file by following the template in `mcp/server_metadata_spec.yaml`, populating it with their data scope and supported use cases from the Use Case Library (MUL).

---

## How to cite

Cite the release you used, for example:

> MARS — Minimum AMR Surveillance Standard, v0.4.1, commit `14bfd823e2da515563003ba73c0e6b40a3595958`, https://github.com/aikya-bio/mars-standard/releases/tag/v0.4.1

---

## Licensing

| Artefact | Licence |
|---|---|
| Schema SQL, data dictionary, vocabularies, crosswalk templates, compatibility docs, test vectors, MCP specifications, use case library | [CC-BY 4.0](LICENSE) |
| Reference code preserved in Git history (up to commit 4104456) | [Apache 2.0](LICENSE_CODE) |

**Attribution required:** Any implementation of MARS must credit:  
`MARS — Minimum AMR Surveillance Standard, created by Aikya / microdao.bio`  
with a link to `https://github.com/aikya-bio/mars-standard`

---

## Community & Contributing

- 💬 **Questions & Discussion** → [GitHub Discussions](https://github.com/aikya-bio/mars-standard/discussions)
- 🐛 **Spec bug or inconsistency** → [Open an Issue](https://github.com/aikya-bio/mars-standard/issues/new?template=bug_report.yml)
- ➕ **New term or vocabulary addition** → [New Term Request](https://github.com/aikya-bio/mars-standard/issues/new?template=feature_request.yml)
- 📖 **How to contribute** → [CONTRIBUTING.md](CONTRIBUTING.md)
- ⚖️ **How decisions are made** → [GOVERNANCE.md](GOVERNANCE.md)



## Versioning

MARS follows [Semantic Versioning](https://semver.org): `MAJOR.MINOR.PATCH`

| Change Type | Bump |
|---|---|
| Schema changes that break existing implementations | MAJOR |
| New optional fields or vocabulary additions | MINOR |
| Clarifications, documentation fixes | PATCH |

**Version lifecycle:**
- `v0.x` — Pre-release; public, not yet validated by independent adopters
- `v1.0` — First stable public release, CC-BY 4.0
- `v1.x` — Community contributions, minor additions
- `v2.0` — Breaking changes, published migration guide required

---

*MARS Specification v0.4.1 · Created by [Aikya](https://aikya.bio) / [microdao.bio](https://microdao.bio)*

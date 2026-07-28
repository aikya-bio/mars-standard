# MARS — Minimum AMR Surveillance Standard

[![Version](https://img.shields.io/badge/version-v0.1-blue)](CHANGELOG.md)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![License: Apache 2.0](https://img.shields.io/badge/Code%20License-Apache%202.0-green.svg)](LICENSE_CODE)
[![Status](https://img.shields.io/badge/status-pre--release-orange)](CHANGELOG.md)
[![DOI](https://img.shields.io/badge/DOI-pending%20v1.0-lightgrey)](#)

> **MARS is an open community standard for isolate-level antimicrobial resistance surveillance data.**  
> It defines a minimal mandatory data model, canonical identifier mappings, controlled vocabularies, and a machine-readable agent access interface - all in one versioned, citable artefact.

**Created by [Aikya](https://aikya.bio) · Founding Specification v0.1**

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

No open, versioned, isolate-level data standard designed for agentic AI access currently exists.

| Standard | What It Does | Relationship to MARS |
|---|---|---|
| WHO GLASS | Aggregate surveillance (countries submit resistance *rates*) | Downstream consumer of MARS-level analysis |
| PHA4GE | Minimal pathogen-agnostic contextual metadata for genomics | Compatible - MARS is explicitly PHA4GE-aligned |
| WHONET | Data capture tool for clinical labs | Source of heterogeneous naming MARS resolves |
| OMOP CDM | Common data model for EHR observational data | Wrong fit - designed for clinical records, not surveillance isolates |

MARS fills the gap: **an open, isolate-level CDM designed for agentic AI access**.

---

## Founding Principles

| # | Principle | Description |
|---|---|---|
| 1 | **Isolate-level, not aggregate** | MARS operates at the individual clinical isolate level. GLASS handles aggregation. |
| 2 | **Built on community identifiers** | Uses NCBI Taxonomy, ARO, ChEMBL, and ISO 3166 - invents nothing new. |
| 3 | **PHA4GE-compatible** | A PHA4GE-aligned dataset can be made MARS-compliant with minimal additional work. |
| 4 | **Mandatory minimum, optional enrichment** | Small mandatory core; optional fields unlock additional use cases. |
| 5 | **Designed for Agentic Access** | Schemas and identifiers are explicitly optimized for LLM Text-to-SQL and tool use. |
| 6 | **Open, versioned, and citable** | CC-BY 4.0 for artefacts. Apache 2.0 for reference code. DOI from v1.0. |

---

## How to Implement MARS

*Note: There is an upcoming MARS CLI tool to be released soon that will empower users to automate harmonisation, map their data to MARS, and serve it via MCP.*

Until the CLI is released, you can implement the standard manually. If you are building custom ETL pipelines, follow these steps:
1. **Download schema SQL** from [`schema/`](schema/) and create the four core tables in your database
2. **Download crosswalk templates** from [`crosswalk_tables/`](crosswalk_tables/) and populate using the [reference lookup scripts](reference_implementation/)
3. **Normalise MIC values** using [`reference_implementation/mic_normaliser.py`](reference_implementation/mic_normaliser.py) before loading
4. **Load harmonised data** into the four MARS tables

---

## Repository Structure

```
mars-standard/
├── LICENSE                            # CC-BY 4.0 (standard artefacts)
├── LICENSE_CODE                       # Apache 2.0 (reference_implementation/)
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
│   └── glass_crosswalk.md
├── reference_implementation/          # Apache 2.0 — Python normalisation scripts
│   └── example_data/harmonised/       # Gold-standard demo dataset & manifest
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
- ✅ Compatibility crosswalks — PHA4GE, hAMRonization, WHO GLASS
- ✅ Reference Python scripts (`reference_implementation/`)
- ✅ Governance, contribution, and versioning policy

### v0.2 — Discovery Infrastructure (current)
MCP agent-routing and use case vocabulary:
- ✅ MARS Use Case Library (MUL) — 16 seed AMR investigation types (`use_case_library/mars_ucl_v0.1.yaml`)
- ✅ Server Metadata Standard — minimum declaration template for every MARS MCP server (`mcp/server_metadata_spec.yaml`)
- ✅ Tool Annotation Standard — per-tool routing signals for agent use case matching (`mcp/tool_annotation_spec.yaml`)

### v1.0 — First Stable Public Release (planned)
- Community governance model replaces BDFL-style
- Zenodo DOI registration
- Public release of certified dataset registry
- Full MCP manifest with live endpoint validation

---

## Ecosystem & AI Readiness

MARS is explicitly designed to be **AI-ready** out of the box:
- **LLM-Friendly Schemas:** Denormalized table structures allow LLMs to easily generate accurate Text-to-SQL queries without complex JOIN hallucinations.
- **Canonical IDs over Strings:** Agents use precise NCBI Taxonomy and ChEMBL IDs, avoiding fuzzy string matching errors.
- **Strict Vocabularies:** Extensive controlled vocabularies give LLMs perfect context on allowed values when reasoning about the data.
- **Use Case Library:** The [MARS Use Case Library](use_case_library/mars_ucl_v0.1.yaml) defines 16 structured AMR investigation types with intent signals, so agents can route queries to the right tool without guessing.
- **Discovery Manifest:** Every MARS MCP server declares structured metadata at startup — what data it holds, what use cases it supports, and what it cannot do — so agents choose the right server before calling any tool.

**MCP Discovery Infrastructure**
The MCP specifications (server metadata standard and tool annotation standard) live in this repo as the authoritative artefacts. 

*Note: An upcoming MARS CLI will be released soon that automatically generates discovery manifests from your harmonised data.*

Until the CLI is released, implementers must construct their own `manifest.yaml` manually by adhering to the template provided in `mcp/server_metadata_spec.yaml`, populating it with their data scope and supported use cases from the Use Case Library (MUL).

---

## Licensing

| Artefact | Licence |
|---|---|
| Schema SQL, data dictionary, vocabularies, crosswalk templates, compatibility docs | [CC-BY 4.0](LICENSE) |
| Reference Python scripts (`reference_implementation/`) | [Apache 2.0](LICENSE_CODE) |

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
- `v0.x` — Pre-release, Aikya internal
- `v1.0` — First stable public release, CC-BY 4.0, DOI via Zenodo
- `v1.x` — Community contributions, minor additions
- `v2.0` — Breaking changes, published migration guide required

---

*MARS Founding Specification v0.1 · Created by [Aikya](https://aikya.bio) / [microdao.bio](https://microdao.bio)*

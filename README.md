# MARS — Minimum AMR Surveillance Standard

[![Version](https://img.shields.io/badge/version-v0.4.1-blue)](CHANGELOG.md)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-pre--release-orange)](CHANGELOG.md)
[![Preprint DOI](https://img.shields.io/badge/preprint%20DOI-10.20944%2Fpreprints202611.2139.v1-blue)](https://www.preprints.org/manuscript/202611.2139)

> **MARS is an open community standard for isolate-level antimicrobial resistance (AMR) surveillance data.**
> It defines a minimal mandatory data model, canonical identifier mappings, controlled vocabularies, and MCP server-metadata and tool-annotation standards for agent access, as one versioned, citable artefact.

**Created by [Aikya](https://aikya.bio) · Specification v0.4.1 · Pre-release (not yet validated by independent adopters)**

For the rationale, design and comparison with GLASS, PHA4GE, hAMRonization, PAHO, WHONET and OMOP, read the [preprint](https://www.preprints.org/manuscript/202611.2139) (not peer-reviewed). This repository holds the specification itself.

---

## What is in this repository

MARS defines how AMR data is **represented and shared**, not how it is collected. A MARS dataset exposes four tables: `harmonised.isolates`, `harmonised.mic_observations`, `harmonised.genotype_observations` and `harmonised.crosswalk_log`.

| Folder | Contents | Raise an issue here if... |
|---|---|---|
| [`schema/`](schema/) | PostgreSQL DDL, SQLite DDL, JSON Schema | a table, column, type or constraint is wrong or missing |
| [`data_dictionary/`](data_dictionary/) | Field-by-field definitions for each table | a definition is unclear, inconsistent or contradicts the schema |
| [`vocabularies/`](vocabularies/) | Controlled-value CSVs (allowed values for categorical fields) | a value is missing, wrong or should be deprecated |
| [`crosswalk_tables/`](crosswalk_tables/) | Unpopulated mapping templates (drug, organism, gene) | a template column or identifier scheme is wrong |
| [`compatibility/`](compatibility/) | Indicative crosswalks to PHA4GE, hAMRonization, WHO GLASS, PAHO | a mapping is wrong, or you maintain the source specification |
| [`test_vectors/`](test_vectors/) | Normative MIC normalisation test cases | an expected output is wrong or a case is missing |
| [`use_case_library/`](use_case_library/) | 16 seed AMR investigation use cases (MUL) | a use case is wrong or one is missing |
| [`mcp/`](mcp/) | MCP server-metadata and tool-annotation templates | the template is unclear or inconsistent with the data model |

Crosswalk documents are indicative. They were checked against the cited specifications but have not been reviewed by those specifications' maintainers.

---

## How to use MARS

To implement MARS in your own pipeline:

1. **Create the tables.** Use the DDL in [`schema/`](schema/) (`mars_schema.sql` for PostgreSQL, `mars_schema_sqlite.sql` for SQLite), or `mars_schema.json` to validate records.
2. **Read the data dictionary.** [`data_dictionary/`](data_dictionary/) defines every field and marks it `Mandatory`, `Recommended` or `Optional`.
3. **Map your identifiers.** Populate the templates in [`crosswalk_tables/`](crosswalk_tables/) with your lookups to NCBI Taxonomy, ChEMBL and ARO, and use the values in [`vocabularies/`](vocabularies/) for categorical fields.
4. **Normalise MIC values** following [`data_dictionary/mic_observations.md`](data_dictionary/mic_observations.md), and check your implementation against [`test_vectors/`](test_vectors/) before loading.
5. **Load your data** into the four tables, recording each identifier mapping decision in `crosswalk_log`.
6. **Optional, for agent access:** describe your MCP server using the templates in [`mcp/`](mcp/) and the use cases in [`use_case_library/`](use_case_library/).

Reference tooling is not hosted in this repository and will be released separately.

---

## Feedback and issues

**One issue per term.** Please open a separate issue for each field, vocabulary value or mapping you want to add, change or question. Do not bundle several terms into one issue: each issue gets its own accept, reject or defer decision and its own changelog entry.

| I want to... | Open |
|---|---|
| Propose a **new field or table** (one field per issue) | [New term request](https://github.com/aikya-bio/mars-standard/issues/new?template=feature_request.yml) |
| **Add, change or deprecate a vocabulary value** (one value per issue) | [New term request](https://github.com/aikya-bio/mars-standard/issues/new?template=feature_request.yml), naming the vocabulary file |
| Report an **error or inconsistency** in the schema, data dictionary, vocabularies, crosswalks, test vectors or MCP templates | [Spec bug report](https://github.com/aikya-bio/mars-standard/issues/new?template=bug_report.yml) |
| Ask **how to implement MARS** or discuss use | [GitHub Discussions](https://github.com/aikya-bio/mars-standard/discussions) (not an issue) |
| Report a **security concern** or a **governance** concern | Email mars@aikya.bio (do not open a public issue); see [GOVERNANCE.md](GOVERNANCE.md) |

Search existing issues first. In every issue, name the file and field affected and give the use case or source specification behind your request. A maintainer will reply `ACCEPTED`, `REJECTED` or `DEFERRED` with written rationale. Accepted changes are made by pull request that links the issue; please do not open a pull request for a schema or vocabulary change before the issue is accepted. Full process: [CONTRIBUTING.md](CONTRIBUTING.md) · [GOVERNANCE.md](GOVERNANCE.md) · [Code of Conduct](CODE_OF_CONDUCT.md).

---

## Reuse, licence and citation

All specification artefacts in this repository (schema, data dictionary, vocabularies, crosswalks, test vectors, MCP specifications, use case library) are licensed under **[CC BY 4.0](LICENSE)**. You may copy, adapt and redistribute them, including commercially, provided you:

- **credit** the standard: `MARS — Minimum AMR Surveillance Standard, created by Aikya / microdao.bio`, with a link to <https://github.com/aikya-bio/mars-standard>;
- **link to the licence** (<https://creativecommons.org/licenses/by/4.0/>); and
- **indicate whether you made changes**, and name the MARS version you used.

Reference code in Git history up to commit `4104456` is licensed under Apache 2.0. Source specifications referenced in `compatibility/` keep their own licences; see the notices in those files.

**Citing.** Please cite the [preprint](https://www.preprints.org/manuscript/202611.2139) (Preprints.org, version 1, 20 November 2026; not peer-reviewed). The DOI may not resolve until registration completes; the link goes directly to the article. GitHub's "Cite this repository" button uses [`CITATION.cff`](CITATION.cff).

```bibtex
@article{kothamachu2026mars,
  author  = {Kothamachu, Varun},
  title   = {{MARS}: An Open Minimum Standard for Isolate-Level Antimicrobial Resistance Surveillance Data},
  journal = {Preprints},
  year    = {2026},
  month   = nov,
  doi     = {10.20944/preprints202611.2139.v1},
  url     = {https://www.preprints.org/manuscript/202611.2139},
  note    = {Preprint, not peer-reviewed}
}
```

To cite a specific release, add the version and release link, for example: *MARS — Minimum AMR Surveillance Standard, v0.4.1, https://github.com/aikya-bio/mars-standard/releases/tag/v0.4.1*

---

## Versioning and status

MARS follows [Semantic Versioning](https://semver.org): breaking schema changes are MAJOR, new optional fields and vocabulary additions are MINOR, clarifications and documentation fixes are PATCH. All changes are recorded in [CHANGELOG.md](CHANGELOG.md).

`v0.x` is pre-release. Planned work (no dates): EARS-Net and WHONET/BacLink crosswalks, disk-diffusion zone data, fungal and mycobacterial mechanisms, reference tooling, and validation of the MCP standards against live agent workflows. `v1.0` will be the first stable release.

---

*MARS Specification v0.4.1 · Created by [Aikya](https://aikya.bio) / [microdao.bio](https://microdao.bio)*

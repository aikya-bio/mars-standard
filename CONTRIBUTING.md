# Contributing to MARS

Thank you for your interest in contributing to the Minimum AMR Surveillance Standard. MARS is an open community project — your expertise makes it better.

Please read [GOVERNANCE.md](GOVERNANCE.md) for the full decision-making process.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Before You Start](#before-you-start)
- [Requesting a New Term or Field](#requesting-a-new-term-or-field)
- [Proposing a Vocabulary Change](#proposing-a-vocabulary-change)
- [Reporting a Spec Bug](#reporting-a-spec-bug)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Style Guide](#style-guide)

---

## Code of Conduct

By participating in this project, you agree to abide by the [MARS Code of Conduct](CODE_OF_CONDUCT.md). Be respectful, constructive, and collaborative.

---

## Ways to Contribute

| Type | How |
|---|---|
| 🐛 Report a spec inconsistency | [Open a Spec Bug Report issue](../../issues/new?template=bug_report.yml) |
| ➕ Request a new field | [Open a New Term Request issue](../../issues/new?template=feature_request.yml) |
| 📋 Propose a vocabulary change | [Open a Vocabulary Change issue](../../issues/new?template=feature_request.yml) |
| 💬 Ask a question | [Start a Discussion](../../discussions) |
| 🔧 Improve reference implementation code | Fork → PR (see below) |
| 📖 Improve documentation | Fork → PR (see below) |

---

## Before You Start

1. **Search existing issues and discussions** to check if someone has already raised the same point.
2. **Read the relevant data dictionary doc** in [`data_dictionary/`](data_dictionary/) to understand the current field definitions.
3. **Check the controlled vocabularies** in [`vocabularies/`](vocabularies/) before requesting a new term.
4. For significant proposals, **open an issue first** before writing any code or drafting a PR. This saves everyone time.

---

## Requesting a New Term or Field

Use the [New Term Request issue template](../../issues/new?template=new_term_request.yml). Please provide:

- **Which table** the field belongs in (`isolates`, `mic_observations`, `genotype_observations`, `crosswalk_log`)
- **Proposed field name** (snake_case, consistent with existing fields)
- **Data type** (TEXT, INTEGER, DECIMAL, BOOLEAN, TIMESTAMPTZ, JSONB)
- **Status** you are proposing (Mandatory / Recommended / Optional) — with justification
- **Description** of what the field captures
- **External ontology or standard reference** (e.g., NCBI Taxonomy, ARO, ChEMBL, ISO code)
- **Example values**
- **Use case:** what MARS query or agentic use case this field enables

New mandatory fields require a MAJOR version bump and 60-day comment period. New optional/recommended fields require a MINOR version bump and 30-day comment period.

---

## Proposing a Vocabulary Change

Use the [Vocabulary Change issue template](../../issues/new?template=vocabulary_change.yml). Specify:

- **Which vocabulary** (e.g., `specimen_type`, `aware_category`)
- **Change type:** Add / Modify / Deprecate
- **Proposed value** and its definition
- **Rationale** — why is the current vocabulary insufficient?
- **Backward-compatibility impact** — will existing implementations break?

All vocabulary CSVs live in [`vocabularies/`](vocabularies/).

---

## Reporting a Spec Bug

Use the [Spec Bug Report issue template](../../issues/new?template=spec_bug_report.yml). Include:

- **Section** of the spec where the error appears
- **Field name(s)** involved
- **Description** of the inconsistency or error
- **Suggested fix** if you have one

---

## Submitting a Pull Request

> **PRs should always reference an approved issue.** Do not open a PR for schema or vocabulary changes without a linked, accepted issue.

1. **Fork** the repository and create a branch: `git checkout -b fix/issue-123-specimen-type`
2. Make your changes. Follow the [style guide](#style-guide) below.
3. **Update CHANGELOG.md** — add an entry under `[Unreleased]`
4. **Open the PR** against `main`, fill out the [PR template](.github/pull_request_template.md), and link the related issue
5. A maintainer will review within the SLA defined in [GOVERNANCE.md](GOVERNANCE.md)

**Branch naming:**
- `fix/issue-NNN-short-description` — for spec bug fixes
- `feat/issue-NNN-short-description` — for new fields or vocabulary additions
- `docs/issue-NNN-short-description` — for documentation improvements

---

## Style Guide

### Markdown files
- Use sentence case for headings
- Use markdown tables for field definitions (see `data_dictionary/isolates.md` as the reference)
- Status values must be exactly: `Mandatory` / `Recommended` / `Optional` (capitalised)

### SQL files
- Column names in `snake_case`
- All mandatory fields must have `NOT NULL` constraints
- Add inline comments for non-obvious fields

### Python scripts (reference_implementation/)
- PEP 8 compliant
- Every public function must have a Google-style docstring
- No external dependencies beyond the Python standard library (unless absolutely necessary and documented)

### CSV files (vocabularies/, crosswalk_tables/)
- UTF-8 encoding
- Unix line endings
- Always include the header row
- The `value` column must exactly match the string used in the schema

---

## Questions?

For general questions about implementing MARS, start a [Discussion](../../discussions) rather than opening an issue. Discussions are a great place for community Q&A.

---

*MARS is maintained by [Aikya](https://aikya.bio). Thank you for helping build the standard for AMR surveillance data.*

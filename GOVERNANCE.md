# MARS Governance

This document describes how the MARS standard is maintained, how contributions are reviewed, and how decisions are made.

---

## 1. Overview

MARS is an open specification maintained by Aikya / microdao.bio. Anyone may propose changes through GitHub Issues and pull requests. Aikya maintainers review proposals and make final decisions, and give written rationale for each decision.

---

## 2. How Changes Are Proposed

All changes to the MARS standard — whether schema modifications, new vocabulary terms, or documentation fixes — must be proposed through a **GitHub Issue** before any pull request is submitted.

### Step-by-step process

1. **Open an Issue** using the appropriate template:
   - [New Term Request](https://github.com/aikya-bio/mars-standard/issues/new?template=feature_request.yml) — to add a new field or table
   - [Vocabulary Change](https://github.com/aikya-bio/mars-standard/issues/new?template=feature_request.yml) — to add, modify, or deprecate a controlled vocabulary value
   - [Spec Bug Report](https://github.com/aikya-bio/mars-standard/issues/new?template=bug_report.yml) — to report an inconsistency or error in the specification
   - [General Question](https://github.com/aikya-bio/mars-standard/discussions) — for questions and usage discussions

2. **Community comment period:**
   - `PATCH` changes (documentation fixes, clarifications): No minimum comment period. Maintainer can merge after review.
   - `MINOR` changes (new optional fields, vocabulary additions): **30-day** community comment period before decision.
   - `MAJOR` changes (breaking schema changes, new mandatory fields): **60-day** community comment period, requires explicit maintainer sign-off with written rationale.

3. **Decision:** A maintainer posts a decision comment on the issue: `ACCEPTED`, `REJECTED`, or `DEFERRED` with rationale.

4. **Implementation:** Accepted changes are implemented via a Pull Request that references the issue. The PR must update: the relevant schema/vocabulary file, the data dictionary, and the CHANGELOG.

---

## 3. Decision Authority

Aikya / microdao.bio maintains MARS. Final decisions on acceptance or rejection of proposed changes rest with Aikya maintainers, which keeps the specification coherent and versioned. Rationale is always provided in writing on the relevant GitHub Issue.

---

## 4. Review SLAs

| Change Type | Target Response Time |
|---|---|
| Spec bug report | 5 working days |
| New vocabulary term request | 15 working days |
| New field (MINOR) | 30 working days + community comment period |
| Breaking schema change (MAJOR) | 60-day comment period, then maintainer decision |

---

## 5. Code of Conduct

All contributors and community members are expected to adhere to the [MARS Code of Conduct](CODE_OF_CONDUCT.md).

---

## 6. How to Report Issues with Governance

If you believe a governance process has not been followed correctly, email **mars@aikya.bio** with the subject line `MARS Governance Concern — [Issue #]`.

---

## 7. Reporting Security Vulnerabilities

If you discover a security issue in any MARS reference implementation code, **do not open a public issue**. Email **mars@aikya.bio** instead.

---

## 8. Attribution

Any implementation of MARS must credit:  
`MARS — Minimum AMR Surveillance Standard, created by Aikya / microdao.bio`  
with a link to `https://github.com/aikya-bio/mars-standard`

---

*Last updated: v0.3.0 · 2026-10-12 · Aikya*

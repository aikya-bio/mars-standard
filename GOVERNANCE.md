# MARS Governance

This document describes how the MARS standard is maintained, how contributions are reviewed, and how decisions are made.

---

## 1. Overview

MARS uses a **BDFL-style governance model** during the v0.x pre-release phase, transitioning to a **community governance model** from v1.0 onwards.

| Phase | Decision Authority | Contribution Channel |
|---|---|---|
| `v0.x` (pre-release) | Aikya (BDFL-style) | GitHub Issues — reviewed by Aikya maintainers |
| `v1.0+` (stable) | Elected steering committee + Aikya seat | GitHub Issues → 30-day community comment period |

---

## 2. How Changes Are Proposed

All changes to the MARS standard — whether schema modifications, new vocabulary terms, or documentation fixes — must be proposed through a **GitHub Issue** before any pull request is submitted.

### Step-by-step process

1. **Open an Issue** using the appropriate template:
   - [New Term Request](../../issues/new?template=feature_request.yml) — to add a new field or table
   - [Vocabulary Change](../../issues/new?template=feature_request.yml) — to add, modify, or deprecate a controlled vocabulary value
   - [Spec Bug Report](../../issues/new?template=bug_report.yml) — to report an inconsistency or error in the specification
   - [General Question](../../discussions) — for questions and usage discussions

2. **Community comment period:**
   - `PATCH` changes (documentation fixes, clarifications): No minimum comment period. Maintainer can merge after review.
   - `MINOR` changes (new optional fields, vocabulary additions): **30-day** community comment period before decision.
   - `MAJOR` changes (breaking schema changes, new mandatory fields): **60-day** community comment period, requires explicit steering committee vote from v1.0.

3. **Decision:** Maintainer (or steering committee from v1.0) posts a decision comment on the issue: `ACCEPTED`, `REJECTED`, or `DEFERRED` with rationale.

4. **Implementation:** Accepted changes are implemented via a Pull Request that references the issue. The PR must update: the relevant schema/vocabulary file, the data dictionary, and the CHANGELOG.

---

## 3. Decision Authority

### v0.x (Current)

**BDFL:** Aikya / microdao.bio  
All final decisions on acceptance or rejection of proposed changes rest with Aikya maintainers.  
Rationale is always provided in writing on the relevant GitHub Issue.

### v1.0+ (Planned)

A **MARS Steering Committee** will be formed, comprising:
- 2 seats: Aikya (permanent, as founding organisation)
- 3 seats: Elected community representatives (researchers, implementers, public health institutions)
- Quorum: 4 of 5 members required for MAJOR version decisions

Details of the v1.0 governance transition will be published as a separate RFC before the v1.0 release.

---

## 4. Review SLAs

| Change Type | Target Response Time |
|---|---|
| Spec bug report | 5 working days |
| New vocabulary term request | 15 working days |
| New field (MINOR) | 30 working days + community comment period |
| Breaking schema change (MAJOR) | By steering committee vote |

---

## 5. Code of Conduct

All contributors and community members are expected to adhere to the [MARS Code of Conduct](CODE_OF_CONDUCT.md).

---

## 6. How to Report Issues with Governance

If you believe a governance process has not been followed correctly, email **governance@aikya.bio** with the subject line `MARS Governance Concern — [Issue #]`.

---

## 7. Reporting Security Vulnerabilities

If you discover a security issue in any MARS reference implementation code, **do not open a public issue**. Email **security@aikya.bio** instead.

---

## 8. Attribution

Any implementation of MARS must credit:  
`MARS — Minimum AMR Surveillance Standard, created by Aikya / microdao.bio`  
with a link to `https://github.com/aikya-bio/mars`

---

*Last updated: v0.1 · 2026-07-08 · Aikya*

# MARS Governance

This document describes how the MARS standard is maintained, how contributions are reviewed, and how decisions are made.

---

## 1. Overview

MARS uses a **BDFL-style governance model** during its incubation and initial release phases, transitioning to a **community governance model** once critical adoption milestones are met.

| Phase | Decision Authority | Contribution Channel |
|---|---|---|
| `Incubation` (v0.x - v1.x) | Aikya (BDFL-style) | GitHub Issues — reviewed by Aikya maintainers |
| `Community` (Post-trigger) | Elected steering committee + Aikya seat | GitHub Issues → 30-day community comment period |

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

### Incubation Phase (Current)

**BDFL:** Aikya / microdao.bio  
To ensure rapid iteration and agility during early adoption, all final decisions on acceptance or rejection of proposed changes rest with Aikya maintainers.  
Rationale is always provided in writing on the relevant GitHub Issue.

### Community Phase (Planned Transition)

To guarantee that MARS remains an open, community-owned standard, Aikya will cede BDFL control and form a formal **MARS Steering Committee**. 

**The Transition Trigger:**
This governance transition will occur automatically when MARS reaches **10 independent institutional adopters**.

The committee will comprise:
- 2 seats: Aikya (permanent, as founding organisation)
- 3 seats: Elected community representatives (researchers, implementers, public health institutions)
- Quorum: 4 of 5 members required for MAJOR version decisions

Details of the governance transition and election mechanics will be published as a separate RFC when the adoption trigger is reached.

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

If you believe a governance process has not been followed correctly, email **mars@aikya.bio** with the subject line `MARS Governance Concern — [Issue #]`.

---

## 7. Reporting Security Vulnerabilities

If you discover a security issue in any MARS reference implementation code, **do not open a public issue**. Email **mars@aikya.bio** instead.

---

## 8. Attribution

Any implementation of MARS must credit:  
`MARS — Minimum AMR Surveillance Standard, created by Aikya / microdao.bio`  
with a link to `https://github.com/aikya-bio/mars`

---

*Last updated: v0.1 · 2026-07-08 · Aikya*

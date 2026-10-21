# PAHO Enhanced Surveillance Compatibility

This document provides a crosswalk between MARS and the Pan American Health Organization (PAHO) isolate-level surveillance protocol.

> **Notice:** This crosswalk is indicative, not a validated mapping. Implementation teams must verify transformation and aggregation logic against their local institutional and national reporting rules.

**Source citation:** Protocol for Enhanced Isolate-Level Antimicrobial Resistance Surveillance in the Americas. Primary Phase: Bloodstream Infections. Washington, D.C.: Pan American Health Organization; 2021 (CDE/AR/2020).

*(In compliance with CC BY-NC-SA 3.0 IGO licensing, tables contain codes, labels, and MARS mappings only; descriptive prose from the manual is not reproduced.)*

## Scope
This crosswalk applies specifically to the **Primary Phase: Bloodstream Infections** of the PAHO protocol. In this initial surveillance phase, only bloodstream infection isolates (specimen code `bl`) are collected regionally.

## Specimen Crosswalk
Source: PAHO 2021, Section 5, Table: Primary Phase variables, Variable 16 (`SPEC_TYPE`), p. 41.

| PAHO Code | PAHO Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `bl` | Blood | `Blood` | none | Primary Phase collects bloodstream specimens only. |

## Sex / Gender Crosswalk
Source: PAHO 2021, Section 5, Table: Primary Phase variables, Variable 4 (`SEX`), p. 38.

| PAHO Code | PAHO Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `m` | male | `M` | none | Direct 1:1 match. |
| `f` | female | `F` | none | Direct 1:1 match. |
| `o` | other | `O` | none | Direct 1:1 match. Added in MARS v0.4. |
| `u` | unknown | `Unknown` | none | Direct match for unrecorded or unknown sex. |

## Infection Origin Crosswalk
Source: PAHO 2021, Section 5, Table: Primary Phase variables, Variable 12 (`INFECT_TYP`), p. 40.

| PAHO Code | PAHO Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `ho` | hospital origin | `Hospital` | none | Healthcare-associated; must agree with `nosocomial = true` when both populated. |
| `co` | community origin | `Community` | none | Community-acquired; must agree with `nosocomial = false` when both populated. |
| `unk` | unknown | `Unknown` | none | Origin unknown. |

## Age Crosswalk
Source: PAHO 2021, Section 5, Table: Primary Phase variables, Variable 6 (`AGE` and `PAT_TYPE`), pp. 38–39.

PAHO captures patient age through two distinct variables:

1. **Exact Age (`AGE`):** Recorded in exact units (years: `1, 2, 3...`; months: `1m, 2m... 11m`; weeks: `1w, 2w... 51w`; days: `1d, 2d... 30d`). When exact age is available, implementers should compute the corresponding standard MARS age band (`<1`, `1–4`, `5–14`, `15–24`, `25–34`, `35–44`, `45–54`, `55–64`, `65–74`, `75–84`, `85+`).
2. **Age Category (`PAT_TYPE`):** Broad clinical age categories used when exact age is unrecorded:

| PAHO Code | PAHO Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `new` | newborn | `Unknown` | no_equivalent | No direct band mapping; preserve `new` in `age_group_raw`. Map to `<1` only if exact age or birth date confirms age under 1 year. |
| `ped` | pediatric | `Unknown` | no_equivalent | Broad clinical group spanning multiple MARS bands (`<1` through `15–24`); preserve `ped` in `age_group_raw`. |
| `adu` | adult | `Unknown` | no_equivalent | Spans multiple MARS adult bands; preserve `adu` in `age_group_raw`. |
| `ger` | geriatric | `Unknown` | no_equivalent | Spans multiple older adult bands (`65–74`, `75–84`, `85+`); preserve `ger` in `age_group_raw`. |
| `unk` | unknown | `Unknown` | none | Age unknown. |
| `oth` | other | `Unknown` | no_equivalent | Other category; preserve in `age_group_raw`. |

## Patient Identifier (`PATIENT_ID`)
Source: PAHO 2021, Section 5, Table: Primary Phase variables, Variable 3 (`PATIENT_ID`), p. 37.

PAHO requires anonymisation of patient identifiers before regional transmission. Similarly, MARS `harmonised.isolates.patient_key` is an optional pseudonymous key:
- Direct patient identifiers (hospital MRNs, national identity numbers, names) must **never** be stored in `patient_key`.
- `patient_key` must be derived via a keyed cryptographic hash with a secret salt held securely by the data owner (e.g. HMAC-SHA256).
- `patient_key` is unique only within `source_dataset` to identify deduplicated repeat isolates from the same patient.

## Location / Ward Type Crosswalk
Source: PAHO 2021, Section 5, Table: Primary Phase variables, Variable 11 (`WARD_TYPE`), p. 40.

| PAHO Code | PAHO Label | MARS `facility_type` | Loss | Notes |
|---|---|---|---|---|
| `icu` | intensive care unit | `ICU` | none | Direct match. |
| `out` | outpatient | `Outpatient` | none | Direct match. |
| `com` | community | `Community` | none | Direct match. |
| `nur` | nursing home | `Long-term Care` | none | Direct match. |
| `in` | inpatient | `General Ward` | many_to_one | Approximation; general inpatient setting without sub-ward specificity. |
| `inx` | inpatient (non-ICU) | `General Ward` | many_to_one | Approximation; non-ICU inpatient care. |
| `int` | intermediate CU | `General Ward` | many_to_one | Approximation; step-down or intermediate care unit. |
| `eme` | emergency | `Unknown` | no_equivalent | Emergency department has no distinct MARS `facility_type`; record raw value in metadata or crosswalk audit. |
| `lab` | laboratory | `Unknown` | no_equivalent | Diagnostic facility, not a care setting; mapped to `Unknown`. |
| `oth` | other | `Unknown` | no_equivalent | Other unclassified location; mapped to `Unknown`. |
| `mix` | mixed | `Unknown` | no_equivalent | Mixed ward type; mapped to `Unknown`. |
| `unk` | unknown | `Unknown` | no_equivalent | Unknown location type; mapped to `Unknown`. |

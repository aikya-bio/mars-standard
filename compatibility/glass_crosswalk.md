# WHO GLASS Compatibility

MARS operates at the individual clinical isolate level, whereas the WHO Global Antimicrobial Resistance Surveillance System (GLASS) collects aggregated surveillance data (national RIS and SAMPLE datasets). Isolate-level data formatted according to MARS can be aggregated into the categorical summary counts requested by GLASS.

> **Notice:** This crosswalk is indicative, not a validated submission mapping. Implementation teams must verify aggregation logic against their reporting mandate.

**Source citation:** GLASS manual for antimicrobial resistance surveillance in common bacteria causing human infection. Geneva: World Health Organization; 2023. ISBN 978-92-4-007660-0 (electronic). Annex 3 coded values, Annex 1 RIS variables.

*(In compliance with CC BY-NC-SA 3.0 IGO licensing, tables contain codes, labels, and MARS mappings only; descriptive prose from the manual is not reproduced.)*

## Conceptual Mapping

| MARS Field | GLASS Concept | Notes |
|---|---|---|
| `organism_name_standard` | Target pathogen | Filter isolates to GLASS target pathogens (Annex 3). |
| `specimen_type` | Specimen source | Mapped to GLASS priority specimen types (Blood, Urine, Stool, Genital swabs, etc.). |
| `drug_name_standard` | Target antibacterial | Aggregate counts per target antimicrobial agent (Annex 3). |
| `interpretation_standard` | Susceptibility categories (S / I / R) | Group by susceptibility category to generate the aggregated counts (`S`, `I`, `R`) required by GLASS. |
| `gender`, `age_group` | Demographics | Stratification variables for demographic reporting (Annex 3). |
| `infection_origin` | Infection origin (HO / CO) | Stratification by origin of infection. |

## Specimen Crosswalk

| GLASS Code | GLASS Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `BLOOD` | Blood | `Blood` | none | Direct 1:1 match. |
| `CSF` | Cerebrospinal fluid | `CSF` | none | Direct 1:1 match. |
| `URINE` | Urine | `Urine` | none | Direct 1:1 match. |
| `STOOL` | Stool | `Stool` | none | Direct 1:1 match. Added in MARS v0.4. |
| `LOWRESP` | Lower respiratory tract | `Respiratory` | many_to_one | MARS `Respiratory` covers both lower and upper respiratory tract samples; source specificity survives in `specimen_type_raw`. |
| `UROGENITAL` | Urethral and cervical swabs | `Genital` | none | Direct match for urogenital specimens. Added in MARS v0.4. |
| `ANORECTAL` | Anorectal swabs | `Other` | no_equivalent | No direct MARS equivalent; mapped to `Other`, preserved in `specimen_type_raw`. |
| `PHARYNGEAL` | Pharyngeal swabs | `Other` | no_equivalent | No direct MARS equivalent; mapped to `Other`, preserved in `specimen_type_raw`. |

## Gender Crosswalk

Source: GLASS manual 2023, Annex 3 (coded values for national aggregated data).

| GLASS Code | GLASS Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `M` | Male | `M` | none | Direct 1:1 match. |
| `F` | Female | `F` | none | Direct 1:1 match. |
| `O` | Other | `O` | none | Direct 1:1 match. Added in MARS v0.4. |
| `UNK` | Unknown | `Unknown` | none | Used when data are not stratified by gender. |

## Infection Origin Crosswalk

| GLASS Code | GLASS Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `HO` | Hospital origin | `Hospital` | none | Must agree with `nosocomial = true` when both populated. |
| `CO` | Community origin | `Community` | none | Must agree with `nosocomial = false` when both populated. |
| `UNK` | Unknown | `Unknown` | none | Used when data are not stratified by infection origin. |

### Origin Definition Note
GLASS defines infection origin based on length of stay prior to sample collection: hospital origin is defined as hospitalization for more than 2 calendar days (or transfer from another health care facility where admitted for 2 or more calendar days); community origin is defined as outpatient status or hospitalization for 2 calendar days or fewer. Implementers should note that the manual's narrative contains subtle inconsistencies regarding the exact 2-day threshold (e.g. `> 2 days` vs `≥ 2 days` in transfer criteria), and should explicitly document their institutional operationalization in `crosswalk_log` or dataset documentation.

## Age Group Crosswalk

| GLASS Code | GLASS Label | MARS Value | Loss | Notes |
|---|---|---|---|---|
| `<1` | <1 | `<1` | none | Under 1 year. |
| `01<04` | 1-4 | `1–4` | none | 1 to 4 years. |
| `05<14` | 5-14 | `5–14` | none | 5 to 14 years. |
| `15<24` | 15-24 | `15–24` | none | 15 to 24 years. |
| `25<34` | 25-34 | `25–34` | none | 25 to 34 years. |
| `35<44` | 35-44 | `35–44` | none | 35 to 44 years. |
| `45<54` | 45-54 | `45–54` | none | 45 to 54 years. |
| `55<64` | 55-64 | `55–64` | none | 55 to 64 years. |
| `65<74` | 65-74 | `65–74` | none | 65 to 74 years. |
| `75<84` | 75-84 | `75–84` | none | 75 to 84 years. |
| `85<` | 85+ | `85+` | none | 85 years and older. |
| `UNK` | Unknown | `Unknown` | none | Used when data are not stratified by age. |

*Note:* GLASS uses `<` as the separator in age band codes (e.g., `01<04`, `85<`) specifically to avoid automated spreadsheet date reformatting. MARS standard values use typographic en-dashes (`1–4`, `85+`).

## Patient Location Type Note
GLASS collects inpatient versus outpatient patient location type. MARS has no direct equivalent field; `facility_type` (ICU, General Ward, Community, Outpatient, Long-term Care, Unknown) is related but not equivalent.

# Data Dictionary: harmonised.mic_observations

One row per drug tested per isolate. An isolate tested against 20 drugs produces 20 rows.

| Field | Type | Status | Description |
|---|---|---|---|
| `isolate_id` | TEXT | Mandatory | Foreign key to isolates |
| `source_dataset` | TEXT | Mandatory | Identifier of the source dataset (free text, e.g. `Demo-Dataset-2026`) |
| `chembl_id` | TEXT | Mandatory | ChEMBL compound identifier |
| `drug_name_standard` | TEXT | Mandatory | ChEMBL preferred name |
| `drug_class` | TEXT | Recommended | Beta-lactam / Fluoroquinolone / Aminoglycoside / etc. |
| `aware_category` | TEXT | Recommended | Access / Watch / Reserve / Unknown |
| `mic_numeric` | DECIMAL | Mandatory | Normalised MIC value |
| `mic_qualifier` | TEXT | Mandatory | = / > / < / >= / <= |
| `mic_raw` | TEXT | Optional | Original MIC string as in source data |
| `interpretation_raw` | TEXT | Optional | Original S/I/R as in source data |
| `interpretation_standard` | TEXT | Recommended | S / I / R / Unknown |
| `breakpoint_system` | TEXT | Recommended | CLSI / EUCAST / Unknown |
| `breakpoint_version` | TEXT | Optional | e.g. EUCAST 2023, CLSI 2022 |

## MIC Normalisation Rules

1. **Conventional Concentration Grid & Float Artifacts**:
   - The conventional doubling dilution series forms the reference concentration grid (..., 0.002, 0.004, 0.008, 0.015, 0.03, 0.06, 0.12, 0.25, 0.5, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 mg/L).
   - Artifact tolerance is **0.0001, inclusive**, evaluated on the decimal value **in exact decimal arithmetic** (for example Python `decimal.Decimal`, not binary floating point). A value v is an overflow artefact if 0 < v − g ≤ 0.0001 and an underflow artefact if 0 < g − v ≤ 0.0001 for a grid value g. Implementations that use binary floats MUST round |v − g| to at least 6 decimal places before comparing.
   - **Overflow**: A value within $10^{-4}$ above a grid value is an off-scale high artifact and normalises to `>grid` (e.g., `64.0001` -> `mic_numeric: 64.0`, `mic_qualifier: '>'`).
   - **Underflow**: A value within $10^{-4}$ below a grid value is an off-scale low artifact and normalises to `<=grid` (e.g., `0.0599` -> `mic_numeric: 0.06`, `mic_qualifier: '<='`), interpreted as left-censored at the lowest tested concentration (inferred rule; provisional, see GitHub issue #4).
   - Ordinary plain decimals not within tolerance of a float artifact (e.g., `0.5`, `1.5`) retain qualifier `=`.

2. **Censored Values & No Imputation**:
   - Censored values are preserved exactly as reported (e.g., `<=0.25` -> `mic_numeric: 0.25`, `mic_qualifier: '<='`).
   - **No imputation** is performed at the MARS storage layer (e.g., no halving `<` values to `0.125`, no converting flags to `0`). Downstream analysis tasks (such as MIC50/MIC90 calculation or log2 transformation) handle imputation explicitly as needed.

3. **Fixed Ratios**:
   - For combination antimicrobials reported as fixed ratios (e.g., `4/2`, `0.25/4.75`), `mic_numeric` records the first component (the primary agent) so numeric filtering and statistical operations continue to function.
   - The full original representation is preserved verbatim in `mic_raw`.

4. **Preservation of Raw Input (`mic_raw`)**:
   - The full, un-normalised input string from the source data is captured in `mic_raw` (e.g., `64.0001`, `0.0599`, `4/2`, `8 (R)`, `1,5`).

5. **No Breakpoint or S/I/R Interpretation**:
   - The normalisation layer does not apply clinical breakpoints or infer S/I/R interpretations. MARS stores what the source reported.

## Values that are not loaded

If normalisation yields no numeric value or no qualifier (reason `empty` or `non_numeric`: blank, whitespace, NA, ND, bare S/I/R tokens, a lone qualifier symbol, or unparseable text), **no row is written to `mic_observations`**, because `mic_numeric` and `mic_qualifier` are mandatory and MUST NOT be imputed. The source string is preserved by the loader outside this table (for example in its own load report). Implementations MUST NOT substitute a default value.

## Reason codes (informative, used by the test vectors)

The reason codes below are used exclusively by the normative test vectors to classify normalisation outcomes. They are informative diagnostic codes and are **not** stored as fields in the `harmonised.mic_observations` schema table.

| Reason Code | Meaning |
|---|---|
| `ok` | Standard concentration decimal, integer, or reported inequality parsed without artifact adjustment. |
| `empty` | Input is empty or contains only whitespace; yields no numeric value or qualifier and is not loaded. |
| `non_numeric` | Input contains unparseable text, missing tokens (`NA`, `ND`), bare S/I/R tokens, or lone qualifiers; not loaded. |
| `float_artifact_overflow` | Off-scale high artifact within 0.0001 above a grid concentration; normalises to `>grid`. |
| `float_artifact_underflow` | Off-scale low artifact within 0.0001 below a grid concentration; normalises to `<=grid` (provisional). |
| `ratio` | Combination antimicrobial reported as a fixed ratio; primary agent stored in `mic_numeric`, full string in `mic_raw`. |

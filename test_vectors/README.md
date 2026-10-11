# MARS Test Vectors: MIC Normalisation

This directory contains normative test vectors for the MARS Minimum Inhibitory Concentration (MIC) normalisation rules.

## Purpose

The MARS specification defines unambiguous rules for converting heterogeneous raw MIC strings reported by laboratory information systems, instruments, and literature into standard numeric and qualifier representations without clinical interpretation or statistical imputation.

Conforming implementations of MARS tools and pipelines must pass these test vectors.

## Schema of `mic_normalisation.csv`

| Column | Type | Description |
|---|---|---|
| `input` | TEXT | Raw string input presented to the normaliser |
| `expected_numeric` | REAL | Expected normalised numeric value (empty if non-numeric/empty) |
| `expected_qualifier` | TEXT | Expected qualifier: `=`, `>`, `<`, `>=`, `<=`, or empty |
| `expected_mic_raw` | TEXT | Expected raw string preserved in `mic_raw` (empty if blank/empty input) |
| `reason_code` | TEXT | Reason code explaining normalisation outcome (`ok`, `float_artifact_overflow`, `float_artifact_underflow`, `ratio`, `empty`, `non_numeric`) |
| `status` | TEXT | `approved` or `provisional` (underflow is provisional pending issue #4) |
| `note` | TEXT | Contextual explanation and rationale |

## Status Classifications

- **`approved`**: Normative requirement confirmed by MARS specification governance.
- **`provisional`**: Inferred behavior currently under review (e.g. float underflow mapped to `<=` pending confirmation on paired legacy datasets; see GitHub issue #4).

## Normalisation Principles

1. **Float Artifacts on Dilution Grid**: Values within $10^{-4}$ above a standard doubling dilution grid value are treated as overflow (`>grid`). Values within $10^{-4}$ below a grid value are treated as underflow (`<=grid`, provisional). Ordinary decimals outside this tolerance remain `=`.
2. **Censored Values Preserved**: `<` and `<=` are never imputed or halved; `>` and `>=` are never bumped.
3. **Fixed Ratios**: For combinations (e.g. `4/2`), the primary component is recorded in `expected_numeric`, and the complete original string is retained in `expected_mic_raw`.
4. **No Breakpoints**: Breakpoints and S/I/R interpretations are not applied by this layer.

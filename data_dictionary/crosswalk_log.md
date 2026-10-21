# Data Dictionary: harmonised.crosswalk_log

Audit trail of every mapping decision. This is the standardisation evidence.

| Field | Type | Status | Description |
|---|---|---|---|
| `source_dataset` | TEXT | Mandatory | Dataset where raw value came from |
| `crosswalk_type` | TEXT | Mandatory | organism / drug / gene / country / specimen / age_group / gender / infection_origin |
| `raw_value` | TEXT | Mandatory | Original value from source data |
| `mapped_identifier` | TEXT | Mandatory | Canonical identifier assigned |
| `mapped_name` | TEXT | Mandatory | Standard name assigned |
| `confidence` | TEXT | Mandatory | exact / fuzzy / manual / unknown |
| `mapped_at` | TIMESTAMPTZ | Mandatory | When mapping was made |
| `mapped_by` | TEXT | Optional | Person or system that made mapping |

## Categorical Crosswalks and Loss Definitions
MARS v0.4 extends crosswalk tracking beyond entity identifiers (organism, drug, gene, country) to categorical fields: `specimen`, `age_group`, `gender`, and `infection_origin`. Categorical mappings are recorded using `crosswalk_tables/categorical_crosswalk_template.csv` with fields:
`field,source_system,source_value,mars_value,loss,notes`

Mapping categorical values may entail information loss. The `loss` field in categorical crosswalk tables records this:
- `none`: 1:1 mapping with no loss of semantic precision (e.g. GLASS `BLOOD` -> MARS `Blood`).
- `many_to_one`: several source values share one MARS value; source detail survives only in `*_raw` (e.g. GLASS `LOWRESP` -> MARS `Respiratory`, which covers both upper- and lower-tract specimens; or hospital ward types `in`, `inx`, `int` -> `General Ward`).
- `no_equivalent`: source concept has no direct counterpart in MARS and is mapped to `Other` or `Unknown`; source detail is not recoverable from the standard MARS fields alone (e.g. GLASS `ANORECTAL` -> MARS `Other`).

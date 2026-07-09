# Data Dictionary: harmonised.crosswalk_log

Audit trail of every mapping decision. This is the standardisation evidence.

| Field | Type | Status | Description |
|---|---|---|---|
| `source_dataset` | TEXT | Mandatory | Dataset where raw value came from |
| `crosswalk_type` | TEXT | Mandatory | organism / drug / gene / country |
| `raw_value` | TEXT | Mandatory | Original value from source data |
| `mapped_identifier` | TEXT | Mandatory | Canonical identifier assigned |
| `mapped_name` | TEXT | Mandatory | Standard name assigned |
| `confidence` | TEXT | Mandatory | exact / fuzzy / manual / unknown |
| `mapped_at` | TIMESTAMPTZ | Mandatory | When mapping was made |
| `mapped_by` | TEXT | Optional | Person or system that made mapping |

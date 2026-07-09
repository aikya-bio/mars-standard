-- MARS Schema v0.1
-- Database: PostgreSQL

CREATE SCHEMA IF NOT EXISTS harmonised;

CREATE TABLE harmonised.isolates (
    isolate_id TEXT NOT NULL,
    source_dataset TEXT NOT NULL,
    loaded_at TIMESTAMPTZ NOT NULL,
    ncbi_taxonomy_id INTEGER NOT NULL,
    organism_name_standard TEXT NOT NULL,
    gram_type TEXT NOT NULL,
    organism_group TEXT,
    country_iso CHAR(2) NOT NULL,
    region_un_m49 TEXT,
    year_collected SMALLINT NOT NULL,
    specimen_type TEXT,
    facility_type TEXT,
    age_group TEXT,
    gender TEXT,
    nosocomial BOOLEAN,
    infection_type TEXT,
    subtype TEXT,
    has_genotype_data BOOLEAN NOT NULL,
    metadata JSONB,
    PRIMARY KEY (isolate_id, source_dataset)
);

CREATE TABLE harmonised.mic_observations (
    isolate_id TEXT NOT NULL,
    source_dataset TEXT NOT NULL,
    chembl_id TEXT NOT NULL,
    drug_name_standard TEXT NOT NULL,
    drug_class TEXT,
    aware_category TEXT,
    mic_numeric DECIMAL NOT NULL,
    mic_qualifier TEXT NOT NULL,
    interpretation_raw TEXT,
    interpretation_standard TEXT,
    breakpoint_system TEXT,
    breakpoint_version TEXT,
    FOREIGN KEY (isolate_id, source_dataset) REFERENCES harmonised.isolates (isolate_id, source_dataset)
);

CREATE TABLE harmonised.genotype_observations (
    isolate_id TEXT NOT NULL,
    source_dataset TEXT NOT NULL,
    gene_aro_id TEXT,
    gene_name_standard TEXT,
    phenotypic_class TEXT,
    betalactamase_status TEXT,
    hgvs_notation TEXT,
    variant_type TEXT,
    raw_notation TEXT,
    FOREIGN KEY (isolate_id, source_dataset) REFERENCES harmonised.isolates (isolate_id, source_dataset)
);

CREATE TABLE harmonised.crosswalk_log (
    source_dataset TEXT NOT NULL,
    crosswalk_type TEXT NOT NULL,
    raw_value TEXT NOT NULL,
    mapped_identifier TEXT NOT NULL,
    mapped_name TEXT NOT NULL,
    confidence TEXT NOT NULL,
    mapped_at TIMESTAMPTZ NOT NULL,
    mapped_by TEXT
);

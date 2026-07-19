-- MARS Schema v0.1
-- Database: SQLite

CREATE TABLE isolates (
    isolate_id TEXT NOT NULL,
    source_dataset TEXT NOT NULL,
    loaded_at TEXT NOT NULL,
    ncbi_taxonomy_id INTEGER NOT NULL,
    organism_name_standard TEXT NOT NULL,
    gram_type TEXT NOT NULL CHECK (gram_type IN ('Gram-negative', 'Gram-positive', 'Fungal', 'Mycobacteria', 'Unknown')),
    organism_group TEXT CHECK (organism_group IN ('Enterobacterales', 'Non-fermenters', 'Streptococci', 'Staphylococci', 'Enterococci', 'Candida', 'Other', 'Unknown')),
    country_iso TEXT NOT NULL,
    region_un_m49 TEXT,
    year_collected INTEGER NOT NULL,
    specimen_type TEXT CHECK (specimen_type IN ('Blood', 'Urine', 'Respiratory', 'Wound', 'CSF', 'Skin/Soft Tissue', 'Intra-abdominal', 'Bone/Joint', 'Eye', 'Other', 'Unknown')),
    facility_type TEXT CHECK (facility_type IN ('ICU', 'General Ward', 'Community', 'Outpatient', 'Long-term Care', 'Unknown')),
    age_group TEXT CHECK (age_group IN ('0–2', '3–17', '18–64', '65+', 'Unknown')),
    gender TEXT CHECK (gender IN ('M', 'F', 'Unknown')),
    nosocomial INTEGER,
    infection_type TEXT CHECK (infection_type IN ('BSI', 'UTI', 'Pneumonia', 'Wound', 'IAI', 'HAP', 'SSTI', 'Other', 'Unknown')),
    subtype TEXT,
    has_genotype_data INTEGER NOT NULL,
    metadata TEXT,
    PRIMARY KEY (isolate_id, source_dataset)
);

CREATE TABLE mic_observations (
    isolate_id TEXT NOT NULL,
    source_dataset TEXT NOT NULL,
    chembl_id TEXT NOT NULL,
    drug_name_standard TEXT NOT NULL,
    drug_class TEXT,
    aware_category TEXT CHECK (aware_category IN ('Access', 'Watch', 'Reserve', 'Unknown')),
    mic_numeric REAL NOT NULL,
    mic_qualifier TEXT NOT NULL CHECK (mic_qualifier IN ('=', '>', '<', '>=', '<=')),
    interpretation_raw TEXT,
    interpretation_standard TEXT CHECK (interpretation_standard IN ('S', 'I', 'R', 'Unknown')),
    breakpoint_system TEXT CHECK (breakpoint_system IN ('CLSI', 'EUCAST', 'Unknown')),
    breakpoint_version TEXT,
    FOREIGN KEY (isolate_id, source_dataset) REFERENCES isolates (isolate_id, source_dataset)
);

CREATE TABLE genotype_observations (
    isolate_id TEXT NOT NULL,
    source_dataset TEXT NOT NULL,
    gene_aro_id TEXT,
    gene_name_standard TEXT,
    phenotypic_class TEXT,
    betalactamase_status TEXT CHECK (betalactamase_status IN ('POS', 'NEG', 'Unknown')),
    hgvs_notation TEXT,
    variant_type TEXT CHECK (variant_type IN ('nucleotide', 'amino_acid', 'Unknown')),
    raw_notation TEXT,
    FOREIGN KEY (isolate_id, source_dataset) REFERENCES isolates (isolate_id, source_dataset)
);

CREATE TABLE crosswalk_log (
    source_dataset TEXT NOT NULL,
    crosswalk_type TEXT NOT NULL CHECK (crosswalk_type IN ('organism', 'drug', 'gene', 'country')),
    raw_value TEXT NOT NULL,
    mapped_identifier TEXT NOT NULL,
    mapped_name TEXT NOT NULL,
    confidence TEXT NOT NULL CHECK (confidence IN ('exact', 'fuzzy', 'manual', 'unknown')),
    mapped_at TEXT NOT NULL,
    mapped_by TEXT
);

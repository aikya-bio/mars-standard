# MARS Reference Implementation

This directory contains standalone Python reference scripts demonstrating how to normalise and map surveillance data to the MARS standard. 

> [!NOTE]
> **Data Provenance:** The example data in `example_data/` is entirely synthetic. It uses real biological names from literature to demonstrate edge cases, but does not contain data from any real-world surveillance dataset.

## Scripts Included

1. `mic_normaliser.py`: Parses raw MIC strings (e.g. `>64`, `<=0.015`, `64.0001`) into the MARS `{numeric, qualifier}` format.
2. `chembl_lookup.py`: Maps drug names and WHONET abbreviations to ChEMBL IDs and WHO AWaRe 2023 categories.
3. `ncbi_taxonomy_lookup.py`: Maps organism names (including abbreviations and misspellings) to NCBI Taxonomy IDs.
4. `aro_lookup.py`: Maps resistance gene names to the Comprehensive Antibiotic Resistance Database (CARD) ARO ontology.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **One-Time ARO Setup:**
   The `aro_lookup.py` script requires a local copy of the CARD ontology (OBO file). This ensures mappings are version-locked and doesn't hammer the CARD APIs.
   ```bash
   mkdir -p data
   curl -L https://card.mcmaster.ca/latest/ontology -o data/aro.obo
   ```

## Usage

```bash
# Run the MIC normaliser tests
python mic_normaliser.py

# Run the API lookups
python chembl_lookup.py
python ncbi_taxonomy_lookup.py
python aro_lookup.py
```

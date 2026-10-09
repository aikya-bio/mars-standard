"""
MARS Reference Implementation: ChEMBL Lookup

Maps raw drug names to ChEMBL IDs. Demonstrates caching to avoid redundant API calls.

Illustrative only: the abbreviation map covers a handful of common drugs, and the
`aware_category` value is a placeholder, NOT a lookup against the WHO AWaRe
classification. A production crosswalk should use a versioned copy of the WHO AWaRe
list and the full WHONET antibiotic dictionary.
"""
import json
import os
import re
import requests

CACHE_FILE = 'chembl_cache.json'
CHEMBL_API = 'https://www.ebi.ac.uk/chembl/api/data/molecule.json'

# Example three-letter abbreviation map (illustrative subset, not the WHONET code list)
ABBREVIATION_MAP = {
    'MEM': 'Meropenem',
    'TZP': 'Piperacillin/tazobactam',
    'CTX': 'Cefotaxime',
    'CRO': 'Ceftriaxone',
    'CIP': 'Ciprofloxacin',
    'AMK': 'Amikacin'
}

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache_data):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache_data, f, indent=2)

def clean_drug_name(raw_name: str) -> str:
    # Remove example suffixes such as _MIC and _ND (WHONET-style test codes such as
    # AMP_ND10 carry additional method/content suffixes and are not handled here)
    cleaned = re.sub(r'_(MIC|ND)$', '', raw_name.strip(), flags=re.IGNORECASE)
    # Check if it's a known abbreviation
    return ABBREVIATION_MAP.get(cleaned.upper(), cleaned)

def lookup_drug(raw_name: str, cache: dict = None) -> dict:
    if cache is None:
        cache = load_cache()
        
    cleaned_name = clean_drug_name(raw_name)
    
    # Return from cache if available
    if cleaned_name.lower() in cache:
        return cache[cleaned_name.lower()]
        
    print(f"Querying ChEMBL for: {cleaned_name}")
    try:
        response = requests.get(CHEMBL_API, params={'pref_name__iexact': cleaned_name})
        response.raise_for_status()
        data = response.json()
        
        molecules = data.get('molecules', [])
        if molecules:
            best_match = molecules[0]
            chembl_id = best_match.get('molecule_chembl_id')
            standard_name = best_match.get('pref_name') or cleaned_name
            # PLACEHOLDER: AWaRe is not resolved here. A full implementation would
            # cross-reference the ChEMBL ID or name against a versioned copy of the WHO AWaRe list.
            aware = "Unknown"
            
            result = {
                'chembl_id': chembl_id,
                'standard_name': standard_name,
                'aware_category': aware,
                'confidence': 'exact'
            }
            cache[cleaned_name.lower()] = result
            save_cache(cache)
            return result
            
    except requests.RequestException as e:
        print(f"API Error for {cleaned_name}: {e}")
        
    result = {'chembl_id': None, 'standard_name': None, 'aware_category': 'Unknown', 'confidence': 'unknown'}
    cache[cleaned_name.lower()] = result
    save_cache(cache)
    return result

if __name__ == "__main__":
    print("Testing ChEMBL Lookup...")
    cache = load_cache()
    test_cases = ['MEM', 'TZP_MIC', 'Amoxicillin']
    for t in test_cases:
        res = lookup_drug(t, cache)
        print(f"{t.ljust(15)} -> {res}")

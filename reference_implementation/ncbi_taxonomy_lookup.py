"""
MARS Reference Implementation: NCBI Taxonomy Lookup

Maps organism names to NCBI Taxonomy IDs using Biopython.
Includes a pre-verified map for common pathogens to minimise API usage.
"""
import json
import os
from Bio import Entrez

# ALWAYS set your email before using Entrez!
Entrez.email = "open-source@aikya.bio"

CACHE_FILE = 'organism_taxonomy_cache.json'

# Pre-verified map for the most common AMR pathogens (skips API call)
PRE_VERIFIED_MAP = {
    'k. pneumoniae': {'ncbi_taxonomy_id': 573, 'standard_name': 'Klebsiella pneumoniae', 'gram_type': 'Gram-negative', 'organism_group': 'Enterobacterales', 'confidence': 'pre_verified'},
    'e. coli': {'ncbi_taxonomy_id': 562, 'standard_name': 'Escherichia coli', 'gram_type': 'Gram-negative', 'organism_group': 'Enterobacterales', 'confidence': 'pre_verified'},
    's. aureus': {'ncbi_taxonomy_id': 1280, 'standard_name': 'Staphylococcus aureus', 'gram_type': 'Gram-positive', 'organism_group': 'Staphylococci', 'confidence': 'pre_verified'},
    'p. aeruginosa': {'ncbi_taxonomy_id': 287, 'standard_name': 'Pseudomonas aeruginosa', 'gram_type': 'Gram-negative', 'organism_group': 'Non-fermenters', 'confidence': 'pre_verified'}
}

def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_cache(cache_data):
    with open(CACHE_FILE, 'w') as f:
        json.dump(cache_data, f, indent=2)

def lookup_organism(raw_name: str, cache: dict = None) -> dict:
    if cache is None:
        cache = load_cache()
        
    cleaned_name = raw_name.strip().lower()
    
    # 1. Check pre-verified map
    if cleaned_name in PRE_VERIFIED_MAP:
        return PRE_VERIFIED_MAP[cleaned_name]
        
    # 2. Check local cache
    if cleaned_name in cache:
        return cache[cleaned_name]
        
    print(f"Querying NCBI Entrez for: {raw_name}")
    try:
        # Search taxonomy database
        handle = Entrez.esearch(db="taxonomy", term=raw_name)
        record = Entrez.read(handle)
        handle.close()
        
        if record["IdList"]:
            tax_id = record["IdList"][0]
            # Fetch details
            handle = Entrez.efetch(db="taxonomy", id=tax_id, retmode="xml")
            details = Entrez.read(handle)
            handle.close()
            
            scientific_name = details[0]["ScientificName"]
            lineage = details[0].get("Lineage", "")
            
            # Simple heuristic for gram type and group based on lineage
            gram_type = "Unknown"
            group = "Other"
            if "Enterobacterales" in lineage:
                gram_type = "Gram-negative"
                group = "Enterobacterales"
            elif "Pseudomonadales" in lineage:
                gram_type = "Gram-negative"
                group = "Non-fermenters"
                
            result = {
                'ncbi_taxonomy_id': int(tax_id),
                'standard_name': scientific_name,
                'gram_type': gram_type,
                'organism_group': group,
                'confidence': 'exact',
                'needs_review': "spp" in raw_name.lower() or "genus" in raw_name.lower()
            }
            cache[cleaned_name] = result
            save_cache(cache)
            return result
            
    except Exception as e:
        print(f"NCBI API Error for {raw_name}: {e}")
        
    result = {'ncbi_taxonomy_id': None, 'standard_name': None, 'gram_type': 'Unknown', 'organism_group': 'Unknown', 'confidence': 'unknown'}
    cache[cleaned_name] = result
    save_cache(cache)
    return result

if __name__ == "__main__":
    print("Testing NCBI Taxonomy Lookup...")
    cache = load_cache()
    test_cases = ['K. pneumoniae', 'Acinetobacter baumannii', 'Klesiella spp.']
    for t in test_cases:
        res = lookup_organism(t, cache)
        print(f"{t.ljust(25)} -> {res}")

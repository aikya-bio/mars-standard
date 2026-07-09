"""
MARS Reference Implementation: ARO Gene Lookup

Parses the CARD OBO file to map resistance genes to ARO IDs.
Handles comma-separated lists and simple variant stripping.
"""
import os
import re

def load_aro_index(obo_path: str = 'data/aro.obo') -> dict:
    """
    Parses the OBO file into a fast lookup dictionary.
    Keys are lowercased gene names/synonyms, values are ARO IDs.
    """
    index = {}
    if not os.path.exists(obo_path):
        print(f"Warning: {obo_path} not found. Returning empty index.")
        print("Run: curl -L https://card.mcmaster.ca/latest/ontology -o data/aro.obo")
        return index
        
    current_id = None
    current_name = None
    
    with open(obo_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('[Term]'):
                current_id = None
                current_name = None
            elif line.startswith('id: ARO:'):
                current_id = line.replace('id: ', '')
            elif line.startswith('name: '):
                current_name = line.replace('name: ', '')
                if current_id and current_name:
                    index[current_name.lower()] = current_id
            elif line.startswith('synonym: '):
                # Extract exact synonyms
                match = re.match(r'synonym:\s*"([^"]+)"\s*EXACT', line)
                if match and current_id:
                    index[match.group(1).lower()] = current_id
                    
    return index

def lookup_gene(raw_name: str, index: dict) -> list:
    """
    Looks up a gene string, which may contain multiple comma-separated genes.
    Returns a list of dicts: [{'gene_aro_id', 'gene_name_standard', 'phenotypic_class', 'confidence'}]
    """
    results = []
    
    # Split by comma or slash
    genes = re.split(r'[,/]', str(raw_name))
    
    for gene in genes:
        gene = gene.strip()
        if not gene: continue
        
        # Strip common variant mutations for the baseline lookup (e.g. rpoB S450L -> rpoB)
        base_gene = re.sub(r'\s+[A-Z]\d+[A-Z\*]$', '', gene)
        
        lookup_term = base_gene.lower()
        
        if lookup_term in index:
            results.append({
                'gene_aro_id': index[lookup_term],
                'gene_name_standard': base_gene, # In a full system, you'd pull the canonical name from the OBO
                'phenotypic_class': 'Unknown',   # Requires traversing the OBO hierarchy
                'confidence': 'exact'
            })
        else:
            results.append({
                'gene_aro_id': None,
                'gene_name_standard': gene,
                'phenotypic_class': 'Unknown',
                'confidence': 'unknown'
            })
            
    return results

if __name__ == "__main__":
    print("Testing ARO Lookup...")
    # This requires data/aro.obo to exist. 
    # If it doesn't, we will just simulate an empty index behavior.
    index = load_aro_index()
    if index:
        test_cases = ['TEM-1', 'SHV-18, CTX-M', 'rpoB S450L']
        for t in test_cases:
            res = lookup_gene(t, index)
            print(f"{t.ljust(20)} -> {res}")

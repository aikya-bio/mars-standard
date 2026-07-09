"""
MARS Reference Implementation: MIC Normaliser

Normalises a raw MIC string from clinical systems into the MARS two-field standard.
Handles float underflow/overflow, inequalities, and plain decimals.
"""
import re

def normalise_mic(raw_mic: str) -> dict:
    """
    Parses a raw MIC string.
    Returns: {'numeric': float, 'qualifier': str ('=', '>', '<', '>=', '<=')}
    """
    raw = str(raw_mic).strip()
    if not raw:
        return {'numeric': None, 'qualifier': None}

    # Extract optional qualifier and numeric value using regex
    # Matches: <=, >=, <, >, =, or nothing, followed by numbers/decimals
    match = re.match(r'(<=|>=|<|>|=)?\s*([0-9]*\.?[0-9]+)$', raw)
    
    if not match:
        # Check for float overflow/underflow artifacts from some LIMS systems
        # E.g. 64.0001 -> >64
        # E.g. 0.0599 -> <0.06
        try:
            val = float(raw)
            str_val = f"{val:.4f}"
            if str_val.endswith("0001"):
                base = round(val)
                return {'numeric': float(base), 'qualifier': '>'}
            elif str_val.endswith("99"):
                base = round(val, 2)
                return {'numeric': float(base), 'qualifier': '<'}
        except ValueError:
            pass
        return {'numeric': None, 'qualifier': None}

    qualifier = match.group(1) or '='
    numeric_str = match.group(2)
    numeric_val = float(numeric_str)
    
    return {
        'numeric': numeric_val,
        'qualifier': qualifier
    }

if __name__ == "__main__":
    # Internal test suite
    test_cases = [
        ('64.0001', {'numeric': 64.0, 'qualifier': '>'}),
        ('0.0599', {'numeric': 0.06, 'qualifier': '<'}),
        ('<=0.015', {'numeric': 0.015, 'qualifier': '<='}),
        ('>128', {'numeric': 128.0, 'qualifier': '>'}),
        ('2.0', {'numeric': 2.0, 'qualifier': '='}),
        ('16', {'numeric': 16.0, 'qualifier': '='}),
        ('< 0.5', {'numeric': 0.5, 'qualifier': '<'})
    ]
    
    passed = 0
    for raw, expected in test_cases:
        result = normalise_mic(raw)
        assert result == expected, f"Failed on {raw}: got {result}, expected {expected}"
        passed += 1
        
    print(f"Passed {passed}/{len(test_cases)} tests.")

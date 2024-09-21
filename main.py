import re
from difflib import get_close_matches

# Dictionary of common abbreviations for company suffixes
suffix_abbreviations = {
    "corp": "corporation",
    "inc": "incorporated",
    "ltd": "limited",
    "co": "company"
}

def normalize_name(name):
    # Replace dashes with spaces
    name = name.replace('-', ' ')

    # Remove common prefix "the"
    name = re.sub(r'^\bthe\b\s+', '', name, flags=re.IGNORECASE)
    
    # Replace suffix abbreviations
    for abbr, full in suffix_abbreviations.items():
        name = re.sub(r'\b' + abbr + r'\b', full, name, flags=re.IGNORECASE)
    return name.lower()

def find_closest_match(name_to_match, reference_names):
    # Normalize the name to match
    normalized_name_to_match = normalize_name(name_to_match)
    
    # Normalize all reference names
    normalized_reference_names = [normalize_name(name) for name in reference_names]
    
    # Find the closest match using edit distance
    closest_matches = get_close_matches(normalized_name_to_match, normalized_reference_names, n=1, cutoff=0.6)
    if closest_matches:
        return closest_matches[0]
    else:
        return None
#
# Example usage
#
reference_names = ["The Corporation", "Acme Inc", "Global Ltd", "Tech-Co"]
name_to_match = "Acme Corporation"
closest_match = find_closest_match(name_to_match, reference_names)
print(f"The closest match for '{name_to_match}' is '{closest_match}'")

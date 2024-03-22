# Prompt: return everything after the "_" in input
# Input: '2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'
# Output: 'HEEN PAX 77820'

def extract_after_underscore(input_str):
    return input_str.split('_')[1]

# Test cases
print(extract_after_underscore('2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'))  # Output: 'HEEN PAX 77820'
print(extract_after_underscore('44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'))  # Output: 'PAX'
print(extract_after_underscore('PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'))  # Output: 'BOX 4403 PAX SSKA'

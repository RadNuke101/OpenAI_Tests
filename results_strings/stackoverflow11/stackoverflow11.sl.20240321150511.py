# Prompt: return everything after the "_" in input
# Input: '2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'
# Output: 'HEEN PAX 77820'

def get_output(input_str):
    split_input = input_str.split("_")
    if len(split_input) > 1:
        return split_input[1].strip()
    else:
        return ""

# Test cases
print(get_output('2283-332-44543 CAP DDT PPL445_ HEEN PAX 77820'))  # Output: 'HEEN PAX 77820'
print(get_output('44372-33-3223 TYYTE CAP BOX 1550 244 BOX PPSSA223_ PAX'))  # Output: 'PAX'
print(get_output('PRECISE 77 CLEAR BLUE 99WIE_ BOX 4403 PAX SSKA'))  # Output: 'BOX 4403 PAX SSKA'

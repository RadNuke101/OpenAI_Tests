# Prompt: return the number from input
# Input: '<b>0.66<b>'
# Output: 0.66

def extract_number(input_str):
    return float(input_str.strip('<b>').strip('</b>'))

# Test cases
print(extract_number('<b>0.66<b>'))  # Output: 0.66
print(extract_number('<b>0.409<b>'))  # Output: 0.409
print(extract_number('<b>0.7268<b>'))  # Output: 0.7268

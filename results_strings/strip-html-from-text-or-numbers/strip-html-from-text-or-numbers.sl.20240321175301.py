# Prompt: return the number from input
# Input: '<b>0.66<b>'
# Output: 0.66

def extract_number(input_str):
    start_index = input_str.find('<b>') + 3
    end_index = input_str.find('<', start_index)
    return float(input_str[start_index:end_index])

# Test cases
print(extract_number('<b>0.66<b>'))  # Output: 0.66
print(extract_number('<b>0.409<b>'))  # Output: 0.409
print(extract_number('<b>0.7268<b>'))  # Output: 0.7268

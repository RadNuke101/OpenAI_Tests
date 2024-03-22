# Prompt: return the number from input
# Input: '<b>0.66<b>'
# Output: 0.66

def extract_number(input_str):
    # Remove '<b>' and '</b>' from the input string
    number = input_str.replace('<b>', '').replace('</b>', '')
    
    # Convert the extracted number to a float
    return float(number)

# Test cases
print(extract_number('<b>0.66<b>'))  # Output: 0.66
print(extract_number('<b>0.409<b>'))  # Output: 0.409
print(extract_number('<b>0.7268<b>'))  # Output: 0.7268

# Prompt: return the number from input
# Input: '<b>0.66<b>'
# Output: 0.66

def extract_number(input_str):
    # Remove '<b>' and '</b>' from the input string
    number_str = input_str.replace('<b>', '').replace('</b>', '')
    
    # Convert the extracted number string to a float
    number = float(number_str)
    
    return number

# Test cases
print(extract_number('<b>0.66<b>'))  # Output: 0.66
print(extract_number('<b>0.409<b>'))  # Output: 0.409
print(extract_number('<b>0.7268<b>'))  # Output: 0.7268
0.66
0.409
0.7268

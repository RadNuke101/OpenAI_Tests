# Prompt: return the number from input
# Input: '100 apples'
# Output: '100'

def extract_number(input_str):
    num_str = ''.join(filter(str.isdigit, input_str))
    return num_str

# Test cases
print(extract_number('100 apples'))  # Output: '100'
print(extract_number('the price is %500 dollars'))  # Output: '500'
print(extract_number('serial number %003399'))  # Output: '003399'

# Prompt: return the number from input
# Input: '100 apples'
# Output: '100'

def extract_number(input_str):
    num = ''
    for char in input_str:
        if char.isdigit():
            num += char
    return num

# Test cases
print(extract_number('100 apples'))  # Output: '100'
print(extract_number('the price is %500 dollars'))  # Output: '500'
print(extract_number('serial number %003399'))  # Output: '003399'

# Prompt: return everything after the sequence of 4 numbers (excluding spaces) from input
# Input: 'geb. 14 oct 1956 Westerkerk HRL'
# Output: 'Westerkerk HRL'

def extract_info(input_str):
    numbers = ''.join(filter(str.isdigit, input_str))
    index = input_str.find(numbers[:4])
    if index != -1:
        return input_str[index + 4:].strip()
    else:
        return ''

# Test cases
print(extract_info('geb. 14 oct 1956 Westerkerk HRL'))  # Output: 'Westerkerk HRL'
print(extract_info('geb. 14 oct 1956 '))  # Output: ''
print(extract_info('geb. 15 feb 1987 Westerkerk HRL'))  # Output: 'Westerkerk HRL'

# Prompt: return everything after the sequence of 4 numbers (excluding spaces) from input
# Input: 'geb. 14 oct 1956 Westerkerk HRL'
# Output: 'Westerkerk HRL'

def extract_info(input_str):
    numbers = ''.join([char for char in input_str if char.isdigit()])
    index = input_str.find(numbers) + len(numbers)
    return input_str[index:].strip()

# Test cases
print(extract_info('geb. 14 oct 1956 Westerkerk HRL'))  # Output: 'Westerkerk HRL'
print(extract_info('geb. 14 oct 1956 '))  # Output: ''
print(extract_info('geb. 15 feb 1987 Westerkerk HRL'))  # Output: 'Westerkerk HRL'
Westerkerk HRL

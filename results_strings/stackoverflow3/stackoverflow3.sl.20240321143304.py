# Prompt: return everything after the sequence of 4 numbers (excluding spaces) from input
# Input: ['geb. 14 oct 1956 Westerkerk HRL']
# Output: Westerkerk HRL

def extract_info(input_str):
    numbers = '0123456789'
    count = 0
    for char in input_str:
        if char in numbers:
            count += 1
            if count == 4:
                return input_str[input_str.index(char)+4:].strip()
    return ''

# Test cases
print(extract_info('geb. 14 oct 1956 Westerkerk HRL'))  # Output: Westerkerk HRL
print(extract_info('geb. 14 oct 1956 '))  # Output: 
print(extract_info('geb. 15 feb 1987 Westerkerk HRL'))  # Output: Westerkerk HRL

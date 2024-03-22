# Prompt: return the three numbers in between "-" in input
# Input: '+106 769-858-438'
# Output: '858'

def extract_numbers(input_str):
    numbers = input_str.split('-')
    return numbers[1]

# Test cases
print(extract_numbers('+106 769-858-438'))  # Output: '858'
print(extract_numbers('+83 973-757-831'))   # Output: '757'
print(extract_numbers('+62 647-787-775'))   # Output: '787'
print(extract_numbers('+172 027-507-632'))  # Output: '507'
print(extract_numbers('+72 001-050-856'))   # Output: '050'
print(extract_numbers('+95 310-537-401'))   # Output: '537'
print(extract_numbers('+6 775-969-238'))    # Output: '969'

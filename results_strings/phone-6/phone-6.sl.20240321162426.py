# Prompt: return first three numbers after the first space in input
# Input: '+106 769-858-438'
# Output: '769'

def extract_numbers_after_space(input_str):
    space_index = input_str.index(' ')
    numbers = input_str[space_index+1:space_index+4]
    return numbers

# Test cases
print(extract_numbers_after_space('+106 769-858-438'))  # Output: '769'
print(extract_numbers_after_space('+83 973-757-831'))    # Output: '973'
print(extract_numbers_after_space('+62 647-787-775'))    # Output: '647'
print(extract_numbers_after_space('+172 027-507-632'))   # Output: '027'
print(extract_numbers_after_space('+72 001-050-856'))    # Output: '001'
print(extract_numbers_after_space('+95 310-537-401'))    # Output: '310'
print(extract_numbers_after_space('+6 775-969-238'))     # Output: '775'

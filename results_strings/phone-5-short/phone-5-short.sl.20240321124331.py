# Prompt: return first three numbers in input
# Input: '+106 769-858-438', Output: '106'
# Input: '+83 973-757-831', Output: '83'
# Input: '+62 647-787-775', Output: '62'
# Input: '+172 027-507-632', Output: '172'
# Input: '+72 001-050-856', Output: '72'
# Input: '+95 310-537-401', Output: '95'
# Input: '+6 775-969-238', Output: '6'

def extract_first_three_numbers(input_str):
    return input_str.split()[0][1:]

# Test cases
print(extract_first_three_numbers('+106 769-858-438'))  # Output: '106'
print(extract_first_three_numbers('+83 973-757-831'))   # Output: '83'
print(extract_first_three_numbers('+62 647-787-775'))   # Output: '62'
print(extract_first_three_numbers('+172 027-507-632'))  # Output: '172'
print(extract_first_three_numbers('+72 001-050-856'))   # Output: '72'
print(extract_first_three_numbers('+95 310-537-401'))   # Output: '95'
print(extract_first_three_numbers('+6 775-969-238'))    # Output: '6'

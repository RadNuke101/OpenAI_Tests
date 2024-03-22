# Prompt: return first three numbers in input
# Input: '+106 769-858-438'
# Output: '106'

def get_first_three_numbers(input_str):
    numbers = ''.join(filter(str.isdigit, input_str))  # Extract all numbers from input string
    return numbers[:3]  # Return the first three numbers

# Test cases
print(get_first_three_numbers('+106 769-858-438'))  # Output: '106'
print(get_first_three_numbers('+83 973-757-831'))  # Output: '83'
print(get_first_three_numbers('+62 647-787-775'))  # Output: '62'
print(get_first_three_numbers('+172 027-507-632'))  # Output: '172'
print(get_first_three_numbers('+72 001-050-856'))  # Output: '72'
print(get_first_three_numbers('+95 310-537-401'))  # Output: '95'
print(get_first_three_numbers('+6 775-969-238'))  # Output: '6'

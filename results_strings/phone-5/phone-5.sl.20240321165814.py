# Prompt: return first three numbers in input
# Input: '+106 769-858-438'
# Output: '106'

def return_first_three_numbers(input_str):
    output = input_str.split()[0][1:]
    return output

# Test cases
print(return_first_three_numbers('+106 769-858-438'))  # Output: '106'
print(return_first_three_numbers('+83 973-757-831'))   # Output: '83'
print(return_first_three_numbers('+62 647-787-775'))   # Output: '62'
print(return_first_three_numbers('+172 027-507-632'))  # Output: '172'
print(return_first_three_numbers('+72 001-050-856'))   # Output: '72'
print(return_first_three_numbers('+95 310-537-401'))   # Output: '95'
print(return_first_three_numbers('+6 775-969-238'))    # Output: '6'

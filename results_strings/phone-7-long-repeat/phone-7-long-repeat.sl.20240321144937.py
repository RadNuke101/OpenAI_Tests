def get_numbers_between_dash(input_str):
    # Prompt: return the three numbers in between "-" in input
    # Input: '+106 769-858-438'
    # Output: '858'
    
    # Extract the numbers between the dashes
    numbers = input_str.split('-')[1:-1]
    
    # Join the numbers into a single string
    output = ''.join(numbers)
    
    return output

# Test the function with the provided inputs
print(get_numbers_between_dash('+106 769-858-438'))  # Output: '858'
print(get_numbers_between_dash('+83 973-757-831'))   # Output: '757'
print(get_numbers_between_dash('+62 647-787-775'))   # Output: '787'
print(get_numbers_between_dash('+172 027-507-632'))  # Output: '507'
print(get_numbers_between_dash('+72 001-050-856'))   # Output: '050'
print(get_numbers_between_dash('+95 310-537-401'))   # Output: '537'
print(get_numbers_between_dash('+6 775-969-238'))    # Output: '969'
print(get_numbers_between_dash('+174 594-539-946'))  # Output: '539'
print(get_numbers_between_dash('+155 927-275-860'))  # Output: '275'
print(get_numbers_between_dash('+167 405-461-331'))  # Output: '461'
858
757
787
507
050
537
969
539
275
461

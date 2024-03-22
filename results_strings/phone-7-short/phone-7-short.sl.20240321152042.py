def get_numbers_between_dash(input_str):
    # Prompt: return the three numbers in between "-" in input
    input_str = input_str.split('-')
    output = input_str[1]
    return output

# Test cases
print(get_numbers_between_dash('+106 769-858-438'))  # Output: 858
print(get_numbers_between_dash('+83 973-757-831'))    # Output: 757
print(get_numbers_between_dash('+62 647-787-775'))    # Output: 787
print(get_numbers_between_dash('+172 027-507-632'))   # Output: 507
print(get_numbers_between_dash('+72 001-050-856'))    # Output: 050
print(get_numbers_between_dash('+95 310-537-401'))    # Output: 537
print(get_numbers_between_dash('+6 775-969-238'))     # Output: 969

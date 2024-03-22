# Prompt: return input with parentheses around the first three numbers before the first "-", delete the first "-" and replace it with a space
# Input: '+106 769-858-438'
# Output: +106 (769) 858-438

def format_phone_number(input_str):
    parts = input_str.split('-')
    first_three = parts[0][-3:]
    new_input = input_str.replace('-', ' ', 1)
    new_input = new_input.replace(first_three, '(' + first_three + ')', 1)
    return new_input

# Test the function with the given inputs
print(format_phone_number('+106 769-858-438'))
print(format_phone_number('+83 973-757-831'))
print(format_phone_number('+62 647-787-775'))
print(format_phone_number('+172 027-507-632'))
print(format_phone_number('+72 001-050-856'))

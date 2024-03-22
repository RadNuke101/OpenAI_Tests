def format_phone_number(input_str):
    input_str = input_str[0]
    first_part = input_str.split('-')[0]
    first_three_nums = first_part.split()[1][:3]
    output = input_str.replace('-', ' ', 1).replace(first_three_nums, f'({first_three_nums})', 1)
    return output

# Prompt: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space
# Input: ['+106 769-858-438']
# Output: +106 (769) 858-438

# Test cases
print(format_phone_number(['+106 769-858-438']))
print(format_phone_number(['+83 973-757-831']))
print(format_phone_number(['+62 647-787-775']))
print(format_phone_number(['+172 027-507-632']))
print(format_phone_number(['+72 001-050-856']))

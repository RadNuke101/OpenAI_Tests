def format_phone_number(input_str):
    # input: ['+106 769-858-438']
    # output: +106 (769) 858-438
    input_str = input_str[0]
    first_three_nums = input_str.split()[1][:3]
    formatted_num = input_str.replace('-', ' ', 1).replace(first_three_nums, f'({first_three_nums})', 1)
    return formatted_num

# Test cases
print(format_phone_number(['+106 769-858-438']))  # Output: +106 (769) 858-438
print(format_phone_number(['+83 973-757-831']))  # Output: +83 (973) 757-831
print(format_phone_number(['+62 647-787-775']))  # Output: +62 (647) 787-775
print(format_phone_number(['+172 027-507-632']))  # Output: +172 (027) 507-632
print(format_phone_number(['+72 001-050-856']))  # Output: +72 (001) 050-856
print(format_phone_number(['+95 310-537-401']))  # Output: +95 (310) 537-401

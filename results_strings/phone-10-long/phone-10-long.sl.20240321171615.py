def format_phone_number(input_str):
    # Prompt: return input with parentheses around the first three numbers before the first "-", 
    # and delete the first "-" and replace it with a space
    input_str = input_str.replace("-", " ", 1)
    first_three_nums = input_str.split()[1][:3]
    input_str = input_str.replace(first_three_nums, "(" + first_three_nums + ")", 1)
    return input_str

# Test cases
print(format_phone_number('+106 769-858-438'))  # Output: +106 (769) 858-438
print(format_phone_number('+83 973-757-831'))   # Output: +83 (973) 757-831
print(format_phone_number('+62 647-787-775'))   # Output: +62 (647) 787-775

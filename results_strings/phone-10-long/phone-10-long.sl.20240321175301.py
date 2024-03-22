def format_phone_number(input_str):
    input_str = input_str[0]
    parts = input_str.split("-")
    first_three_nums = "(" + parts[0][-3:] + ")"
    new_input = parts[0][:-3] + first_three_nums + " " + "-".join(parts[1:])
    return new_input

# Prompt: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space
# Input: ['+106 769-858-438']
# Output: +106 (769) 858-438

# Test cases
print(format_phone_number(['+106 769-858-438'])) # Output: +106 (769) 858-438
print(format_phone_number(['+83 973-757-831'])) # Output: +83 (973) 757-831
print(format_phone_number(['+62 647-787-775'])) # Output: +62 (647) 787-775

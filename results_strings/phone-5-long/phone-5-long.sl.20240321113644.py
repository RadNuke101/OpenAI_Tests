def get_first_number(input_str):
    input_str = input_str.replace('+', '').split()[0]
    return int(input_str)

# Prompt: return first three numbers in input
# given input as ['+106 769-858-438'] output is 106
# given input as ['+83 973-757-831'] output is 83
# given input as ['+62 647-787-775'] output is 62

# Test cases
print(get_first_number('+106 769-858-438'))  # Output: 106
print(get_first_number('+83 973-757-831'))   # Output: 83
print(get_first_number('+62 647-787-775'))   # Output: 62

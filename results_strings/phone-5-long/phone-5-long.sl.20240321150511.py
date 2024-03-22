def get_first_number(input_str):
    input_str = input_str.replace('+', '')  # remove '+'
    first_number = input_str.split()[0]  # get the first number
    return first_number

# Prompt: return first three numbers in input
# Given input as ['+106 769-858-438'] output is 106
# Given input as ['+83 973-757-831'] output is 83
# Given input as ['+62 647-787-775'] output is 62

# Test cases
print(get_first_number('+106 769-858-438'))  # Output: 106
print(get_first_number('+83 973-757-831'))  # Output: 83
print(get_first_number('+62 647-787-775'))  # Output: 62

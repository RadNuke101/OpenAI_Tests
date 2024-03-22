# Prompt: return first three numbers in input
# Given input as ['+106 769-858-438'] output is 106
# Given input as ['+83 973-757-831'] output is 83
# Given input as ['+62 647-787-775'] output is 62
# ...

def extract_first_three_numbers(input_str):
    return input_str.split()[0][1:]

# Test cases
print(extract_first_three_numbers('+106 769-858-438'))  # Output: 106
print(extract_first_three_numbers('+83 973-757-831'))   # Output: 83
print(extract_first_three_numbers('+62 647-787-775'))   # Output: 62

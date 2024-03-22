# Prompt: return the three numbers in between "-" in input
# Given input as ['+106 769-858-438'] output is 858
# Given input as ['+83 973-757-831'] output is 757
# Given input as ['+62 647-787-775'] output is 787

def extract_numbers(input_str):
    parts = input_str.split('-')
    return parts[1]

# Test cases
print(extract_numbers('+106 769-858-438'))  # Output: 858
print(extract_numbers('+83 973-757-831'))   # Output: 757
print(extract_numbers('+62 647-787-775'))   # Output: 787

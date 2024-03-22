def get_numbers_between_dash(input_str):
    input_str = input_str.split('-')
    return input_str[1]

# Prompt: return the three numbers in between "-" in input
# Given input as ['+106 769-858-438'], output is 858
# Given input as ['+83 973-757-831'], output is 757
# Given input as ['+62 647-787-775'], output is 787

# Test the function
print(get_numbers_between_dash('+106 769-858-438')) # Output: 858
print(get_numbers_between_dash('+83 973-757-831')) # Output: 757
print(get_numbers_between_dash('+62 647-787-775')) # Output: 787

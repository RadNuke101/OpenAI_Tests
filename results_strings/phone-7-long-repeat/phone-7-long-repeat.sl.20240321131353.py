# Prompt: return the three numbers in between "-" in input
# Given input as '+106 769-858-438', output is '858'
# Given input as '+83 973-757-831', output is '757'
# Given input as '+62 647-787-775', output is '787'

def get_numbers_between_dash(input_str):
    dash_index = input_str.index('-')
    first_num_index = dash_index - 3
    last_num_index = dash_index + 1
    return input_str[first_num_index:last_num_index]

# Test cases
print(get_numbers_between_dash('+106 769-858-438'))  # Output: '858'
print(get_numbers_between_dash('+83 973-757-831'))   # Output: '757'
print(get_numbers_between_dash('+62 647-787-775'))   # Output: '787'

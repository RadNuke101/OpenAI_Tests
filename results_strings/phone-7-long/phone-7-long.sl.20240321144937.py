def get_numbers_in_between(input_str):
    input_str = input_str.split('-')
    return input_str[1]

# Prompt: return the three numbers in between "-" in input
# Input: ['+106 769-858-438']
# Output: 858
print(get_numbers_in_between('+106 769-858-438')) # Output: 858

def get_numbers_between_dash(input_str):
    input_str = input_str.split('-')
    return input_str[1]

# Prompt: return the three numbres in between "-" in input
# Input: '+106 769-858-438'
# Output: '858'
print(get_numbers_between_dash('+106 769-858-438'))  # Expected output: '858'

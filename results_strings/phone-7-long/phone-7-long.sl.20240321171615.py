def find_number_between_dash(input_str):
    input_str = input_str.split('-')
    return input_str[1]

# Prompt: return the three numbers in between "-" in input
# Input: '+106 769-858-438'
# Output: '858'
print(find_number_between_dash('+106 769-858-438'))

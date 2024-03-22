def get_numbers_between_dash(input_str):
    input_list = input_str.split()
    numbers = input_list[1].split('-')
    return numbers[1]

# Prompt: return the three numbers in between "-" in input
# Input: '+106 769-858-438'
# Output: '858'
print(get_numbers_between_dash('+106 769-858-438'))  # Output: '858'

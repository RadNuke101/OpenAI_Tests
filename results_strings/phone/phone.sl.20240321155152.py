# Prompt: return first three numbers in input
# Input: ['938-242-504'], Output: 938
# Input: ['308-916-545'], Output: 308
# Input: ['623-599-749'], Output: 623
# Input: ['981-424-843'], Output: 981
# Input: ['118-980-214'], Output: 118
# Input: ['244-655-094'], Output: 244

def get_first_three_numbers(input_str):
    return input_str.split('-')[0]

# Test the function with an example input
input_example = '938-242-504'
output_example = get_first_three_numbers(input_example)
print(output_example)  # Output: 938

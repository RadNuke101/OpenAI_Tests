# Prompt: return first three numbers in input
# Given input as ['938-242-504'], output is 938
# Given input as ['308-916-545'], output is 308
# Given input as ['623-599-749'], output is 623
# Given input as ['981-424-843'], output is 981
# Given input as ['118-980-214'], output is 118
# Given input as ['244-655-094'], output is 244

def get_first_three_numbers(input_str):
    return input_str.split('-')[0]

# Test cases
print(get_first_three_numbers('938-242-504'))  # Output: 938
print(get_first_three_numbers('308-916-545'))  # Output: 308
print(get_first_three_numbers('623-599-749'))  # Output: 623
print(get_first_three_numbers('981-424-843'))  # Output: 981
print(get_first_three_numbers('118-980-214'))  # Output: 118
print(get_first_three_numbers('244-655-094'))  # Output: 244

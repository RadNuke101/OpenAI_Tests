# Prompt: return first three numbers in input
# Input: '938-242-504'
# Output: 938

def return_first_three_numbers(input_str):
    return input_str.split('-')[0]

# Test cases
print(return_first_three_numbers('938-242-504'))  # Output: 938
print(return_first_three_numbers('308-916-545'))  # Output: 308
print(return_first_three_numbers('623-599-749'))  # Output: 623
print(return_first_three_numbers('981-424-843'))  # Output: 981
print(return_first_three_numbers('118-980-214'))  # Output: 118
print(return_first_three_numbers('244-655-094'))  # Output: 244

def return_first_three_numbers(input_str):
    # Prompt: return first three numbers in input
    # Input: ['938-242-504'] => Output: 938
    # Input: ['308-916-545'] => Output: 308
    # Input: ['623-599-749'] => Output: 623
    input_list = input_str.split('-')
    return input_list[0]

# Test cases
print(return_first_three_numbers('938-242-504'))  # Output: 938
print(return_first_three_numbers('308-916-545'))  # Output: 308
print(return_first_three_numbers('623-599-749'))  # Output: 623

def return_first_three_numbers(input_str):
    input_str = input_str.replace('-', '')  # Remove dashes from input string
    return input_str[:3]  # Return the first three characters of the modified input string

# Prompt: return first three numbers in input
# Given input as ['938-242-504'] output is 938
# Given input as ['308-916-545'] output is 308
# Given input as ['623-599-749'] output is 623
# ...

# Test cases
print(return_first_three_numbers('938-242-504'))  # Output: 938
print(return_first_three_numbers('308-916-545'))  # Output: 308
print(return_first_three_numbers('623-599-749'))  # Output: 623

# Prompt: return the last three numbers
# Input: ['938-242-504'] -> Output: 504
# Input: ['308-916-545'] -> Output: 545
# Input: ['623-599-749'] -> Output: 749

def get_last_three_numbers(input_str):
    return input_str[-3:]

# Test the function with the provided inputs
print(get_last_three_numbers('938-242-504'))  # Output: 504
print(get_last_three_numbers('308-916-545'))  # Output: 545
print(get_last_three_numbers('623-599-749'))  # Output: 749

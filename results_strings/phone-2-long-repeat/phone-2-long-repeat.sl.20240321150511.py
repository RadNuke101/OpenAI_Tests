def get_last_three_numbers(input_str):
    # Prompt: return the last three numbers
    # Input: ['938-242-504'] -> Output: 504
    # Input: ['308-916-545'] -> Output: 545
    # Input: ['623-599-749'] -> Output: 749
    # Add more input-output examples as needed
    
    input_list = input_str.split('-')
    output = input_list[-1]
    
    return output

# Test the function with the provided examples
print(get_last_three_numbers('938-242-504'))  # Output: 504
print(get_last_three_numbers('308-916-545'))  # Output: 545
print(get_last_three_numbers('623-599-749'))  # Output: 749

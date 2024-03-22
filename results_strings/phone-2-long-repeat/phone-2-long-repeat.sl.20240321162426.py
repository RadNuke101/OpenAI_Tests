def get_last_three_numbers(input_str):
    # Prompt: return the last three numbers
    # Input: ['938-242-504'] -> Output: 504
    # Input: ['308-916-545'] -> Output: 545
    # Input: ['623-599-749'] -> Output: 749
    # Add more input-output examples here
    
    # Extract the last three characters from the input string
    output = input_str[-3:]
    
    return output

# Test the function with a sample input
input_str = '938-242-504'
output = get_last_three_numbers(input_str)
print(output)  # Output should be '504'

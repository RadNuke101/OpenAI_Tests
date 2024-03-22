def get_numbers_in_between(input_str):
    # Prompt: return the three numbers in between "-" in input
    # Input: '+106 769-858-438'
    # Output: '858'
    
    # Extract the numbers between the dashes
    numbers = input_str.split('-')[1:-1]
    
    # Join the numbers into a single string
    output = ''.join(numbers)
    
    return output

# Test the function with the provided input
input_str = '+106 769-858-438'
output_str = get_numbers_in_between(input_str)
print(output_str)  # Output: '858'

def get_numbers_between_dash(input_str):
    # Prompt: return the three numbers in between "-" in input
    # Input: '+106 769-858-438'
    # Output: '858'
    
    # Split the input string by "-"
    parts = input_str.split("-")
    
    # Get the second part which contains the numbers between "-"
    numbers_between_dash = parts[1]
    
    return numbers_between_dash

# Test the function
input_str = '+106 769-858-438'
output_str = get_numbers_between_dash(input_str)
print(output_str)  # Output: '858'

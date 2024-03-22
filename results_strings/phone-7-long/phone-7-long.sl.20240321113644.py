def find_number_between_dash(input_str):
    # Prompt: return the three numbers in between "-" in input
    # Input: '+106 769-858-438'
    # Output: '858'
    
    # Extract the numbers between the dashes
    numbers = input_str.split('-')[1:-1]
    
    # Join the numbers into a single string
    output = ''.join(numbers)
    
    return output

# Test cases
print(find_number_between_dash('+106 769-858-438'))  # Output: '858'
print(find_number_between_dash('+83 973-757-831'))    # Output: '757'
print(find_number_between_dash('+62 647-787-775'))    # Output: '787'

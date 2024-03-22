def get_numbers_between_dash(input_str):
    # Prompt: return the three numbers in between "-" in input
    # Given input as ['+106 769-858-438'] output is 858
    # Given input as ['+83 973-757-831'] output is 757
    # Given input as ['+62 647-787-775'] output is 787
    
    # Extract the numbers between the dashes
    numbers = input_str.split('-')[1:-1]
    
    # Return the middle number
    return numbers[1]

# Test cases
print(get_numbers_between_dash('+106 769-858-438'))  # Output: 858
print(get_numbers_between_dash('+83 973-757-831'))    # Output: 757
print(get_numbers_between_dash('+62 647-787-775'))    # Output: 787

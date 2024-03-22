def get_first_number(input_str):
    # Prompt: return first three numbers in input
    # Given input as ['+106 769-858-438'] output is 106
    # Given input as ['+83 973-757-831'] output is 83
    # Given input as ['+62 647-787-775'] output is 62
    first_three_numbers = input_str.split()[0][1:]  # Extract the first three numbers after '+'
    return first_three_numbers

# Test cases
print(get_first_number('+106 769-858-438'))  # Output: 106
print(get_first_number('+83 973-757-831'))  # Output: 83
print(get_first_number('+62 647-787-775'))  # Output: 62

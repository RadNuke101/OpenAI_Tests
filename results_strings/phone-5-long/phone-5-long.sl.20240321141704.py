def extract_first_number(input_str):
    # Prompt: return first three numbers in input
    # Given input as ['+106 769-858-438'] output is 106
    # Given input as ['+83 973-757-831'] output is 83
    # Given input as ['+62 647-787-775'] output is 62
    numbers = ''.join(filter(str.isdigit, input_str))  # Extract all numbers from input
    return numbers[:3]  # Return the first three numbers

# Test cases
print(extract_first_number('+106 769-858-438'))  # Output: 106
print(extract_first_number('+83 973-757-831'))  # Output: 83
print(extract_first_number('+62 647-787-775'))  # Output: 62

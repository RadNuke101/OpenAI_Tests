# Prompt: return last three numbers in input
# Given input as ['+106 769-858-438'] output is 438
# Given input as ['+83 973-757-831'] output is 831
# Given input as ['+62 647-787-775'] output is 775

def last_three_numbers(input_str):
    input_str = input_str.replace(' ', '')  # Remove spaces
    numbers = input_str.split('-')  # Split by hyphen
    return numbers[-1]  # Return the last element

# Test cases
print(last_three_numbers('+106 769-858-438'))  # Output: 438
print(last_three_numbers('+83 973-757-831'))  # Output: 831
print(last_three_numbers('+62 647-787-775'))  # Output: 775

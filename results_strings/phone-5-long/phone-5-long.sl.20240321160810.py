def return_first_three_numbers(input_str):
    # Prompt: return first three numbers in input
    # Given input as ['+106 769-858-438'] output is 106
    input_str = input_str.replace('+', '')  # Remove the '+' sign
    numbers = input_str.split()  # Split the input string by spaces
    return numbers[0]  # Return the first element

# Test cases
print(return_first_three_numbers('+106 769-858-438'))  # Output: 106
print(return_first_three_numbers('+83 973-757-831'))  # Output: 83
print(return_first_three_numbers('+62 647-787-775'))  # Output: 62

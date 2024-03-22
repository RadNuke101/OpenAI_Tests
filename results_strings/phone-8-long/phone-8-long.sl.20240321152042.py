def return_last_three_numbers(input_str):
    input_list = input_str.split()
    output = input_list[-1][-3:]
    return output

# Prompt: return last three numbers in input
# Given input as ['+106 769-858-438'] output is 438
# Given input as ['+83 973-757-831'] output is 831
# Given input as ['+62 647-787-775'] output is 775

# Test the function
print(return_last_three_numbers('+106 769-858-438'))  # Output: 438
print(return_last_three_numbers('+83 973-757-831'))  # Output: 831
print(return_last_three_numbers('+62 647-787-775'))  # Output: 775

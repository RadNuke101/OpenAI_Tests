def return_last_three_numbers(input_str):
    input_list = input_str.split()
    last_three_numbers = input_list[-1][-3:]
    return last_three_numbers

# Prompt: return last three numbers in input
# given input as ['+106 769-858-438'] output is 438
# given input as ['+83 973-757-831'] output is 831
# given input as ['+62 647-787-775'] output is 775

# Test cases
print(return_last_three_numbers('+106 769-858-438'))  # 438
print(return_last_three_numbers('+83 973-757-831'))  # 831
print(return_last_three_numbers('+62 647-787-775'))  # 775

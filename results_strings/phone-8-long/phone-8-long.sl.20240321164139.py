def return_last_three_numbers(input_str):
    input_str = input_str[0]  # extract string from list
    output = input_str[-3:]  # get last three characters
    return output

# Prompt: return last three numbers in input
# Given input as ['+106 769-858-438'] output is 438
# Given input as ['+83 973-757-831'] output is 831
# Given input as ['+62 647-787-775'] output is 775

# Test the function
print(return_last_three_numbers(['+106 769-858-438']))  # 438
print(return_last_three_numbers(['+83 973-757-831']))  # 831
print(return_last_three_numbers(['+62 647-787-775']))  # 775

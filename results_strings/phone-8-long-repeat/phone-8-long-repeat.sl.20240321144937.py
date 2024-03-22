def return_last_three_numbers(input_str):
    # Prompt: return last three numbers in input
    # Given input as ['+106 769-858-438'] output is 438
    input_str = input_str.replace('-', '').replace('+', '').replace(' ', '')
    return input_str[-3:]

# Test cases
print(return_last_three_numbers('+106 769-858-438'))  # Output: 438
print(return_last_three_numbers('+83 973-757-831'))  # Output: 831
print(return_last_three_numbers('+62 647-787-775'))  # Output: 775
print(return_last_three_numbers('+172 027-507-632'))  # Output: 632
print(return_last_three_numbers('+72 001-050-856'))  # Output: 856
print(return_last_three_numbers('+95 310-537-401'))  # Output: 401
print(return_last_three_numbers('+6 775-969-238'))  # Output: 238
print(return_last_three_numbers('+174 594-539-946'))  # Output: 946
print(return_last_three_numbers('+155 927-275-860'))  # Output: 860
print(return_last_three_numbers('+167 405-461-331'))  # Output: 331

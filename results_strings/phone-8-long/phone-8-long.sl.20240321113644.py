def return_last_three_numbers(input_str):
    # Prompt: return last three numbers in input
    # Given input as ['+106 769-858-438'] output is 438
    return input_str[-3:]

# Test cases
print(return_last_three_numbers('+106 769-858-438'))  # Output: 438
print(return_last_three_numbers('+83 973-757-831'))    # Output: 831
print(return_last_three_numbers('+62 647-787-775'))    # Output: 775
print(return_last_three_numbers('+172 027-507-632'))   # Output: 632
print(return_last_three_numbers('+72 001-050-856'))    # Output: 856

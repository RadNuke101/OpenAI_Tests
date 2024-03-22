def return_last_three_numbers(input_str):
    # Prompt: return last three numbers in input
    # Input: ['+106 769-858-438'] -> Output: 438
    # Input: ['+83 973-757-831'] -> Output: 831
    # Input: ['+62 647-787-775'] -> Output: 775
    input_list = input_str.split()
    output_str = input_list[1][-3:]
    return output_str

# Test the function with the provided inputs
print(return_last_three_numbers('+106 769-858-438'))  # Output: 438
print(return_last_three_numbers('+83 973-757-831'))   # Output: 831
print(return_last_three_numbers('+62 647-787-775'))   # Output: 775

def return_last_three_numbers(input_str):
    # Prompt: return last three numbers in input
    # Input: ['+106 769-858-438'], Output: 438
    # Input: ['+83 973-757-831'], Output: 831
    # Input: ['+62 647-787-775'], Output: 775
    input_list = input_str.split('-')
    last_three_numbers = input_list[-1]
    return last_three_numbers

# Test the function with one of the inputs
input_str = '+106 769-858-438'
output = return_last_three_numbers(input_str)
print(output)  # Output should be 438

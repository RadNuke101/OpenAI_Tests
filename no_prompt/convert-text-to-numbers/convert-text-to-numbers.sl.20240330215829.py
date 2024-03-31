# Start time: 2024-03-30 22:11:10.969458

# Content: Given that given input as ['101'] output is 101, given input as ['1002'] output is 1002, given input as ['743'] output is 743, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def convert_to_int(input_str):
    try:
        return int(input_str)
    except ValueError:
        print("Invalid input. Please provide a valid integer string.")

# Test cases
# Input: '101', Output: 101
# Input: '1002', Output: 1002
# Input: '743', Output: 743

# Uncomment the below lines to test the function
# print(convert_to_int('101'))
# print(convert_to_int('1002'))
# print(convert_to_int('743'))

# End time: 2024-03-30 22:11:12.178599
# Elapsed time in seconds: 1.2091105519994017
# Start time: 2024-03-30 23:17:56.562478

# Content: Given that given input as ['101'] output is 101, given input as ['1002'] output is 1002, given input as ['743'] output is 743, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_number(input_str):
    try:
        return int(input_str)
    except ValueError:
        print("Invalid input. Please provide a valid number.")

# Test cases
# print(extract_number('101'))  # Output: 101
# print(extract_number('1002'))  # Output: 1002
# print(extract_number('743'))  # Output: 743

# End time: 2024-03-30 23:17:57.803739
# Elapsed time in seconds: 1.2412279719974322
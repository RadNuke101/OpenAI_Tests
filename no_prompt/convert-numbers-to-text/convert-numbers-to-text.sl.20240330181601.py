# Start time: 2024-03-30 18:19:13.061910

# Content: Given that given input as ['101'] output is 101, given input as ['1002'] output is 1002, given input as ['743'] output is 743, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '101'
# Output: 101

def convert_string_to_int(input_str):
    try:
        output = int(input_str)
        return output
    except ValueError:
        print("Invalid input. Please provide a valid integer string.")
        return None

# Test cases
print(convert_string_to_int('101'))
print(convert_string_to_int('1002'))
print(convert_string_to_int('743'))

# End time: 2024-03-30 18:19:14.272049
# Elapsed time in seconds: 1.210110794000002
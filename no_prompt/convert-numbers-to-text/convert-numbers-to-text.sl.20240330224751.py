# Start time: 2024-03-30 22:51:43.587643

# Content: Given that given input as ['101'] output is 101, given input as ['1002'] output is 1002, given input as ['743'] output is 743, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_number(input_str):
    try:
        num = int(input_str)
        return num
    except ValueError:
        print("Invalid input. Please provide a valid number.")
        return None

# Test cases
# input: '101', output: 101
# input: '1002', output: 1002
# input: '743', output: 743
print(extract_number('101'))
print(extract_number('1002'))
print(extract_number('743'))

# End time: 2024-03-30 22:51:44.758707
# Elapsed time in seconds: 1.1710323789993708
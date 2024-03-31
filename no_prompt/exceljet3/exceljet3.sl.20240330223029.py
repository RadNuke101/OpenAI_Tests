# Start time: 2024-03-30 22:42:56.182920

# Content: Given that given input as ['year= 2016'] output is 2016, given input as ['make= subaru'] output is subaru, given input as ['model= outback wagon'] output is outback wagon, given input as ['fuel economy= 25/33'] output is 25/33, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_value(input_str):
    try:
        key, value = input_str.split('= ')
        return value
    except ValueError:
        return "Invalid input format"

# Test cases
# input_str = 'year= 2016'
# print(extract_value(input_str))  # Output: 2016

# input_str = 'make= subaru'
# print(extract_value(input_str))  # Output: subaru

# input_str = 'model= outback wagon'
# print(extract_value(input_str))  # Output: outback wagon

# input_str = 'fuel economy= 25/33'
# print(extract_value(input_str))  # Output: 25/33

# End time: 2024-03-30 22:43:02.741753
# Elapsed time in seconds: 6.558652752999478
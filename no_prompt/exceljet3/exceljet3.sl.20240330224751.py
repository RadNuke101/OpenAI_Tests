# Start time: 2024-03-30 22:59:21.300347

# Content: Given that given input as ['year= 2016'] output is 2016, given input as ['make= subaru'] output is subaru, given input as ['model= outback wagon'] output is outback wagon, given input as ['fuel economy= 25/33'] output is 25/33, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_value(input_string):
    try:
        key, value = input_string.split('= ')
        return value
    except ValueError:
        return "Invalid input format"

# Test cases
# input_string = 'year= 2016'
# print(extract_value(input_string))  # Output: 2016

# input_string = 'make= subaru'
# print(extract_value(input_string))  # Output: subaru

# input_string = 'model= outback wagon'
# print(extract_value(input_string))  # Output: outback wagon

# input_string = 'fuel economy= 25/33'
# print(extract_value(input_string))  # Output: 25/33

# End time: 2024-03-30 22:59:23.396392
# Elapsed time in seconds: 2.09599755400086
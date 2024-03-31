# Start time: 2024-03-30 23:38:32.564267

# Content: Given that given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def rearrange_names(input_str):
    try:
        names = input_str.split(',')
        rearranged_names = names[1] + ',' + names[0]
        return rearranged_names
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
# input_str = 'chang,amy'
# print(rearrange_names(input_str))  # Output: amy,chang

# input_str = 'smith,bobby'
# print(rearrange_names(input_str))  # Output: bobby,smith

# input_str = 'lennox,aaron'
# print(rearrange_names(input_str))  # Output: aaron,lennox

# End time: 2024-03-30 23:38:34.407511
# Elapsed time in seconds: 1.8436898059990199
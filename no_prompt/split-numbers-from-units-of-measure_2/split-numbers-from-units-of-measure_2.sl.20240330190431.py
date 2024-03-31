# Start time: 2024-03-30 19:11:22.682198

# Content: Given that given input as ['80v', '3'] output is v, given input as ['10hrs', '3'] output is hrs, given input as ['7h', '2'] output is h, given input as ['500m', '4'] output is m, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_unit(input_str):
    try:
        unit = input_str.split(' ')[1]
        return unit
    except IndexError:
        return "Invalid input format"

# Test cases
'''
print(extract_unit('80v'))  # Output: v
print(extract_unit('10hrs'))  # Output: hrs
print(extract_unit('7h'))  # Output: h
print(extract_unit('500m'))  # Output: m
'''

# End time: 2024-03-30 19:11:24.017404
# Elapsed time in seconds: 1.3351694289999614
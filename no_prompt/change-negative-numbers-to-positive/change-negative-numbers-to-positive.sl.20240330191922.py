# Start time: 2024-03-30 19:25:10.820386

# Content: Given that given input as ['-%134'] output is %134, given input as ['500'] output is 500, given input as ['5.125'] output is 5.125, given input as ['-%43.00'] output is %43.00, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def clean_input(input_str):
    try:
        if input_str.startswith('-'):
            input_str = input_str[1:]
        if input_str.startswith('%'):
            input_str = input_str[1:]
        return float(input_str)
    except ValueError:
        return input_str

# Test cases
"""
print(clean_input('-%134'))  # Output: 134.0
print(clean_input('500'))    # Output: 500.0
print(clean_input('5.125'))  # Output: 5.125
print(clean_input('-%43.00'))  # Output: 43.0
"""

# End time: 2024-03-30 19:25:12.035906
# Elapsed time in seconds: 1.215481791000002
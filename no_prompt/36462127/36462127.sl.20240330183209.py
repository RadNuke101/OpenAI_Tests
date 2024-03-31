# Start time: 2024-03-30 18:36:12.322733

# Content: Given that given input as ['ABCDE/FGHI/JKL/MNOPQR'] output is MNOPQR, given input as ['A/ABCDE/FGHI/JKL'] output is JKL, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_last_segment(input_str):
    try:
        segments = input_str.split('/')
        last_segment = segments[-1]
        return last_segment
    except (AttributeError, IndexError):
        return "Invalid input format"

# Test cases
# print(get_last_segment('ABCDE/FGHI/JKL/MNOPQR'))  # Output should be MNOPQR
# print(get_last_segment('A/ABCDE/FGHI/JKL'))  # Output should be JKL

# End time: 2024-03-30 18:36:13.689173
# Elapsed time in seconds: 1.3664008699999783
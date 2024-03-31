# Start time: 2024-03-30 19:54:45.457007

# Content: Given that given input as ['ABCDE/FGHI/JKL/MNOPQR'] output is MNOPQR, given input as ['A/ABCDE/FGHI/JKL'] output is JKL, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_last_segment(input_str):
    try:
        segments = input_str.split('/')
        last_segment = segments[-1]
        return last_segment
    except (AttributeError, IndexError):
        return "Invalid input format"

# Test cases
# input_str = 'ABCDE/FGHI/JKL/MNOPQR'
# print(extract_last_segment(input_str))  # Output should be MNOPQR

# input_str = 'A/ABCDE/FGHI/JKL'
# print(extract_last_segment(input_str))  # Output should be JKL

# End time: 2024-03-30 19:54:49.299875
# Elapsed time in seconds: 3.8428128430005017
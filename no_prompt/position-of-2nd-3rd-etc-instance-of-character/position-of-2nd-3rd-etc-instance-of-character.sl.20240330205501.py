# Start time: 2024-03-30 21:07:36.115517

# Content: Given that given input as ['100x15x50', 'x', '2'] output is 7, given input as ['cat-in-the-hat', '-', '3'] output is 11, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '100x15x50', 'x', '2' output: 7
# input: 'cat-in-the-hat', '-', '3' output: 11

def calculate_length(input_str, delimiter, index):
    try:
        parts = input_str.split(delimiter)
        target_str = parts[int(index)]
        return len(target_str)
    except (ValueError, IndexError):
        return "Invalid input"

# Test cases
print(calculate_length('100x15x50', 'x', '2'))  # Output should be 7
print(calculate_length('cat-in-the-hat', '-', '3'))  # Output should be 11

# End time: 2024-03-30 21:07:37.884023
# Elapsed time in seconds: 1.768481764000171
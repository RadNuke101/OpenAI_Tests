# Start time: 2024-03-30 23:01:00.241877

# Content: Given that given input as ['100x15x50', 'x', '2'] output is 7, given input as ['cat-in-the-hat', '-', '3'] output is 11, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '100x15x50', 'x', '2'
# Output: 7

# Input: 'cat-in-the-hat', '-', '3'
# Output: 11

def calculate_length(input_str, delimiter, index):
    try:
        parts = input_str.split(delimiter)
        selected_part = parts[index]
        return len(selected_part)
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
print(calculate_length('100x15x50', 'x', 2))  # Output: 7
print(calculate_length('cat-in-the-hat', '-', 3))  # Output: 11

# End time: 2024-03-30 23:01:02.250561
# Elapsed time in seconds: 2.00862962499923
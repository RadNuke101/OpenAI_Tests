# Start time: 2024-03-30 20:14:20.514489

# Content: Given that given input as ['The'] output is 3, given input as ['The quick fox'] output is 13, given input as ['The quick  fox'] output is 14, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def calculate_length(input_str):
    try:
        words = input_str.split()
        total_length = sum(len(word) for word in words)
        return total_length
    except AttributeError:
        return "Invalid input: Please provide a string input"

# Test cases
# print(calculate_length('The'))  # Output: 3
# print(calculate_length('The quick fox'))  # Output: 13
# print(calculate_length('The quick  fox'))  # Output: 14

# End time: 2024-03-30 20:14:23.197768
# Elapsed time in seconds: 2.6832496709994302
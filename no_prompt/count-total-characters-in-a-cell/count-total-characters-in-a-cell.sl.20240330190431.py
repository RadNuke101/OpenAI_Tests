# Start time: 2024-03-30 19:11:40.006485

# Content: Given that given input as ['The'] output is 3, given input as ['The quick fox'] output is 13, given input as ['The quick  fox'] output is 14, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'The' Output: 3
# Input: 'The quick fox' Output: 13
# Input: 'The quick  fox' Output: 14

def calculate_length(input_str):
    try:
        return len(input_str)
    except Exception as e:
        print("Error:", e)

# Test cases
print(calculate_length('The'))  # Output: 3
print(calculate_length('The quick fox'))  # Output: 13
print(calculate_length('The quick  fox'))  # Output: 14

# End time: 2024-03-30 19:11:42.331506
# Elapsed time in seconds: 2.3249507470000026
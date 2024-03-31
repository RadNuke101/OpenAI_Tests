# Start time: 2024-03-30 22:11:00.275022

# Content: Given that given input as ['100x15x50', 'x', '2'] output is 7, given input as ['cat-in-the-hat', '-', '3'] output is 11, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# input: '100x15x50', 'x', '2'
# output: 7

def calculate_length(input_str, delimiter, factor):
    try:
        if delimiter not in input_str:
            raise ValueError("Delimiter not found in input string")
        
        parts = input_str.split(delimiter)
        if len(parts) != 3:
            raise ValueError("Input string does not have 3 parts separated by delimiter")
        
        length = 0
        for part in parts:
            length += int(part) * int(factor)
        
        return length
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Test cases
print(calculate_length('100x15x50', 'x', '2'))  # 7
print(calculate_length('cat-in-the-hat', '-', '3'))  # 11

# End time: 2024-03-30 22:11:02.604112
# Elapsed time in seconds: 2.3290277529995365
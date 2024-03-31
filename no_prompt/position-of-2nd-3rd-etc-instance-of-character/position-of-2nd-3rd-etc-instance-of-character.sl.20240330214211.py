# Start time: 2024-03-30 21:55:15.060727

# Content: Given that given input as ['100x15x50', 'x', '2'] output is 7, given input as ['cat-in-the-hat', '-', '3'] output is 11, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def calculate_length(input_str):
    try:
        parts = input_str.split(',')
        if len(parts) != 3:
            raise ValueError("Input must contain exactly 3 elements separated by commas")
        
        string = parts[0]
        char = parts[1]
        num = int(parts[2])

        if char not in string:
            raise ValueError("Character not found in the string")

        count = string.count(char)
        result = count * num

        return result

    except ValueError as ve:
        return str(ve)

# Test cases
"""
Input: '100x15x50,x,2'
Output: 7
"""
print(calculate_length('100x15x50,x,2'))

"""
Input: 'cat-in-the-hat,-,3'
Output: 11
"""
print(calculate_length('cat-in-the-hat,-,3'))

# End time: 2024-03-30 21:55:17.709550
# Elapsed time in seconds: 2.6487450759996136
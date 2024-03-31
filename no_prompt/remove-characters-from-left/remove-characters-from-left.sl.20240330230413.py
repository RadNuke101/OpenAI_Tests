# Start time: 2024-03-30 23:13:51.832222

# Content: Given that given input as ['1234', '1'] output is 234, given input as ['**512A', '2'] output is 512A, given input as ['343DMX', '3'] output is DMX, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_substring(input_str, num):
    try:
        index = int(num)
        if index < 0 or index >= len(input_str):
            return "Invalid index"
        return input_str[index:]
    except ValueError:
        return "Invalid input"

# Test cases
"""
Input: '1234', '1'
Output: 234

Input: '**512A', '2'
Output: 512A

Input: '343DMX', '3'
Output: DMX
"""

# End time: 2024-03-30 23:13:55.788398
# Elapsed time in seconds: 3.956068398998468
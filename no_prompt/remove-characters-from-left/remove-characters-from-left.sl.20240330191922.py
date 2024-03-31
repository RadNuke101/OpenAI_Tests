# Start time: 2024-03-30 19:27:13.233942

# Content: Given that given input as ['1234', '1'] output is 234, given input as ['**512A', '2'] output is 512A, given input as ['343DMX', '3'] output is DMX, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_string(input_str, num):
    try:
        index = int(num)
        output_str = input_str[index:]
        return output_str
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
# Input: '1234', '1'  Output: '234'
# Input: '**512A', '2'  Output: '512A'
# Input: '343DMX', '3'  Output: 'DMX'

# End time: 2024-03-30 19:27:14.896453
# Elapsed time in seconds: 1.6624543879997873
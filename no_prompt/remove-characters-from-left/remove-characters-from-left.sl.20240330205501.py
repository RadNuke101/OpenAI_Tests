# Start time: 2024-03-30 21:02:44.400172

# Content: Given that given input as ['1234', '1'] output is 234, given input as ['**512A', '2'] output is 512A, given input as ['343DMX', '3'] output is DMX, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_string(input_str, num):
    try:
        index = input_str.index(num)
        output_str = input_str[index+1:]
        return output_str
    except ValueError:
        return "Number not found in input string"

# Test cases
# input: '1234', '1' => output: '234'
# input: '**512A', '2' => output: '512A'
# input: '343DMX', '3' => output: 'DMX'

# End time: 2024-03-30 21:02:45.960268
# Elapsed time in seconds: 1.5600526470007026
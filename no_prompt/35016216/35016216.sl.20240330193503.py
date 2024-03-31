# Start time: 2024-03-30 19:42:06.714483

# Content: Given that given input as ['C0abc', 'def'] output is C0abc, given input as ['aabc', 'def'] output is def, given input as ['C0dd', 'qwe'] output is C0dd, given input as ['dd', 'qwe'] output is qwe, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'C0abc', 'def'
# Output: C0abc

# Input: 'aabc', 'def'
# Output: def

# Input: 'C0dd', 'qwe'
# Output: C0dd

# Input: 'dd', 'qwe'
# Output: qwe

def match_input_output(input_str1, input_str2):
    try:
        if input_str1[0].isupper():
            return input_str1
        else:
            return input_str2
    except IndexError:
        return "Invalid input"

# Test cases
print(match_input_output('C0abc', 'def'))
print(match_input_output('aabc', 'def'))
print(match_input_output('C0dd', 'qwe'))
print(match_input_output('dd', 'qwe'))

# End time: 2024-03-30 19:42:09.137389
# Elapsed time in seconds: 2.4228842200000145
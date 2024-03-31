# Start time: 2024-03-30 22:39:20.296923

# Content: Given that given input as ['C0abc', 'def'] output is C0abc, given input as ['aabc', 'def'] output is def, given input as ['C0dd', 'qwe'] output is C0dd, given input as ['dd', 'qwe'] output is qwe, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'C0abc', 'def'
# Output: C0abc

def match_input_output(input_str):
    try:
        input_list = input_str.split(', ')
        if input_list[0][0].isupper():
            print(input_list[0])
        else:
            print(input_list[1])
    except Exception as e:
        print("Error: Invalid input")

# Test cases
match_input_output('C0abc, def')
match_input_output('aabc, def')
match_input_output('C0dd, qwe')
match_input_output('dd, qwe')

# End time: 2024-03-30 22:39:23.274595
# Elapsed time in seconds: 2.9775904409998475
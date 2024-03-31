# Start time: 2024-03-30 22:55:50.145312

# Content: Given that given input as ['C0abc', 'def'] output is C0abc, given input as ['aabc', 'def'] output is def, given input as ['C0dd', 'qwe'] output is C0dd, given input as ['dd', 'qwe'] output is qwe, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_input_output(input_str):
    try:
        input_list = input_str.split(', ')
        if 'C0' in input_list[0]:
            print(input_list[0])
        else:
            print(input_list[1])
    except (IndexError, AttributeError):
        print("Invalid input format")

# Test cases
match_input_output('C0abc, def')  # Output: C0abc
match_input_output('aabc, def')   # Output: def
match_input_output('C0dd, qwe')  # Output: C0dd
match_input_output('dd, qwe')    # Output: qwe

# End time: 2024-03-30 22:55:52.013435
# Elapsed time in seconds: 1.868085014000826
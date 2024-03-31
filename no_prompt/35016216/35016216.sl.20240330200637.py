# Start time: 2024-03-30 20:14:30.356140

# Content: Given that given input as ['C0abc', 'def'] output is C0abc, given input as ['aabc', 'def'] output is def, given input as ['C0dd', 'qwe'] output is C0dd, given input as ['dd', 'qwe'] output is qwe, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_string(input_str):
    try:
        input_list = input_str.split(',')
        first_str = input_list[0].strip()
        second_str = input_list[1].strip()

        if first_str[0].isupper() and first_str[1:].isalnum():
            print(first_str)
        elif second_str[0].isupper() and second_str[1:].isalnum():
            print(second_str)
        else:
            print("Invalid input")

    except IndexError:
        print("Invalid input")

# Test cases
# match_string('C0abc, def')  # Output: C0abc
# match_string('aabc, def')    # Output: def
# match_string('C0dd, qwe')    # Output: C0dd
# match_string('dd, qwe')      # Output: qwe

# End time: 2024-03-30 20:14:34.790139
# Elapsed time in seconds: 4.43395930800034
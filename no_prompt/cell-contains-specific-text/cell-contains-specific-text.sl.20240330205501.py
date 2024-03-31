# Start time: 2024-03-30 20:59:04.201349

# Content: Given that given input as ['An apple a day keeps the doctor away', 'apple'] output is true, given input as ['An apple a day keeps the doctor away', 'orange'] output is false, given input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_substring(input_str, sub_str):
    try:
        if sub_str in input_str:
            return True
        else:
            return False
    except TypeError:
        print("Input must be strings")

# Test cases
# print(check_substring('An apple a day keeps the doctor away', 'apple'))  # True
# print(check_substring('An apple a day keeps the doctor away', 'orange'))  # False
# print(check_substring('Better the devil you know', 'you know'))  # True

# End time: 2024-03-30 20:59:05.575256
# Elapsed time in seconds: 1.373870999999781
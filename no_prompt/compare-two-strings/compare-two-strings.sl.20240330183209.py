# Start time: 2024-03-30 18:33:48.204681

# Content: Given that given input as ['apple', 'apple'] output is true, given input as ['orange', 'Orange'] output is false, given input as ['peach', 'peach'] output is true, given input as ['cherry', 'cherrY'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def compare_strings(str1, str2):
    try:
        if str1.lower() == str2.lower():
            return True
        else:
            return False
    except AttributeError:
        print("Input must be strings")

# Test cases
# print(compare_strings('apple', 'apple'))  # Output: True
# print(compare_strings('orange', 'Orange'))  # Output: False
# print(compare_strings('peach', 'peach'))  # Output: True
# print(compare_strings('cherry', 'cherrY'))  # Output: False

# End time: 2024-03-30 18:33:49.840101
# Elapsed time in seconds: 1.6353739550000057
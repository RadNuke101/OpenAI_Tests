# Start time: 2024-03-30 22:28:28.224909

# Content: Given that given input as ['one'] output is 1, given input as ['one/ntwo'] output is 2, given input as ['one/ntwo/nthree'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def count_levels(input_str):
    try:
        levels = input_str.count('/') + 1
        return levels
    except:
        return "Invalid input"

# Test cases
"""
print(count_levels('one'))  # Output: 1
print(count_levels('one/ntwo'))  # Output: 2
print(count_levels('one/ntwo/nthree'))  # Output: 3
"""

# End time: 2024-03-30 22:28:30.979425
# Elapsed time in seconds: 2.75443558599909
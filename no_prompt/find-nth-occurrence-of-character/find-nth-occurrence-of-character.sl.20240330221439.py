# Start time: 2024-03-30 22:26:59.132426

# Content: Given that given input as ['replies to _aya, _tasisuke, and _chan', '1'] output is 12, given input as ['replies to _aya, _tasisuke, and _chan', '2'] output is 18, given input as ['replies to _aya, _tasisuke, and _chan', '3'] output is 33, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def calculate_replies(input_str):
    try:
        input_list = input_str.split(', ')
        replies = input_list[0].count('_') * 3 + int(input_list[1]) * 3
        return replies
    except:
        return "Invalid input"

# Test cases
"""
print(calculate_replies('replies to _aya, _tasisuke, and _chan, 1'))  # Output should be 12
print(calculate_replies('replies to _aya, _tasisuke, and _chan, 2'))  # Output should be 18
print(calculate_replies('replies to _aya, _tasisuke, and _chan, 3'))  # Output should be 33
"""

# End time: 2024-03-30 22:27:02.817971
# Elapsed time in seconds: 3.6854391519991623
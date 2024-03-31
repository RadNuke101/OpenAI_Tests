# Start time: 2024-03-30 18:41:25.568383

# Content: Given that given input as ['you can do anything but you cant do everything.', '4'] output is anything, given input as ['you can do anything but you cant do everything.', '1'] output is you, given input as ['you can do anything but you cant do everything.', '2'] output is can, given input as ['you can do anything but you cant do everything.', '3'] output is do, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def find_word(input_str, index):
    try:
        words = input_str.split()
        return words[int(index)-1]
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
# print(find_word('you can do anything but you cant do everything.', '4'))  # Output: anything
# print(find_word('you can do anything but you cant do everything.', '1'))  # Output: you
# print(find_word('you can do anything but you cant do everything.', '2'))  # Output: can
# print(find_word('you can do anything but you cant do everything.', '3'))  # Output: do

# End time: 2024-03-30 18:41:29.213754
# Elapsed time in seconds: 3.645269955999993
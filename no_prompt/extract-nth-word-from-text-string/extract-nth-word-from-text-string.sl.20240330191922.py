# Start time: 2024-03-30 19:27:38.793473

# Content: Given that given input as ['you can do anything but you cant do everything.', '4'] output is anything, given input as ['you can do anything but you cant do everything.', '1'] output is you, given input as ['you can do anything but you cant do everything.', '2'] output is can, given input as ['you can do anything but you cant do everything.', '3'] output is do, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_word(input_str):
    try:
        input_list = input_str.split(', ')
        sentence = input_list[0][1:-1]
        index = int(input_list[1][1])
        
        words = sentence.split()
        
        if index <= len(words):
            return words[index-1]
        else:
            return "Index out of range"
    except (IndexError, ValueError):
        return "Invalid input format"

# Test cases
"""
print(get_word('you can do anything but you cant do everything., 4'))  # Output: anything
print(get_word('you can do anything but you cant do everything., 1'))  # Output: you
print(get_word('you can do anything but you cant do everything., 2'))  # Output: can
print(get_word('you can do anything but you cant do everything., 3'))  # Output: do
"""

# End time: 2024-03-30 19:27:40.477161
# Elapsed time in seconds: 1.6836348350002481
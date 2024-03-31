# Start time: 2024-03-30 22:50:05.860542

# Content: Given that given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'chang,amy'
# Output: 'amy,chang'

# Input: 'smith,bobby'
# Output: 'bobby,smith'

# Input: 'lennox,aaron'
# Output: 'aaron,lennox'

def reverse_name(name):
    try:
        first_name, last_name = name.split(',')
        return f'{last_name},{first_name}'
    except (ValueError, AttributeError):
        return "Invalid input format"

# Test cases
print(reverse_name('chang,amy'))
print(reverse_name('smith,bobby'))
print(reverse_name('lennox,aaron'))

# End time: 2024-03-30 22:50:07.006410
# Elapsed time in seconds: 1.145838451999225
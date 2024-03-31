# Start time: 2024-03-30 19:52:30.120576

# Content: Given that given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'chang,amy'
# Output: 'amy,chang'

# Input: 'smith,bobby'
# Output: 'bobby,smith'

# Input: 'lennox,aaron'
# Output: 'aaron,lennox'

def reverse_names(input_str):
    try:
        names = input_str.split(',')
        reversed_names = ','.join(reversed(names))
        return reversed_names
    except Exception as e:
        return str(e)

# Test cases
print(reverse_names('chang,amy'))  # Output: 'amy,chang'
print(reverse_names('smith,bobby'))  # Output: 'bobby,smith'
print(reverse_names('lennox,aaron'))  # Output: 'aaron,lennox'

# End time: 2024-03-30 19:52:32.902394
# Elapsed time in seconds: 2.781772162999914
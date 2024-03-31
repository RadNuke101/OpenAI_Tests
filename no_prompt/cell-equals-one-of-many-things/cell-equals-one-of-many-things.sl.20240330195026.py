# Start time: 2024-03-30 19:55:27.319929

# Content: Given that given input as ['yellow'] output is true, given input as ['gray'] output is false, given input as ['black'] output is false, given input as ['blue'] output is true, given input as ['pink'] output is true, given input as ['orange'] output is true, given input as ['turkey'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_color(color):
    try:
        if color == 'yellow':
            return True
        elif color == 'blue' or color == 'pink' or color == 'orange':
            return True
        else:
            return False
    except:
        return False

# Test cases
print(check_color('yellow'))  # Output: True
print(check_color('gray'))    # Output: False
print(check_color('black'))   # Output: False
print(check_color('blue'))    # Output: True
print(check_color('pink'))    # Output: True
print(check_color('orange'))  # Output: True
print(check_color('turkey'))  # Output: False

# End time: 2024-03-30 19:55:29.308772
# Elapsed time in seconds: 1.9888120570003593
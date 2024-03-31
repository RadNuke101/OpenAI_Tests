# Start time: 2024-03-30 22:18:56.473283

# Content: Given that given input as ['yellow'] output is true, given input as ['gray'] output is false, given input as ['black'] output is false, given input as ['blue'] output is true, given input as ['pink'] output is true, given input as ['orange'] output is true, given input as ['turkey'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'yellow' , Output: True
# Input: 'gray' , Output: False
# Input: 'black' , Output: False
# Input: 'blue' , Output: True
# Input: 'pink' , Output: True
# Input: 'orange' , Output: True
# Input: 'turkey' , Output: False

def check_color(color):
    try:
        if color == 'yellow' or color == 'blue' or color == 'pink' or color == 'orange':
            return True
        else:
            return False
    except:
        return False

# Test cases
print(check_color('yellow'))  # True
print(check_color('gray'))    # False
print(check_color('black'))   # False
print(check_color('blue'))    # True
print(check_color('pink'))    # True
print(check_color('orange'))  # True
print(check_color('turkey'))  # False

# End time: 2024-03-30 22:18:59.006182
# Elapsed time in seconds: 2.5328280640005687
# Start time: 2024-03-30 21:31:23.688400

# Content: Given that given input as ['yellow'] output is true, given input as ['gray'] output is false, given input as ['black'] output is false, given input as ['blue'] output is true, given input as ['pink'] output is true, given input as ['orange'] output is true, given input as ['turkey'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_color(color):
    try:
        color = color.lower()
        if color == 'yellow':
            return True
        elif color == 'blue' or color == 'pink' or color == 'orange':
            return True
        else:
            return False
    except AttributeError:
        print("Input is not a string")
    except:
        print("An error occurred")

# Test cases
# Input: 'yellow', Output: True
# Input: 'gray', Output: False
# Input: 'black', Output: False
# Input: 'blue', Output: True
# Input: 'pink', Output: True
# Input: 'orange', Output: True
# Input: 'turkey', Output: False

# End time: 2024-03-30 21:31:26.862760
# Elapsed time in seconds: 3.174270012001216
# Start time: 2024-03-30 20:11:01.139652

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
        print("Invalid input. Please enter a valid color string.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# Input: 'yellow', Output: True
# Input: 'gray', Output: False
# Input: 'black', Output: False
# Input: 'blue', Output: True
# Input: 'pink', Output: True
# Input: 'orange', Output: True
# Input: 'turkey', Output: False

# Uncomment the below lines to test the function
# print(check_color('yellow'))
# print(check_color('gray'))
# print(check_color('black'))
# print(check_color('blue'))
# print(check_color('pink'))
# print(check_color('orange'))
# print(check_color('turkey'))

# End time: 2024-03-30 20:11:03.462480
# Elapsed time in seconds: 2.3228009240001484
# Start time: 2024-04-10 18:01:23.653817

'''
Prompt:
Given that input as ['yellow'] output is true, input as ['gray'] output is false, input as ['black'] output is false, input as ['blue'] output is true, input as ['pink'] output is true, input as ['orange'] output is true, input as ['turkey'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        color = input_str.lower()
        if color == 'yellow' or color == 'blue' or color == 'pink' or color == 'orange':
            return True
        else:
            return False
    except:
        return False

# Test cases
print(generated_function('yellow'))
print(generated_function('gray'))
print(generated_function('black'))
print(generated_function('blue'))
print(generated_function('pink'))
print(generated_function('orange'))
print(generated_function('turkey'))
print(generated_function("yellow"))  ## Output: true
print(generated_function("gray"))  ## Output: false
print(generated_function("black"))  ## Output: false
print(generated_function("blue"))  ## Output: true
print(generated_function("pink"))  ## Output: true
print(generated_function("orange"))  ## Output: true
print(generated_function("turkey"))  ## Output: false

# End time: 2024-04-10 18:01:25.239240
# Elapsed time in seconds: 1.5854318149999926
# Start time: 2024-04-10 17:58:59.334388

'''
Prompt:
Given that input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        words = input_list[0].split()
        colors = input_list[1:]
        
        for color in colors:
            if color not in words:
                return False
        
        return True
    except:
        return False

# Test cases
print(generated_function('red ball, green sweater, red, green, pink'))
print(generated_function('pink ball, green sweater, red, green, pink'))
print(generated_function('blue sea, pink ribbon, red, blue, pink'))
print(generated_function('black sea, white ribbon, red, blue, pink'))
print(generated_function('red green blue, red, blue, pink'))
print(generated_function("red ball, green sweater", "red", "green", "pink"))  ## Output: true
print(generated_function("pink ball, green sweater", "red", "green", "pink"))  ## Output: false
print(generated_function("blue sea, pink ribbon", "red", "blue", "pink"))  ## Output: false
print(generated_function("black sea, white ribbon", "red", "blue", "pink"))  ## Output: false
print(generated_function("red green blue", "red", "blue", "pink"))  ## Output: true

# End time: 2024-04-10 17:59:01.888242
# Elapsed time in seconds: 2.5537868810001783


# APPEND TEST SCRIPTS...
print(generated_function("red ball, green sweater", "red", "green", "pink"))  ## Output: true
print(generated_function("pink ball, green sweater", "red", "green", "pink"))  ## Output: false
print(generated_function("blue sea, pink ribbon", "red", "blue", "pink"))  ## Output: false
print(generated_function("black sea, white ribbon", "red", "blue", "pink"))  ## Output: false
print(generated_function("red green blue", "red", "blue", "pink"))  ## Output: true


print(generated_function("yellow ball, green sweater", "red", "green", "yellow"))  ### Output: [
print(generated_function("blue sea, yellow ribbon", "red", "blue", "yellow"))  ### Output: f
print(generated_function("red green blue", "red", "blue", "yellow"))  ### Output: a
print(generated_function("black sea, white ribbon", "red", "blue", "yellow"))  ### Output: l
print(generated_function("red ball, green sweater", "red", "green", "yellow"))  ### Output: s

# TEST SCRIPTS APPENDED!


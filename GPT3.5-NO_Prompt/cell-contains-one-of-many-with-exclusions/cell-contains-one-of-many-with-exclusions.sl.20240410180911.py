# Start time: 2024-04-10 18:19:06.996907

'''
Prompt:
Given that input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        words = input_list[0].split()
        if input_list[1] in words and input_list[2] in words and input_list[3] in words:
            return True
        else:
            return False
    except:
        return False

# Test cases
print(generated_function('yellow dog on green grass, yellow, green, cat'))
print(generated_function('warm gray sweater, yellow, green, cat'))
print(generated_function('blue neon signs, blue, green, neon'))
print(generated_function('hot pink socks, blue, pink, neon'))
print(generated_function('deep black eyes, yellow, green, neon'))
print(generated_function("yellow dog on green grass", "yellow", "green", "cat"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "cat"))  ## Output: false
print(generated_function("blue neon signs", "blue", "green", "neon"))  ## Output: false
print(generated_function("hot pink socks", "blue", "pink", "neon"))  ## Output: true
print(generated_function("deep black eyes", "yellow", "green", "neon"))  ## Output: false

# End time: 2024-04-10 18:19:09.070633
# Elapsed time in seconds: 2.0736753619999035
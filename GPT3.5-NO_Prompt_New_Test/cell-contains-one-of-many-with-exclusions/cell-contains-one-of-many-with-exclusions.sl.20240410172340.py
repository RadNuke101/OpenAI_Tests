# Start time: 2024-04-10 17:31:58.074060

'''
Prompt:
Given that input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        if input_list[1] in input_list[0] and input_list[2] in input_list[0] and input_list[3] in input_list[0]:
            return 'true'
        else:
            return 'false'
    except:
        return 'false'

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

# End time: 2024-04-10 17:32:00.158920
# Elapsed time in seconds: 2.084841707999999


# APPEND TEST SCRIPTS...
print(generated_function("yellow dog on green grass", "yellow", "green", "cat"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "cat"))  ## Output: false
print(generated_function("blue neon signs", "blue", "green", "neon"))  ## Output: false
print(generated_function("hot pink socks", "blue", "pink", "neon"))  ## Output: true
print(generated_function("deep black eyes", "yellow", "green", "neon"))  ## Output: false


print(generated_function("deep black eyes", "red", "green", "neon"))  ### Output: [
print(generated_function("red dog on green grass", "red", "green", "cat"))  ### Output: f
print(generated_function("warm white sweater", "red", "green", "cat"))  ### Output: a
print(generated_function("blue neon signs", "blue", "green", "neon"))  ### Output: l
print(generated_function("hot pink socks", "blue", "pink", "neon"))  ### Output: s

# TEST SCRIPTS APPENDED!


# Start time: 2024-04-10 18:05:06.419274

'''
Prompt:
Given that input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str, word1, word2, word3):
    try:
        words = input_str.split()
        if word1 in words and word2 in words and word3 in words:
            return True
        else:
            return False
    except AttributeError:
        return False

# Test cases
print(generated_function('yellow dog on green grass', 'yellow', 'green', 'dog'))
print(generated_function('warm gray sweater', 'yellow', 'green', 'dog'))
print(generated_function('A yellow sun in a green field', 'yellow', 'green', 'dog'))
print(generated_function('yellow neon sign with a green background', 'yellow', 'green', 'dog'))
print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "dog"))  ## Output: false
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))  ## Output: true
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))  ## Output: true

# End time: 2024-04-10 18:05:08.675234
# Elapsed time in seconds: 2.2559217200000603


# APPEND TEST SCRIPTS...
print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "dog"))  ## Output: false
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))  ## Output: true
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))  ## Output: true


print(generated_function("blue dog on yellow grass", "yellow", "green", "dog"))  ### Output: [
print(generated_function("Neon sign with a green background", "yellow", "green", "dog"))  ### Output: t
print(generated_function("N/A", "yellow", "green", "dog"))  ### Output: r
print(generated_function("Cold white sweater", "yellow", "green", "dog"))  ### Output: u
print(generated_function("A yellow sun in a field", "yellow", "green", "dog"))  ### Output: e

# TEST SCRIPTS APPENDED!


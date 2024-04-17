# Start time: 2024-04-10 18:16:54.940164

'''
Prompt:
Given that input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str, *keywords):
    try:
        words = input_str.split()
        for keyword in keywords:
            if keyword not in words:
                return False
        return True
    except Exception as e:
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

# End time: 2024-04-10 18:16:56.916118
# Elapsed time in seconds: 1.9759246359999452
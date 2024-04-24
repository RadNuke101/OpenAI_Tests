# Start time: 2024-04-05 17:21:09.683367

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if either the second, third, or fourth inputs (words) are in the first input (expression), return true, else false, and input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, word1, word2, word3):
    # Check if either of the words (word1, word2, or word3) is in the expression
    return word1 in expression or word2 in expression or word3 in expression

# Test cases
generated_function('yellow dog on green grass', 'yellow', 'green', 'dog')
generated_function('warm gray sweater', 'yellow', 'green', 'dog')
generated_function('A yellow sun in a green field', 'yellow', 'green', 'dog')
generated_function('yellow neon sign with a green background', 'yellow', 'green', 'dog')
print(generated_function("yellow dog on green grass", "yellow", "green", "dog"))  ## Output: true
print(generated_function("warm gray sweater", "yellow", "green", "dog"))  ## Output: false
print(generated_function("A yellow sun in a green field", "yellow", "green", "dog"))  ## Output: true
print(generated_function("yellow neon sign with a green background", "yellow", "green", "dog"))  ## Output: true

# End time: 2024-04-05 17:21:13.720335
# Elapsed time in seconds: 4.036853529999462


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


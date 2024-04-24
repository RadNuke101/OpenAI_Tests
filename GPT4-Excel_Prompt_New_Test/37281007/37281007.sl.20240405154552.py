# Start time: 2024-04-05 16:17:34.671126

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if entered letter or phrase (second column) is in the expression (first column), return true, else false, and input as ['ABC', 'D'] output is false, input as ['ABC', 'BC'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, search_term):
    # Check if the search_term is in the expression
    return search_term in expression

# Test cases based on the prompt
print(generated_function('ABC', 'D'))  # Expected output: False
print(generated_function('ABC', 'BC'))  # Expected output: True
print(generated_function("ABC", "D"))  ## Output: false
print(generated_function("ABC", "BC"))  ## Output: true

# End time: 2024-04-05 16:17:36.816118
# Elapsed time in seconds: 2.1449369760000536


# APPEND TEST SCRIPTS...
print(generated_function("ABC", "D"))  ## Output: false
print(generated_function("ABC", "BC"))  ## Output: true


print(generated_function("ABCD", "D"))  ### Output: [
print(generated_function("AB", "BC"))  ### Output: t

# TEST SCRIPTS APPENDED!


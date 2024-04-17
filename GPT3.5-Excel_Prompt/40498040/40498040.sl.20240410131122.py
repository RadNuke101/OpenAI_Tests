# Start time: 2024-04-10 13:21:58.154390

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the word "overhead" in expression, return false, else true, and input as ['some project,other project'] output is true, input as ['some project'] output is true, input as ['overhead'] output is false, input as ['some project, overhead'] output is false, input as ['some project, other, boo'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    for arg in args:
        if 'overhead' in arg:
            return False
    return True

# Test cases
print(generated_function('some project,other project'))
print(generated_function('some project'))
print(generated_function('overhead'))
print(generated_function('some project, overhead'))
print(generated_function('some project, other, boo'))
print(generated_function("some project,other project"))  ## Output: true
print(generated_function("some project"))  ## Output: true
print(generated_function("overhead"))  ## Output: false
print(generated_function("some project, overhead"))  ## Output: false
print(generated_function("some project, other, boo"))  ## Output: true

# End time: 2024-04-10 13:21:59.984623
# Elapsed time in seconds: 1.8302302989998225
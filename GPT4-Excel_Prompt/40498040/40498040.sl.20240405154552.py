# Start time: 2024-04-05 16:12:58.729074

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the word "overhead" in expression, return false, else true, and input as ['some project,other project'] output is true, input as ['some project'] output is true, input as ['overhead'] output is false, input as ['some project, overhead'] output is false, input as ['some project, other, boo'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    # Iterate through each argument provided
    for arg in args:
        # Check if the word "overhead" is in the argument
        if "overhead" in arg:
            return False
    return True

# Test cases
generated_function('some project', 'other project')
generated_function('some project')
generated_function('overhead')
generated_function('some project', 'overhead')
generated_function('some project', 'other', 'boo')
print(generated_function("some project,other project"))  ## Output: true
print(generated_function("some project"))  ## Output: true
print(generated_function("overhead"))  ## Output: false
print(generated_function("some project, overhead"))  ## Output: false
print(generated_function("some project, other, boo"))  ## Output: true

# End time: 2024-04-05 16:13:01.728306
# Elapsed time in seconds: 2.9991483610001524
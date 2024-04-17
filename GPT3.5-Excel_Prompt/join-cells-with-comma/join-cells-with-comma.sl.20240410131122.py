# Start time: 2024-04-10 13:11:22.383439

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input , and input as ['figs', '', 'apples'] output is figs, apples, input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function
def generated_function(*args):
    result = ""
    for arg in args:
        if arg:
            result += arg + ", "
    return result.rstrip(", ")

# Test cases
print(generated_function('figs', '', 'apples'))
print(generated_function('mangos', 'kiwis', 'grapes'))
print(generated_function("figs", "", "apples"))  ## Output: figs, apples
print(generated_function("mangos", "kiwis", "grapes"))  ## Output: mangos, kiwis, grapes

# End time: 2024-04-10 13:11:24.430087
# Elapsed time in seconds: 2.046620827999959
# Start time: 2024-04-16 14:21:57.589305

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input , and input as ['figs', '', 'apples'] output is figs, apples, input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the function
def generated_function(*args):
    result = ''
    for arg in args:
        if arg != '':
            result += arg + ', '
    return result[:-2]

# Test cases
print(generated_function('figs', '', 'apples'))  # Output: figs, apples
print(generated_function('mangos', 'kiwis', 'grapes'))  # Output: mangos, kiwis, grapes



print(generated_function("figs", "", "bananas"))  ### Output: "figs", "", "bananas"
print(generated_function("alpha", "", "epsilon"))  ### Output: "alpha", "", "epsilon"
print(generated_function("figs", "", "trees"))  ### Output: "figs", "", "trees"
print(generated_function("alpha", "beta", "gamma"))  ### Output: "alpha", "beta", "gamma"
print(generated_function("mango", "kiwi", "grape"))  ### Output: "mango", "kiwi", "grape"
print(generated_function("beta", "gamma", "epsilon"))  ### Output: "beta", "gamma", "epsilon"


print(generated_function("figs", "", "apples"))  ## Output: figs, apples
print(generated_function("mangos", "kiwis", "grapes"))  ## Output: mangos, kiwis, grapes



# End time: 2024-04-16 14:21:59.417185
# Elapsed time in seconds: 1.8278339260000003
# Start time: 2024-04-05 16:22:52.970460

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first three numbers in input, and input as ['938-242-504'] output is 938, input as ['308-916-545'] output is 308, input as ['623-599-749'] output is 623, input as ['981-424-843'] output is 981, input as ['118-980-214'] output is 118, input as ['244-655-094'] output is 244, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Extract and return the first three numbers from the input string
    return input_string.split('-')[0]

# Test cases
generated_function('938-242-504')
generated_function('308-916-545')
generated_function('623-599-749')
generated_function('981-424-843')
generated_function('118-980-214')
generated_function('244-655-094')
print(generated_function("938-242-504"))  ## Output: 938
print(generated_function("308-916-545"))  ## Output: 308
print(generated_function("623-599-749"))  ## Output: 623
print(generated_function("981-424-843"))  ## Output: 981
print(generated_function("118-980-214"))  ## Output: 118
print(generated_function("244-655-094"))  ## Output: 244

# End time: 2024-04-05 16:22:55.644946
# Elapsed time in seconds: 2.676394771000105
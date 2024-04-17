# Start time: 2024-04-10 17:36:16.984264

'''
Prompt:
Given that input as ['938-242-504'] output is 504, input as ['308-916-545'] output is 545, input as ['623-599-749'] output is 749, input as ['981-424-843'] output is 843, input as ['118-980-214'] output is 214, input as ['244-655-094'] output is 094, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_string):
    try:
        output = input_string.split('-')[-1]
        return output
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('938-242-504'))  # Output: 504
print(generated_function('308-916-545'))  # Output: 545
print(generated_function('623-599-749'))  # Output: 749
print(generated_function('981-424-843'))  # Output: 843
print(generated_function('118-980-214'))  # Output: 214
print(generated_function('244-655-094'))  # Output: 094
print(generated_function("938-242-504"))  ## Output: 504
print(generated_function("308-916-545"))  ## Output: 545
print(generated_function("623-599-749"))  ## Output: 749
print(generated_function("981-424-843"))  ## Output: 843
print(generated_function("118-980-214"))  ## Output: 214
print(generated_function("244-655-094"))  ## Output: 094

# End time: 2024-04-10 17:36:18.888730
# Elapsed time in seconds: 1.9044430289999354
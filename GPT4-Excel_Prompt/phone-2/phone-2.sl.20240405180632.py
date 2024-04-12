# Start time: 2024-04-05 18:12:27.524428

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the last three numbers, and input as ['938-242-504'] output is 504, input as ['308-916-545'] output is 545, input as ['623-599-749'] output is 749, input as ['981-424-843'] output is 843, input as ['118-980-214'] output is 214, input as ['244-655-094'] output is 094, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    # Extract and return the last three numbers from the input string
    return phone_number.split('-')[-1]

# Test cases
result1 = generated_function('938-242-504')
result2 = generated_function('308-916-545')
result3 = generated_function('623-599-749')
result4 = generated_function('981-424-843')
result5 = generated_function('118-980-214')
result6 = generated_function('244-655-094')

# The results can be printed or used as needed
print(generated_function("938-242-504"))  ## Output: 504
print(generated_function("308-916-545"))  ## Output: 545
print(generated_function("623-599-749"))  ## Output: 749
print(generated_function("981-424-843"))  ## Output: 843
print(generated_function("118-980-214"))  ## Output: 214
print(generated_function("244-655-094"))  ## Output: 094

# End time: 2024-04-05 18:12:30.418139
# Elapsed time in seconds: 2.893621520999659
# Start time: 2024-04-10 13:27:20.510100

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return first three numbers in input, and input as ['938-242-504'] output is 938, input as ['308-916-545'] output is 308, input as ['623-599-749'] output is 623, input as ['981-424-843'] output is 981, input as ['118-980-214'] output is 118, input as ['244-655-094'] output is 244, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Split the input string by '-' and return the first element
    return input_str.split('-')[0]
print(generated_function("938-242-504"))  ## Output: 938
print(generated_function("308-916-545"))  ## Output: 308
print(generated_function("623-599-749"))  ## Output: 623
print(generated_function("981-424-843"))  ## Output: 981
print(generated_function("118-980-214"))  ## Output: 118
print(generated_function("244-655-094"))  ## Output: 244

# End time: 2024-04-10 13:27:21.646868
# Elapsed time in seconds: 1.1367441180000242


# APPEND TEST SCRIPTS...
print(generated_function("938-242-504"))  ## Output: 938
print(generated_function("308-916-545"))  ## Output: 308
print(generated_function("623-599-749"))  ## Output: 623
print(generated_function("981-424-843"))  ## Output: 981
print(generated_function("118-980-214"))  ## Output: 118
print(generated_function("244-655-094"))  ## Output: 244


print(generated_function("345-980-214"))  ### Output: 345
print(generated_function("678-655-094"))  ### Output: 678
print(generated_function("123-242-504"))  ### Output: 123
print(generated_function("456-916-545"))  ### Output: 456
print(generated_function("234-424-843"))  ### Output: 234
print(generated_function("789-599-749"))  ### Output: 789

# TEST SCRIPTS APPENDED!


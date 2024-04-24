# Start time: 2024-04-10 17:47:53.080450

'''
Prompt:
Given that input as ['938-242-504'] output is 938, input as ['308-916-545'] output is 308, input as ['623-599-749'] output is 623, input as ['981-424-843'] output is 981, input as ['118-980-214'] output is 118, input as ['244-655-094'] output is 244, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(phone_number):
    try:
        return int(phone_number.split('-')[0])
    except (IndexError, ValueError):
        return None

# Test cases
print(generated_function('938-242-504'))  # Output: 938
print(generated_function('308-916-545'))  # Output: 308
print(generated_function('623-599-749'))  # Output: 623
print(generated_function('981-424-843'))  # Output: 981
print(generated_function('118-980-214'))  # Output: 118
print(generated_function('244-655-094'))  # Output: 244
print(generated_function("938-242-504"))  ## Output: 938
print(generated_function("308-916-545"))  ## Output: 308
print(generated_function("623-599-749"))  ## Output: 623
print(generated_function("981-424-843"))  ## Output: 981
print(generated_function("118-980-214"))  ## Output: 118
print(generated_function("244-655-094"))  ## Output: 244

# End time: 2024-04-10 17:47:55.987144
# Elapsed time in seconds: 2.9065966730001946


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


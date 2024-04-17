# Start time: 2024-04-10 18:05:30.272674

'''
Prompt:
Given that input as ['938-242-504'] output is 242, input as ['308-916-545'] output is 916, input as ['623-599-749'] output is 599, input as ['981-424-843'] output is 424, input as ['118-980-214'] output is 980, input as ['244-655-094'] output is 655, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        number = input_str.split('-')[1]
        return int(number)
    except (IndexError, ValueError):
        return None

# Test cases
assert generated_function('938-242-504') == 242
assert generated_function('308-916-545') == 916
assert generated_function('623-599-749') == 599
assert generated_function('981-424-843') == 424
assert generated_function('118-980-214') == 980
assert generated_function('244-655-094') == 655
print(generated_function("938-242-504"))  ## Output: 242
print(generated_function("308-916-545"))  ## Output: 916
print(generated_function("623-599-749"))  ## Output: 599
print(generated_function("981-424-843"))  ## Output: 424
print(generated_function("118-980-214"))  ## Output: 980
print(generated_function("244-655-094"))  ## Output: 655

# End time: 2024-04-10 18:05:32.124551
# Elapsed time in seconds: 1.8518426969999382
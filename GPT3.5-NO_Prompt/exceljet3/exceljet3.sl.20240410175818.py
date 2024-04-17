# Start time: 2024-04-10 18:05:43.462613

'''
Prompt:
Given that input as ['year= 2016'] output is 2016, input as ['make= subaru'] output is subaru, input as ['model= outback wagon'] output is outback wagon, input as ['fuel economy= 25/33'] output is 25/33, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        key, value = input_str.split('= ')
        return value
    except ValueError:
        return "Invalid input format"

# Test cases
print(generated_function('year= 2016'))  # Output: 2016
print(generated_function('make= subaru'))  # Output: subaru
print(generated_function('model= outback wagon'))  # Output: outback wagon
print(generated_function('fuel economy= 25/33'))  # Output: 25/33
print(generated_function("year= 2016"))  ## Output: 2016
print(generated_function("make= subaru"))  ## Output: subaru
print(generated_function("model= outback wagon"))  ## Output: outback wagon
print(generated_function("fuel economy= 25/33"))  ## Output: 25/33

# End time: 2024-04-10 18:05:44.921314
# Elapsed time in seconds: 1.4586736870001005
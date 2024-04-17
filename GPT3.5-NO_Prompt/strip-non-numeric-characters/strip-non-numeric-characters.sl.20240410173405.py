# Start time: 2024-04-10 17:45:11.687231

'''
Prompt:
Given that input as ['100 apples'] output is 100, input as ['the price is %500 dollars'] output is 500, input as ['serial number %003399'] output is 003399, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        output = input_str.split('%')[-1].split()[0].lstrip('0')
        return output
    except:
        return "Invalid input"

# Test cases
print(generated_function('100 apples'))  # Output: 100
print(generated_function('the price is %500 dollars'))  # Output: 500
print(generated_function('serial number %003399'))  # Output: 003399
print(generated_function("100 apples"))  ## Output: 100
print(generated_function("the price is %500 dollars"))  ## Output: 500
print(generated_function("serial number %003399"))  ## Output: 003399

# End time: 2024-04-10 17:45:13.389958
# Elapsed time in seconds: 1.7027079269998922
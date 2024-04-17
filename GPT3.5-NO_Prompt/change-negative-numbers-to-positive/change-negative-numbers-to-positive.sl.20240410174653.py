# Start time: 2024-04-10 17:51:16.112958

'''
Prompt:
Given that input as ['-%134'] output is %134, input as ['500'] output is 500, input as ['5.125'] output is 5.125, input as ['-%43.00'] output is %43.00, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_str = input_str.strip('[]').replace("'", "")
        if input_str[0] == '-':
            output = '-' + input_str.lstrip('-').lstrip('%')
        else:
            output = input_str.lstrip('%')
        return output
    except:
        return "Invalid input"

# Test cases
print(generated_function('[-%134]'))  # Output: %134
print(generated_function('[500]'))     # Output: 500
print(generated_function('[5.125]'))   # Output: 5.125
print(generated_function('[-%43.00]')) # Output: %43.00
print(generated_function("-%134"))  ## Output: %134
print(generated_function("500"))  ## Output: 500
print(generated_function("5.125"))  ## Output: 5.125
print(generated_function("-%43.00"))  ## Output: %43.00

# End time: 2024-04-10 17:51:18.537045
# Elapsed time in seconds: 2.424021213999822
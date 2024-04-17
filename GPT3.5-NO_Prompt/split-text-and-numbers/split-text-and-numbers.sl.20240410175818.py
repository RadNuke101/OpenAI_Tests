# Start time: 2024-04-10 18:02:18.057393

'''
Prompt:
Given that input as ['apples30', '7'] output is apples, input as ['peaches24', '8'] output is peaches, input as ['peaches0', '8'] output is peaches, input as ['pears', '6'] output is pears, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        fruit = input_list[0].strip('0123456789')
        return fruit
    except:
        return "Invalid input"

# Test cases
print(generated_function('apples30,7'))
print(generated_function('peaches24,8'))
print(generated_function('peaches0,8'))
print(generated_function('pears,6'))
print(generated_function("apples30", "7"))  ## Output: apples
print(generated_function("peaches24", "8"))  ## Output: peaches
print(generated_function("peaches0", "8"))  ## Output: peaches
print(generated_function("pears", "6"))  ## Output: pears

# End time: 2024-04-10 18:02:19.539957
# Elapsed time in seconds: 1.482541355000194
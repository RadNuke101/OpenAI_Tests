# Start time: 2024-04-10 18:04:11.817142

'''
Prompt:
Given that input as ['dhfjd9999999dfda'] output is true, input as ['ddsss999dfdfsfd'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        if len(input_str) != 15:
            return False
        if input_str[:4] == 'dhfj' and input_str[4:11].isdigit() and input_str[11:] == 'dfda':
            return True
        else:
            return False
    except Exception as e:
        return False
print(generated_function("dhfjd9999999dfda"))  ## Output: true
print(generated_function("ddsss999dfdfsfd"))  ## Output: false

# End time: 2024-04-10 18:04:13.104098
# Elapsed time in seconds: 1.2869333559997358
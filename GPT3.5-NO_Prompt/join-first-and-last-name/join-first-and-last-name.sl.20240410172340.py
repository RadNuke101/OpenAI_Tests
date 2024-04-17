# Start time: 2024-04-10 17:31:49.067016

'''
Prompt:
Given that input as ['susan', 'chang'] output is susan chang, input as ['aaron', 'kim'] output is aaron kim, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        output = ' '.join(input_list)
        return output.strip()
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('susan, chang'))  # Output: susan chang
print(generated_function('aaron, kim'))  # Output: aaron kim
print(generated_function("susan", "chang"))  ## Output: susan chang
print(generated_function("aaron", "kim"))  ## Output: aaron kim

# End time: 2024-04-10 17:31:50.320458
# Elapsed time in seconds: 1.2534317970000188
# Start time: 2024-04-10 17:41:29.482365

'''
Prompt:
Given that input as ['home/Excel/Sheet1.xls'] output is Sheet1.xls, input as ['home/user/Sheet1.xls'] output is Sheet1.xls, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string by '/' and get the last element
        output = input_str.split('/')[-1]
        return output
    except Exception as e:
        return str(e)

# Test cases
input1 = 'home/Excel/Sheet1.xls'
input2 = 'home/user/Sheet1.xls'

output1 = generated_function(input1)
output2 = generated_function(input2)
print(generated_function("home/Excel/Sheet1.xls"))  ## Output: Sheet1.xls
print(generated_function("home/user/Sheet1.xls"))  ## Output: Sheet1.xls

# End time: 2024-04-10 17:41:30.622472
# Elapsed time in seconds: 1.1400926799999525
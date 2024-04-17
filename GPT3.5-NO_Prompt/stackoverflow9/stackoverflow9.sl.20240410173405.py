# Start time: 2024-04-10 17:44:12.184864

'''
Prompt:
Given that input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string by space
        words = input_str.split()
        
        # Get the last word in the list
        output = words[-1]
        
        return output
    except Exception as e:
        return str(e)

# Test cases
assert generated_function('Sarah Jane Jones') == 'Jones'
assert generated_function('Bob Jane Smithfield') == 'Smithfield'
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-10 17:44:14.076976
# Elapsed time in seconds: 1.8920882800000527
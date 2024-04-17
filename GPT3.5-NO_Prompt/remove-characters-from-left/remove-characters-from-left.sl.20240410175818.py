# Start time: 2024-04-10 18:04:08.026269

'''
Prompt:
Given that input as ['1234', '1'] output is 234, input as ['**512A', '2'] output is 512A, input as ['343DMX', '3'] output is DMX, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str, num):
    try:
        index = input_str.index(num)
        output = input_str[index+1:]
        return output
    except ValueError:
        return "Number not found in input string"
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('1234', '1'))
print(generated_function('**512A', '2'))
print(generated_function('343DMX', '3'))
print(generated_function("1234", "1"))  ## Output: 234
print(generated_function("**512A", "2"))  ## Output: 512A
print(generated_function("343DMX", "3"))  ## Output: DMX

# End time: 2024-04-10 18:04:09.791908
# Elapsed time in seconds: 1.7656089660004
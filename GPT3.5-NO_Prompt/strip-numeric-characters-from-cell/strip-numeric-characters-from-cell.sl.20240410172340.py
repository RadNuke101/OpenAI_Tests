# Start time: 2024-04-10 17:29:33.805767

'''
Prompt:
Given that input as ['34653 jim mcdonald'] output is  jim mcdonald, input as ['price is 500'] output is  price is , input as ['100 apples'] output is  apples, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        words = input_str.split()
        if words[0].isdigit():
            return ' '.join(words[1:])
        else:
            return ' '.join(words[:-1])
    except:
        return ""

# Test cases
print(generated_function('34653 jim mcdonald'))
print(generated_function('price is 500'))
print(generated_function('100 apples'))
print(generated_function("34653 jim mcdonald"))  ## Output:  jim mcdonald
print(generated_function("price is 500"))  ## Output:  price is 
print(generated_function("100 apples"))  ## Output:  apples

# End time: 2024-04-10 17:29:35.498510
# Elapsed time in seconds: 1.6927041210000198
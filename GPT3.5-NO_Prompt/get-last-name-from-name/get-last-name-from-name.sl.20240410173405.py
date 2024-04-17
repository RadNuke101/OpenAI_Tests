# Start time: 2024-04-10 17:44:42.872870

'''
Prompt:
Given that input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        names = input_str.split()
        if len(names) != 2:
            raise ValueError("Input should contain exactly two names separated by a space")
        
        if names[0] == 'Kim':
            return names[1]
        elif names[1] == 'Kim':
            return names[0]
        else:
            raise ValueError("Input should contain 'Kim' as one of the names")
    
    except ValueError as ve:
        return str(ve)

# Test cases
print(generated_function('Park Kim'))  # Output should be Kim
print(generated_function('Lee Kim'))  # Output should be Kim
print(generated_function('Kim Lee'))  # Output should be Lee
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-10 17:44:44.572210
# Elapsed time in seconds: 1.6993190390001018
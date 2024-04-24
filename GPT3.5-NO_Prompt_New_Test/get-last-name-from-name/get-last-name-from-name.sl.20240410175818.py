# Start time: 2024-04-10 18:07:14.615573

'''
Prompt:
Given that input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string into two parts
        first_name, last_name = input_str.split()

        # Return the last name
        return last_name
    except ValueError:
        return "Invalid input format"

# Test cases
print(generated_function('Park Kim'))
print(generated_function('Lee Kim'))
print(generated_function('Kim Lee'))
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-10 18:07:15.855419
# Elapsed time in seconds: 1.2398237969996444


# APPEND TEST SCRIPTS...
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee


print(generated_function("Benjamin Hayes"))  ### Output: Hayes
print(generated_function("Emma Reynolds"))  ### Output: Reynolds
print(generated_function("Grace Harrison"))  ### Output: Harrison
print(generated_function("Caleb Mitchell"))  ### Output: Mitchell
print(generated_function("Olivia Parker"))  ### Output: Parker
print(generated_function("Jackson Turner"))  ### Output: Turner

# TEST SCRIPTS APPENDED!


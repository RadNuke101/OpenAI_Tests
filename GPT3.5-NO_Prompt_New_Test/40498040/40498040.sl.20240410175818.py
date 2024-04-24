# Start time: 2024-04-10 18:06:08.570248

'''
Prompt:
Given that input as ['some project,other project'] output is true, input as ['some project'] output is true, input as ['overhead'] output is false, input as ['some project, overhead'] output is false, input as ['some project, other, boo'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        projects = input_str.split(',')
        for project in projects:
            if 'overhead' in project:
                return False
        return True
    except Exception as e:
        return False

# Test cases
print(generated_function('some project,other project'))
print(generated_function('some project'))
print(generated_function('overhead'))
print(generated_function('some project, overhead'))
print(generated_function('some project, other, boo'))
print(generated_function("some project,other project"))  ## Output: true
print(generated_function("some project"))  ## Output: true
print(generated_function("overhead"))  ## Output: false
print(generated_function("some project, overhead"))  ## Output: false
print(generated_function("some project, other, boo"))  ## Output: true

# End time: 2024-04-10 18:06:10.420142
# Elapsed time in seconds: 1.849860135000199


# APPEND TEST SCRIPTS...
print(generated_function("some project,other project"))  ## Output: true
print(generated_function("some project"))  ## Output: true
print(generated_function("overhead"))  ## Output: false
print(generated_function("some project, overhead"))  ## Output: false
print(generated_function("some project, other, boo"))  ## Output: true


print(generated_function("some project, other, overhead"))  ### Output: [
print(generated_function("some project, other"))  ### Output: f
print(generated_function("some project, other,"))  ### Output: a

# TEST SCRIPTS APPENDED!


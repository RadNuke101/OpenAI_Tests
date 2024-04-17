# Start time: 2024-04-10 17:32:53.586001

'''
Prompt:
Given that input as ['susan ann chang'] output is ann, input as ['ayako tanaka'] output is , input as ['bobby t. smith'] output is t., input as ['anthory r. tom brown'] output is r. tom, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        name_parts = input_str.split()
        for part in name_parts:
            if len(part) == 1 and part.isalpha():
                return part + "."
            elif len(part) > 1 and part.isalpha():
                return part
    except Exception as e:
        return ""

# Test cases
print(generated_function('susan ann chang'))  # Output: ann
print(generated_function('ayako tanaka'))  # Output: 
print(generated_function('bobby t. smith'))  # Output: t.
print(generated_function('anthory r. tom brown'))  # Output: r. tom
print(generated_function("susan ann chang"))  ## Output: ann
print(generated_function("ayako tanaka"))  ## Output: 
print(generated_function("bobby t. smith"))  ## Output: t.
print(generated_function("anthory r. tom brown"))  ## Output: r. tom

# End time: 2024-04-10 17:32:55.658904
# Elapsed time in seconds: 2.0728787430000466
# Start time: 2024-04-10 18:02:33.466189

'''
Prompt:
Given that input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(name):
    try:
        first_name, last_name = name.split()
        return f"{first_name[0]} {last_name}"
    except ValueError:
        return "Invalid input format"

# Test cases
print(generated_function('John Doe'))
print(generated_function('Mayur Naik'))
print(generated_function('Nimit Singh'))
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 18:02:34.655221
# Elapsed time in seconds: 1.1890107389999685


# APPEND TEST SCRIPTS...
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh


print(generated_function("John Singh"))  ### Output: J Singh
print(generated_function("Mayur Doe"))  ### Output: M Doe
print(generated_function("Nimit Naik"))  ### Output: N Naik

# TEST SCRIPTS APPENDED!


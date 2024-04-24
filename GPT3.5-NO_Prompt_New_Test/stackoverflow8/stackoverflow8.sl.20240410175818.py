# Start time: 2024-04-10 18:04:13.155198

'''
Prompt:
Given that input as ['home/Excel/Sheet1.xls'] output is Sheet1.xls, input as ['home/user/Sheet1.xls'] output is Sheet1.xls, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Split the input string by '/'
        parts = input_str.split('/')
        # Return the last part of the split string
        return parts[-1]
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('home/Excel/Sheet1.xls'))  # Output: Sheet1.xls
print(generated_function('home/user/Sheet1.xls'))   # Output: Sheet1.xls
print(generated_function("home/Excel/Sheet1.xls"))  ## Output: Sheet1.xls
print(generated_function("home/user/Sheet1.xls"))  ## Output: Sheet1.xls

# End time: 2024-04-10 18:04:14.911494
# Elapsed time in seconds: 1.7562635539998155


# APPEND TEST SCRIPTS...
print(generated_function("home/Excel/Sheet1.xls"))  ## Output: Sheet1.xls
print(generated_function("home/user/Sheet1.xls"))  ## Output: Sheet1.xls


print(generated_function("home/i/Sheet1.xls"))  ### Output: Sheet1.xls
print(generated_function("home/alotwordsherealotwordshere/Sheet1.xls"))  ### Output: Sheet1.xls
print(generated_function("home/bbob/Sheet1.xls"))  ### Output: Sheet1.xls
print(generated_function("home/achang/Sheet1.xls"))  ### Output: Sheet1.xls

# TEST SCRIPTS APPENDED!


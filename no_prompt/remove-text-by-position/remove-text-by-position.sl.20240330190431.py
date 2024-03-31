# Start time: 2024-03-30 19:11:47.437567

# Content: Given that given input as ['c=/users/dave/shotcut.xls'] output is shotcut.xls, given input as ['c=/users/dave/formulas.xls'] output is formulas.xls, given input as ['c=/users/dave/pivot table.xls'] output is pivot table.xls, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'c=/users/dave/shotcut.xls'
# Output: shotcut.xls

def extract_filename(input_str):
    try:
        # Split the input string by '/'
        parts = input_str.split('/')
        
        # Get the last part of the split string
        filename = parts[-1]
        
        return filename
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
input_str1 = 'c=/users/dave/shotcut.xls'
input_str2 = 'c=/users/dave/formulas.xls'
input_str3 = 'c=/users/dave/pivot table.xls'

print(extract_filename(input_str1))
print(extract_filename(input_str2))
print(extract_filename(input_str3))

# End time: 2024-03-30 19:11:49.558603
# Elapsed time in seconds: 2.120985668999765
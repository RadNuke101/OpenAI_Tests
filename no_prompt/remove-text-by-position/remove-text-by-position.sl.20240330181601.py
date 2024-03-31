# Start time: 2024-03-30 18:22:27.077510

# Content: Given that given input as ['c=/users/dave/shotcut.xls'] output is shotcut.xls, given input as ['c=/users/dave/formulas.xls'] output is formulas.xls, given input as ['c=/users/dave/pivot table.xls'] output is pivot table.xls, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_filename(input_str):
    try:
        # Input: 'c=/users/dave/shotcut.xls'
        # Output: 'shotcut.xls'
        
        # Input: 'c=/users/dave/formulas.xls'
        # Output: 'formulas.xls'
        
        # Input: 'c=/users/dave/pivot table.xls'
        # Output: 'pivot table.xls'
        
        if input_str.startswith('c='):
            file_path = input_str[2:]
            file_name = file_path.split('/')[-1]
            return file_name
        else:
            raise ValueError("Invalid input format. Input should start with 'c='.")
    except Exception as e:
        return str(e)

# Test cases
print(extract_filename('c=/users/dave/shotcut.xls'))
print(extract_filename('c=/users/dave/formulas.xls'))
print(extract_filename('c=/users/dave/pivot table.xls'))

# End time: 2024-03-30 18:22:30.839338
# Elapsed time in seconds: 3.761740111999984
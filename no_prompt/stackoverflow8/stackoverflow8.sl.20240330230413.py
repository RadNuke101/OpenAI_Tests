# Start time: 2024-03-30 23:14:00.718568

# Content: Given that given input as ['home/Excel/Sheet1.xls'] output is Sheet1.xls, given input as ['home/user/Sheet1.xls'] output is Sheet1.xls, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'home/Excel/Sheet1.xls'
# Output: Sheet1.xls

# Input: 'home/user/Sheet1.xls'
# Output: Sheet1.xls

def extract_filename(path):
    try:
        # Split the path by '/'
        parts = path.split('/')
        # Get the last part of the path
        filename = parts[-1]
        return filename
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_filename('home/Excel/Sheet1.xls'))
print(extract_filename('home/user/Sheet1.xls'))

# End time: 2024-03-30 23:14:02.417222
# Elapsed time in seconds: 1.6986047749996942
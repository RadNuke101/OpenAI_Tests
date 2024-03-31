# Start time: 2024-03-30 19:43:39.009239

# Content: Given that given input as ['home/Excel/Sheet1.xls'] output is Sheet1.xls, given input as ['home/user/Sheet1.xls'] output is Sheet1.xls, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_filename(path):
    try:
        filename = path.split('/')[-1]
        return filename
    except (AttributeError, TypeError):
        return "Invalid input"

# Test cases
'''
print(extract_filename('home/Excel/Sheet1.xls'))  # Output: Sheet1.xls
print(extract_filename('home/user/Sheet1.xls'))  # Output: Sheet1.xls
print(extract_filename(123))  # Output: Invalid input
print(extract_filename(['home/user/Sheet1.xls']))  # Output: Invalid input
'''

# End time: 2024-03-30 19:43:42.558095
# Elapsed time in seconds: 3.548817617000168
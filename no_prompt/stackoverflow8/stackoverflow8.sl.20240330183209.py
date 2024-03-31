# Start time: 2024-03-30 18:40:53.999040

# Content: Given that given input as ['home/Excel/Sheet1.xls'] output is Sheet1.xls, given input as ['home/user/Sheet1.xls'] output is Sheet1.xls, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'home/Excel/Sheet1.xls'
# Output: Sheet1.xls

# Input: 'home/user/Sheet1.xls'
# Output: Sheet1.xls

def get_filename(input_str):
    try:
        # Split the input string by '/'
        parts = input_str.split('/')
        # Get the last part of the split string
        filename = parts[-1]
        return filename
    except Exception as e:
        print("Error: ", e)

# Test cases
input1 = 'home/Excel/Sheet1.xls'
input2 = 'home/user/Sheet1.xls'

output1 = get_filename(input1)
output2 = get_filename(input2)

# End time: 2024-03-30 18:40:55.656432
# Elapsed time in seconds: 1.6573446339999691
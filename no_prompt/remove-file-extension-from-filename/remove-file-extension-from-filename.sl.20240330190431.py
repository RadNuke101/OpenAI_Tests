# Start time: 2024-03-30 19:18:42.115430

# Content: Given that given input as ['happy.jpg'] output is happy, given input as ['pivot table.xls'] output is pivot table, given input as ['sales data.csv'] output is sales data, given input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_filename(input_str):
    try:
        # Input: 'happy.jpg'
        # Output: happy
        filename = input_str.split('.')[0]
        return filename
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_filename('happy.jpg'))  # Output: happy
print(extract_filename('pivot table.xls'))  # Output: pivot table
print(extract_filename('sales data.csv'))  # Output: sales data
print(extract_filename('invoice3001.xls.pdf'))  # Output: invoice3001

# End time: 2024-03-30 19:18:43.269846
# Elapsed time in seconds: 1.1543779599996924
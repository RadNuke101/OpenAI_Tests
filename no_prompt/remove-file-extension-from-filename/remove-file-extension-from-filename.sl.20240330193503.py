# Start time: 2024-03-30 19:49:18.894693

# Content: Given that given input as ['happy.jpg'] output is happy, given input as ['pivot table.xls'] output is pivot table, given input as ['sales data.csv'] output is sales data, given input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_file_name(input_str):
    try:
        # Extracting file name from input string
        file_name = input_str.split('.')[0]
        if file_name == '':
            raise ValueError("Invalid input format")
        return file_name
    except Exception as e:
        return str(e)

# Test cases
print(extract_file_name('happy.jpg'))  # Output: happy
print(extract_file_name('pivot table.xls'))  # Output: pivot table
print(extract_file_name('sales data.csv'))  # Output: sales data
print(extract_file_name('invoice3001.xls.pdf'))  # Output: invoice3001

# End time: 2024-03-30 19:49:21.596044
# Elapsed time in seconds: 2.7013199980001446
# Start time: 2024-03-30 19:03:26.595357

# Content: Given that given input as ['happy.jpg'] output is happy, given input as ['pivot table.xls'] output is pivot table, given input as ['sales data.csv'] output is sales data, given input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_name(file_name):
    try:
        # Input: 'happy.jpg'
        # Output: happy
        name = file_name.split('.')[0]
        return name
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_name('happy.jpg'))  # happy
print(extract_name('pivot table.xls'))  # pivot table
print(extract_name('sales data.csv'))  # sales data
print(extract_name('invoice3001.xls.pdf'))  # invoice3001

# End time: 2024-03-30 19:03:28.366683
# Elapsed time in seconds: 1.771275156999991
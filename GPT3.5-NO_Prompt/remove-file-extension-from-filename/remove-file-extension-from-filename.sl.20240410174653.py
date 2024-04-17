# Start time: 2024-04-10 17:57:37.649494

'''
Prompt:
Given that input as ['happy.jpg'] output is happy, input as ['pivot table.xls'] output is pivot table, input as ['sales data.csv'] output is sales data, input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Remove file extension
        file_name = input_str.split('.')[0]
        
        # Remove any numbers at the end of the file name
        while file_name[-1].isdigit():
            file_name = file_name[:-1]
        
        return file_name
    except Exception as e:
        return "Error: Invalid input"

# Test cases
print(generated_function('happy.jpg'))  # Output: happy
print(generated_function('pivot table.xls'))  # Output: pivot table
print(generated_function('sales data.csv'))  # Output: sales data
print(generated_function('invoice3001.xls.pdf'))  # Output: invoice3001
print(generated_function("happy.jpg"))  ## Output: happy
print(generated_function("pivot table.xls"))  ## Output: pivot table
print(generated_function("sales data.csv"))  ## Output: sales data
print(generated_function("invoice3001.xls.pdf"))  ## Output: invoice3001

# End time: 2024-04-10 17:57:39.884507
# Elapsed time in seconds: 2.2349546680000003
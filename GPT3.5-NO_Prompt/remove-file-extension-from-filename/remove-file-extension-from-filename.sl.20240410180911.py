# Start time: 2024-04-10 18:20:27.848379

'''
Prompt:
Given that input as ['happy.jpg'] output is happy, input as ['pivot table.xls'] output is pivot table, input as ['sales data.csv'] output is sales data, input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        filename = input_str.split('.')[0]
        return filename
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('happy.jpg'))
print(generated_function('pivot table.xls'))
print(generated_function('sales data.csv'))
print(generated_function('invoice3001.xls.pdf'))
print(generated_function("happy.jpg"))  ## Output: happy
print(generated_function("pivot table.xls"))  ## Output: pivot table
print(generated_function("sales data.csv"))  ## Output: sales data
print(generated_function("invoice3001.xls.pdf"))  ## Output: invoice3001

# End time: 2024-04-10 18:20:29.443146
# Elapsed time in seconds: 1.5947259260001374
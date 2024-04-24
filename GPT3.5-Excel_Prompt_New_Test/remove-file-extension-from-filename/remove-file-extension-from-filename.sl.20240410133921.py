# Start time: 2024-04-10 13:52:13.021713

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and input as ['happy.jpg'] output is happy, input as ['pivot table.xls'] output is pivot table, input as ['sales data.csv'] output is sales data, input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Remove the period and everything after in the input
    output = input_str.split('.')[0]
    
    return output

# Test cases
print(generated_function('happy.jpg'))
print(generated_function('pivot table.xls'))
print(generated_function('sales data.csv'))
print(generated_function('invoice3001.xls.pdf'))
print(generated_function("happy.jpg"))  ## Output: happy
print(generated_function("pivot table.xls"))  ## Output: pivot table
print(generated_function("sales data.csv"))  ## Output: sales data
print(generated_function("invoice3001.xls.pdf"))  ## Output: invoice3001

# End time: 2024-04-10 13:52:14.652109
# Elapsed time in seconds: 1.6303589930003


# APPEND TEST SCRIPTS...
print(generated_function("happy.jpg"))  ## Output: happy
print(generated_function("pivot table.xls"))  ## Output: pivot table
print(generated_function("sales data.csv"))  ## Output: sales data
print(generated_function("invoice3001.xls.pdf"))  ## Output: invoice3001


print(generated_function("invoice3022.xls.pdf"))  ### Output: invoice3022
print(generated_function("normal table.xls"))  ### Output: normal table
print(generated_function("sales sheet.csv"))  ### Output: sales sheet
print(generated_function("sad.jpg"))  ### Output: sad

# TEST SCRIPTS APPENDED!


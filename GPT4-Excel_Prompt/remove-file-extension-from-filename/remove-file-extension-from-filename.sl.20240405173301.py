# Start time: 2024-04-05 18:04:26.990717

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and input as ['happy.jpg'] output is happy, input as ['pivot table.xls'] output is pivot table, input as ['sales data.csv'] output is sales data, input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(filename):
    # Split the filename by the period and return the first part
    return filename.split('.')[0]

# Test cases
output1 = generated_function('happy.jpg')
output2 = generated_function('pivot table.xls')
output3 = generated_function('sales data.csv')
output4 = generated_function('invoice3001.xls.pdf')

# The outputs can be verified with external print or assert statements if needed
print(generated_function("happy.jpg"))  ## Output: happy
print(generated_function("pivot table.xls"))  ## Output: pivot table
print(generated_function("sales data.csv"))  ## Output: sales data
print(generated_function("invoice3001.xls.pdf"))  ## Output: invoice3001

# End time: 2024-04-05 18:04:29.579794
# Elapsed time in seconds: 2.589002120999794
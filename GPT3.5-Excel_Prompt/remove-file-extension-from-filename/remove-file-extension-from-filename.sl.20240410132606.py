# Start time: 2024-04-10 13:38:39.310892

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and input as ['happy.jpg'] output is happy, input as ['pivot table.xls'] output is pivot table, input as ['sales data.csv'] output is sales data, input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Find the index of the period in the input string
    period_index = input_str.find('.')
    
    # Extract the substring before the period
    output_str = input_str[:period_index]
    
    return output_str

# Test cases
print(generated_function('happy.jpg'))
print(generated_function('pivot table.xls'))
print(generated_function('sales data.csv'))
print(generated_function('invoice3001.xls.pdf'))
print(generated_function("happy.jpg"))  ## Output: happy
print(generated_function("pivot table.xls"))  ## Output: pivot table
print(generated_function("sales data.csv"))  ## Output: sales data
print(generated_function("invoice3001.xls.pdf"))  ## Output: invoice3001

# End time: 2024-04-10 13:38:41.501370
# Elapsed time in seconds: 2.1904297370001586
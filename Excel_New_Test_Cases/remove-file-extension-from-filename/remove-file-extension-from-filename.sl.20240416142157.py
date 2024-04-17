# Start time: 2024-04-16 14:33:44.788330

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and input as ['happy.jpg'] output is happy, input as ['pivot table.xls'] output is pivot table, input as ['sales data.csv'] output is sales data, input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the function to delete the period and everything after in the input
def generated_function(input_str):
    # Find the index of the period in the input string
    period_index = input_str.find('.')
    
    # If period is found, return the substring before the period
    if period_index != -1:
        return input_str[:period_index]
    
    # If period is not found, return the original input string
    return input_str

# Test cases
generated_function('happy.jpg')
generated_function('pivot table.xls')
generated_function('sales data.csv')
generated_function('invoice3001.xls.pdf')



print(generated_function("invoice3022.xls.pdf"))  ### Output: "invoice3022.xls.pdf"
print(generated_function("normal table.xls"))  ### Output: "normal table.xls"
print(generated_function("sales sheet.csv"))  ### Output: "sales sheet.csv"
print(generated_function("sad.jpg"))  ### Output: "sad.jpg"


print(generated_function("happy.jpg"))  ## Output: happy
print(generated_function("pivot table.xls"))  ## Output: pivot table
print(generated_function("sales data.csv"))  ## Output: sales data
print(generated_function("invoice3001.xls.pdf"))  ## Output: invoice3001



# End time: 2024-04-16 14:33:46.945638
# Elapsed time in seconds: 2.1564405760000227
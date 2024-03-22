# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg'] Output: happy
# Input: ['pivot table.xls'] Output: pivot table
# Input: ['sales data.csv'] Output: sales data
# Input: ['invoice3001.xls.pdf'] Output: invoice3001

def remove_extension(input_str):
    # Find the index of the last period in the input string
    index = input_str.rfind('.')
    
    # Return the input string up to the last period
    return input_str[:index]

# Test cases
print(remove_extension('happy.jpg'))  # Output: happy
print(remove_extension('pivot table.xls'))  # Output: pivot table
print(remove_extension('sales data.csv'))  # Output: sales data
print(remove_extension('invoice3001.xls.pdf'))  # Output: invoice3001
happy
pivot table
sales data
invoice3001

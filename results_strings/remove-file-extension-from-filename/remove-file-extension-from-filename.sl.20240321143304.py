# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg'] Output: happy
# Input: ['pivot table.xls'] Output: pivot table
# Input: ['sales data.csv'] Output: sales data
# Input: ['invoice3001.xls.pdf'] Output: invoice3001

def remove_extension(input_str):
    # Find the index of the period in the input string
    period_index = input_str.find('.')
    
    # Return the input string up to the period index
    return input_str[:period_index]

# Test cases
print(remove_extension('happy.jpg'))  # Output: happy
print(remove_extension('pivot table.xls'))  # Output: pivot table
print(remove_extension('sales data.csv'))  # Output: sales data
print(remove_extension('invoice3001.xls.pdf'))  # Output: invoice3001
happy
pivot table
sales data
invoice3001

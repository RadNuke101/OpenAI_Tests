# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg'] 
# Output: happy
# Input: ['pivot table.xls'] 
# Output: pivot table
# Input: ['sales data.csv'] 
# Output: sales data
# Input: ['invoice3001.xls.pdf'] 
# Output: invoice3001

def remove_extension(input_str):
    # Find the position of the period in the input string
    period_index = input_str.find('.')
    
    # Return the substring before the period
    return input_str[:period_index]

# Test cases
print(remove_extension('happy.jpg'))  # Output: happy
print(remove_extension('pivot table.xls'))  # Output: pivot table
print(remove_extension('sales data.csv'))  # Output: sales data
print(remove_extension('invoice3001.xls.pdf'))  # Output: invoice3001

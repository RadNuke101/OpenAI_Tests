# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg'] Output: happy
# Input: ['pivot table.xls'] Output: pivot table
# Input: ['sales data.csv'] Output: sales data
# Input: ['invoice3001.xls.pdf'] Output: invoice3001

def delete_extension(input_str):
    # Find the position of the last period in the input string
    period_index = input_str.rfind('.')
    
    # If a period is found, return the substring before it, otherwise return the original input
    if period_index != -1:
        return input_str[:period_index]
    else:
        return input_str

# Test cases
print(delete_extension('happy.jpg'))  # Output: happy
print(delete_extension('pivot table.xls'))  # Output: pivot table
print(delete_extension('sales data.csv'))  # Output: sales data
print(delete_extension('invoice3001.xls.pdf'))  # Output: invoice3001

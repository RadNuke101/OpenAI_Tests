# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg'] 
# Output: happy

def delete_extension(input_str):
    # Find the position of the period in the input string
    period_index = input_str.find('.')
    
    # If period exists, return the substring before the period
    if period_index != -1:
        return input_str[:period_index]
    else:
        return input_str

# Test cases
print(delete_extension('happy.jpg'))  # Output: happy
print(delete_extension('pivot table.xls'))  # Output: pivot table
print(delete_extension('sales data.csv'))  # Output: sales data
print(delete_extension('invoice3001.xls.pdf'))  # Output: invoice3001

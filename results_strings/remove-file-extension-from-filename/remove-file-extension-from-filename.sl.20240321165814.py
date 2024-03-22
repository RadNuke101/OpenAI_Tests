# Prompt: delete the period and everything after in the input
# Input: 'happy.jpg' 
# Output: 'happy'

def delete_extension(input_str):
    # Find the index of the period
    period_index = input_str.find('.')
    
    # Return the substring before the period
    return input_str[:period_index]

# Test cases
print(delete_extension('happy.jpg'))  # Output: 'happy'
print(delete_extension('pivot table.xls'))  # Output: 'pivot table'
print(delete_extension('sales data.csv'))  # Output: 'sales data'
print(delete_extension('invoice3001.xls.pdf'))  # Output: 'invoice3001'

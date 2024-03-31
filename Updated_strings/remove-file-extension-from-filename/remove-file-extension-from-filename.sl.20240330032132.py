# Start time: 2024-03-30 03:38:06.078787
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and given input as ['happy.jpg'] output is happy, given input as ['pivot table.xls'] output is pivot table, given input as ['sales data.csv'] output is sales data, given input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete the period and everything after in the input
# Input: 'happy.jpg' 
# Output: 'happy'
# Input: 'pivot table.xls'
# Output: 'pivot table'
# Input: 'sales data.csv'
# Output: 'sales data'
# Input: 'invoice3001.xls.pdf'
# Output: 'invoice3001'

def remove_extension(input_str):
    try:
        # Find the index of the last occurrence of '.'
        index = input_str.rfind('.')
        
        # If '.' is not found, return the original input
        if index == -1:
            return input_str
        
        # Return the input string up to the last occurrence of '.'
        return input_str[:index]
    
    except Exception as e:
        return str(e)

# Test cases
print(remove_extension('happy.jpg'))  # Output: happy
print(remove_extension('pivot table.xls'))  # Output: pivot table
print(remove_extension('sales data.csv'))  # Output: sales data
print(remove_extension('invoice3001.xls.pdf'))  # Output: invoice3001

# End time: 2024-03-30 03:38:08.057736
# Elapsed time in seconds: 1.9789005399998132
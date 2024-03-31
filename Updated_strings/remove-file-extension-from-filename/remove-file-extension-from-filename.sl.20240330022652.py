# Start time: 2024-03-30 02:44:25.676257
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and given input as ['happy.jpg'] output is happy, given input as ['pivot table.xls'] output is pivot table, given input as ['sales data.csv'] output is sales data, given input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg']
# Output: happy

def delete_extension(input_str):
    try:
        # Remove the extension by finding the index of the last period
        index = input_str.index('.')
        output_str = input_str[:index]
        return output_str
    except ValueError:
        return "Invalid input"

# Test cases
print(delete_extension('happy.jpg'))  # Output: happy
print(delete_extension('pivot table.xls'))  # Output: pivot table
print(delete_extension('sales data.csv'))  # Output: sales data
print(delete_extension('invoice3001.xls.pdf'))  # Output: invoice3001

# End time: 2024-03-30 02:44:27.773547
# Elapsed time in seconds: 2.0972513500000787
# Start time: 2024-03-30 01:50:12.374685
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and given input as ['happy.jpg'] output is happy, given input as ['pivot table.xls'] output is pivot table, given input as ['sales data.csv'] output is sales data, given input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg']
# Output: happy

def extract_filename(input_str):
    try:
        # Extracting the filename from the input string
        filename = input_str.split('.')[0]
        return filename
    except:
        return "Invalid input"

# Test cases
print(extract_filename('happy.jpg'))  # Output: happy
print(extract_filename('pivot table.xls'))  # Output: pivot table
print(extract_filename('sales data.csv'))  # Output: sales data
print(extract_filename('invoice3001.xls.pdf'))  # Output: invoice3001

# End time: 2024-03-30 01:50:15.964953
# Elapsed time in seconds: 3.5901969719998306
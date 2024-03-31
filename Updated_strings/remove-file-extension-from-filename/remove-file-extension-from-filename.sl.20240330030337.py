# Start time: 2024-03-30 03:20:24.622490
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the period and everything after in the input, and given input as ['happy.jpg'] output is happy, given input as ['pivot table.xls'] output is pivot table, given input as ['sales data.csv'] output is sales data, given input as ['invoice3001.xls.pdf'] output is invoice3001, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete the period and everything after in the input
# Input: ['happy.jpg']
# Output: happy

def delete_period(input_str):
    try:
        # Remove the period and everything after it
        output_str = input_str.split('.')[0]
        return output_str
    except Exception as e:
        print("Error: ", e)

# Test cases
print(delete_period('happy.jpg'))  # Output: happy
print(delete_period('pivot table.xls'))  # Output: pivot table
print(delete_period('sales data.csv'))  # Output: sales data
print(delete_period('invoice3001.xls.pdf'))  # Output: invoice3001

# End time: 2024-03-30 03:20:29.751565
# Elapsed time in seconds: 5.128924840000764
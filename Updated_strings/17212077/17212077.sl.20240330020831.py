# Start time: 2024-03-30 02:24:32.855210
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: delete the first "/" (from the left) and the next two numbers after, and given input as ['01/15/2013'] output is 01/2013, given input as ['03/07/2011'] output is 03/2011, given input as ['05/09/2009'] output is 05/2009, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: delete the first "/" (from the left) and the next two numbers after
# Input: ['01/15/2013'] Output: 01/2013
# Input: ['03/07/2011'] Output: 03/2011
# Input: ['05/09/2009'] Output: 05/2009

def delete_numbers(input_str):
    try:
        # Extract the date part before and after the first "/"
        date_parts = input_str.split('/')
        month = date_parts[0]
        year = date_parts[2]

        # Remove the first "/" and the next two numbers after it
        output_str = month + '/' + year

        return output_str
    except (IndexError, ValueError):
        return "Invalid input format"

# Test cases
print(delete_numbers('01/15/2013'))  # Output: 01/2013
print(delete_numbers('03/07/2011'))  # Output: 03/2011
print(delete_numbers('05/09/2009'))  # Output: 05/2009
print(delete_numbers('invalid_input'))  # Output: Invalid input format

# End time: 2024-03-30 02:24:36.819588
# Elapsed time in seconds: 3.9642791859987483
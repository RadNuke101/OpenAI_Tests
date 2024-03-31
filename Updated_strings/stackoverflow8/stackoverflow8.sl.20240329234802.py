# Start time: 2024-03-29 23:56:42.844060
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return everything after the last "/" in input, and given input as ['home/Excel/Sheet1.xls'] output is Sheet1.xls, given input as ['home/user/Sheet1.xls'] output is Sheet1.xls, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return everything after the last "/" in input
# Input: 'home/Excel/Sheet1.xls'
# Output: 'Sheet1.xls'

def get_last_part(input_str):
    try:
        parts = input_str.split('/')
        return parts[-1]
    except Exception as e:
        print("Error: ", e)

# Test cases
print(get_last_part('home/Excel/Sheet1.xls'))  # Output: 'Sheet1.xls'
print(get_last_part('home/user/Sheet1.xls'))   # Output: 'Sheet1.xls'

# End time: 2024-03-29 23:56:45.583252
# Elapsed time in seconds: 2.739085226000043
# Start time: 2024-03-30 00:42:54.889375
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression, and given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression
# Input: ['chang,amy'] Output: amy,chang
# Input: ['smith,bobby'] Output: bobby,smith
# Input: ['lennox,aaron'] Output: aaron,lennox

def rearrange_names(input_str):
    try:
        input_str = input_str[0]  # Extract the string from the list
        parts = input_str.split(',')  # Split the string at the comma
        if len(parts) != 2:
            raise ValueError("Input format should be 'lastname,firstname'")
        
        return parts[1] + ',' + parts[0]  # Rearrange the parts and add a comma
    except (IndexError, ValueError):
        return "Invalid input format"

# Test cases
print(rearrange_names(['chang,amy']))  # Output: amy,chang
print(rearrange_names(['smith,bobby']))  # Output: bobby,smith
print(rearrange_names(['lennox,aaron']))  # Output: aaron,lennox
print(rearrange_names(['invalidinput']))  # Output: Invalid input format

# End time: 2024-03-30 00:42:59.790780
# Elapsed time in seconds: 4.9012723739997455
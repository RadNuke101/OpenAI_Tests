# Start time: 2024-03-30 03:58:14.281222
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
        
        output_str = parts[1] + ',' + parts[0]  # Rearrange the parts
        return output_str
    except (IndexError, ValueError) as e:
        return "Invalid input format. Please provide input in the format 'lastname,firstname'."

# Test cases
print(rearrange_names(['chang,amy']))  # Output: amy,chang
print(rearrange_names(['smith,bobby']))  # Output: bobby,smith
print(rearrange_names(['lennox,aaron']))  # Output: aaron,lennox
print(rearrange_names(['invalidinput']))  # Output: Invalid input format. Please provide input in the format 'lastname,firstname'.

# End time: 2024-03-30 03:58:18.039936
# Elapsed time in seconds: 3.7586298559999705
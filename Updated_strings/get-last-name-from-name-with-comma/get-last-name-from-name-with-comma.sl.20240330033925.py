# Start time: 2024-03-30 03:41:01.654633
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression, and given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression
# Input: ['chang,amy'] Output: amy,chang
# Input: ['smith,bobby'] Output: bobby,smith
# Input: ['lennox,aaron'] Output: aaron,lennox

def rearrange_names(input_str):
    try:
        # Extracting the names before and after the comma
        names = input_str.split(',')
        first_name = names[1]
        last_name = names[0]

        # Rearranging the names
        rearranged_names = first_name + ',' + last_name

        return rearranged_names
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
print(rearrange_names('chang,amy'))  # Output: amy,chang
print(rearrange_names('smith,bobby'))  # Output: bobby,smith
print(rearrange_names('lennox,aaron'))  # Output: aaron,lennox

# End time: 2024-03-30 03:41:04.828456
# Elapsed time in seconds: 3.1737082569998165
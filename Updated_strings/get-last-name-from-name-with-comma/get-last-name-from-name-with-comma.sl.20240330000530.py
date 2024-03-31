# Start time: 2024-03-30 00:07:12.935532
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression, and given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression
# Input: ['chang,amy'] Output: amy,chang
# Input: ['smith,bobby'] Output: bobby,smith
# Input: ['lennox,aaron'] Output: aaron,lennox

def process_input(input_str):
    try:
        # Split the input string at the comma
        parts = input_str.split(',')
        
        # Rearrange the parts and join them with a comma
        output_str = parts[1] + ',' + parts[0]
        
        return output_str
    except Exception as e:
        return "Error processing input: {}".format(str(e))

# Test cases
print(process_input('chang,amy'))  # Output: amy,chang
print(process_input('smith,bobby'))  # Output: bobby,smith
print(process_input('lennox,aaron'))  # Output: aaron,lennox

# End time: 2024-03-30 00:07:17.809814
# Elapsed time in seconds: 4.874129901999822
# Start time: 2024-03-30 04:37:20.130158
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the phrase (space on atleast one end) in the inputted expression that ends with ".com", and given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_com_phrase(input_str):
    try:
        # Extracting the phrase that ends with ".com"
        phrase = [word for word in input_str.split() if word.endswith(".com")][0]
        return phrase
    except IndexError:
        return "No phrase ending with '.com' found in the input"

# Test cases
print(find_com_phrase('send email to json_acme.com'))  # Output: json_acme.com
print(find_com_phrase('contact help_robot.com for all support requests'))  # Output: help_robot.com

# End time: 2024-03-30 04:37:22.735585
# Elapsed time in seconds: 2.605341310998483
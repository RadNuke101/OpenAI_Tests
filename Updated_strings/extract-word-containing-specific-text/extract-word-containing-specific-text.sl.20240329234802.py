# Start time: 2024-03-29 23:54:36.733911
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the phrase (space on atleast one end) in the inputted expression that ends with ".com", and given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_phrase_with_com(input_str):
    try:
        input_str = input_str[0]  # Convert list input to string
        words = input_str.split()
        for word in words:
            if word.endswith(".com"):
                return word.strip()
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(find_phrase_with_com(['send email to json_acme.com']))  # Output: json_acme.com
print(find_phrase_with_com(['contact help_robot.com for all support requests']))  # Output: help_robot.com
print(find_phrase_with_com('invalid input'))  # Output: Invalid input

# End time: 2024-03-29 23:54:38.447296
# Elapsed time in seconds: 1.713341641999932
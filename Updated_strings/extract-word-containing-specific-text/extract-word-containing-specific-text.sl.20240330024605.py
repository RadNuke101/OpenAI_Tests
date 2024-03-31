# Start time: 2024-03-30 02:52:54.100320
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the phrase (space on atleast one end) in the inputted expression that ends with ".com", and given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

# Input: ['contact help_robot.com for all support requests']
# Output: help_robot.com

def find_phrase_with_com(input_str):
    try:
        input_str = input_str[0]  # Extracting the string from the list
        words = input_str.split()  # Splitting the string into words
        for word in words:
            if word.endswith(".com"):
                return word.strip()  # Removing any leading or trailing spaces
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(find_phrase_with_com(['send email to json_acme.com']))  # Output: json_acme.com
print(find_phrase_with_com(['contact help_robot.com for all support requests']))  # Output: help_robot.com

# End time: 2024-03-30 02:52:59.906891
# Elapsed time in seconds: 5.806441575001372
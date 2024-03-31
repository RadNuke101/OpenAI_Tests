# Start time: 2024-03-30 03:10:31.333143
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the phrase (space on atleast one end) in the inputted expression that ends with ".com", and given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: return the phrase (space on atleast one end) in the inputted expression that ends with ".com"
# Input: ['send email to json_acme.com']
# Output: json_acme.com

def find_com_phrase(input_str):
    try:
        # Check if input is a list and extract the string
        if isinstance(input_str, list):
            input_str = input_str[0]
        
        # Split the input string by spaces
        words = input_str.split()
        
        # Find the phrase that ends with ".com"
        com_phrase = [word for word in words if word.endswith(".com")][0]
        
        return com_phrase
    except Exception as e:
        return "Error: Invalid input"

# Test cases
print(find_com_phrase(['send email to json_acme.com']))  # Output: json_acme.com
print(find_com_phrase(['contact help_robot.com for all support requests']))  # Output: help_robot.com
print(find_com_phrase('invalid input'))  # Output: Error: Invalid input

# End time: 2024-03-30 03:10:36.640443
# Elapsed time in seconds: 5.307155782000336
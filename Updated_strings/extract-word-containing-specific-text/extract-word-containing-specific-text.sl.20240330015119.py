# Start time: 2024-03-30 01:58:13.069508
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
input1 = 'send email to json_acme.com'
input2 = 'contact help_robot.com for all support requests'

print(find_com_phrase(input1))  # Output: json_acme.com
print(find_com_phrase(input2))  # Output: help_robot.com

# End time: 2024-03-30 01:58:17.975632
# Elapsed time in seconds: 4.9060365130007995
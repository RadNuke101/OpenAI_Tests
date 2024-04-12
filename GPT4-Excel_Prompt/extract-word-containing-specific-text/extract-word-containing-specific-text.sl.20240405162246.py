# Start time: 2024-04-05 16:38:24.617966

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the phrase (space on atleast one end) in the inputted expression that ends with ".com", and input as ['send email to json_acme.com'] output is json_acme.com, input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

import re

def generated_function(expression):
    # Use regular expression to find a phrase that ends with ".com" and has space on at least one end
    match = re.search(r'\s([^\s]*\.com)', expression)
    if match:
        # Return the matched phrase without the leading space
        return match.group(1)
    else:
        # If no match is found, return an empty string
        return ""

# Test cases
print(generated_function('send email to json_acme.com'))
print(generated_function('contact help_robot.com for all support requests'))
print(generated_function("send email to json_acme.com"))  ## Output: json_acme.com
print(generated_function("contact help_robot.com for all support requests"))  ## Output: help_robot.com

# End time: 2024-04-05 16:38:29.001502
# Elapsed time in seconds: 4.383843900000102
# Start time: 2024-03-30 22:20:33.174603

# Content: Given that given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'send email to json_acme.com'
# Output: json_acme.com

def extract_domain(input_str):
    try:
        start_index = input_str.index('to ') + 3
        end_index = input_str.index('.')
        domain = input_str[start_index:end_index]
        return domain
    except ValueError:
        print("Invalid input format. Please provide a valid input string.")
        return None

# Test cases
print(extract_domain('send email to json_acme.com'))  # Output: json_acme.com
print(extract_domain('contact help_robot.com for all support requests'))  # Output: help_robot.com

# End time: 2024-03-30 22:20:34.307673
# Elapsed time in seconds: 1.1330344329999207
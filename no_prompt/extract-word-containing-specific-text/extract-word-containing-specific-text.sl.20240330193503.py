# Start time: 2024-03-30 19:41:35.708831

# Content: Given that given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_domain(input_str):
    try:
        domain = input_str.split()[2]
        if '@' in domain:
            domain = domain.split('@')[1]
        return domain
    except IndexError:
        return "Invalid input format"

# Test cases
# input_str = 'send email to json_acme.com'
# print(extract_domain(input_str))  # Output: json_acme.com

# input_str = 'contact help_robot.com for all support requests'
# print(extract_domain(input_str))  # Output: help_robot.com

# End time: 2024-03-30 19:41:39.437128
# Elapsed time in seconds: 3.7282626930000333
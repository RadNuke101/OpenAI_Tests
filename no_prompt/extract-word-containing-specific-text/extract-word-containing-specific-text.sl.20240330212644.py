# Start time: 2024-03-30 21:33:04.667231

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
# print(extract_domain('send email to json_acme.com'))  # Output: json_acme.com
# print(extract_domain('contact help_robot.com for all support requests'))  # Output: help_robot.com
# print(extract_domain('invalid input'))  # Output: Invalid input format

# End time: 2024-03-30 21:33:07.094465
# Elapsed time in seconds: 2.4271544849998463
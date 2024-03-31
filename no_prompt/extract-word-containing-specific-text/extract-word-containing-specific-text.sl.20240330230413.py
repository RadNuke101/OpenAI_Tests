# Start time: 2024-03-30 23:11:48.402616

# Content: Given that given input as ['send email to json_acme.com'] output is json_acme.com, given input as ['contact help_robot.com for all support requests'] output is help_robot.com, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_domain(input_str):
    try:
        # Input: 'send email to json_acme.com'
        # Output: json_acme.com
        domain = input_str.split()[-1]
        if '@' in domain:
            domain = domain.split('@')[-1]
        return domain
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_domain('send email to json_acme.com'))  # json_acme.com
print(extract_domain('contact help_robot.com for all support requests'))  # help_robot.com

# End time: 2024-03-30 23:11:50.335234
# Elapsed time in seconds: 1.9325802430030308
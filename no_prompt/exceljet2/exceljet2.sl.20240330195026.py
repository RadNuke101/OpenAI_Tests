# Start time: 2024-03-30 19:59:47.671362

# Content: Given that given input as ['www.domain.com'] output is com, given input as ['mail.net'] output is net, given input as ['www.amaon.co.uk'] output is uk, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_domain_extension(input_str):
    try:
        domain = input_str.split('.')[-1]
        return domain
    except (AttributeError, IndexError):
        return "Invalid input"

# Test cases
# print(extract_domain_extension('www.domain.com'))  # com
# print(extract_domain_extension('mail.net'))  # net
# print(extract_domain_extension('www.amaon.co.uk'))  # uk

# End time: 2024-03-30 19:59:48.905760
# Elapsed time in seconds: 1.234375204000571
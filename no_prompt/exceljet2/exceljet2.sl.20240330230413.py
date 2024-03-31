# Start time: 2024-03-30 23:14:40.709349

# Content: Given that given input as ['www.domain.com'] output is com, given input as ['mail.net'] output is net, given input as ['www.amaon.co.uk'] output is uk, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_domain_extension(domain):
    try:
        parts = domain.split('.')
        extension = parts[-1]
        return extension
    except (AttributeError, IndexError):
        return "Invalid input"

# Test cases
# print(get_domain_extension('www.domain.com'))  # Output: com
# print(get_domain_extension('mail.net'))  # Output: net
# print(get_domain_extension('www.amaon.co.uk'))  # Output: uk

# End time: 2024-03-30 23:14:41.814758
# Elapsed time in seconds: 1.1053843250010686
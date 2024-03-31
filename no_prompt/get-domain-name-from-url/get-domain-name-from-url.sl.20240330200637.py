# Start time: 2024-03-30 20:15:36.841844

# Content: Given that given input as ['https=//abc.com/def'] output is https=//abc.com/, given input as ['http=//www.abc.com/def/cef'] output is http=//www.abc.com, given input as ['http=//chandoo.org/wp/def-def'] output is http=//chandoo.org/, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_url(input_str):
    try:
        url = input_str.split('=//')[0] + '=//' + input_str.split('=//')[1].split('/')[0]
        return url
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
# input_str = 'https=//abc.com/def'
# input_str = 'http=//www.abc.com/def/cef'
# input_str = 'http=//chandoo.org/wp/def-def'

# End time: 2024-03-30 20:15:38.406074
# Elapsed time in seconds: 1.5642097489999287
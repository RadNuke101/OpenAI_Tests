# Start time: 2024-03-30 18:40:24.652668

# Content: Given that given input as ['https=//abc.com/def'] output is https=//abc.com/, given input as ['http=//www.abc.com/def/cef'] output is http=//www.abc.com, given input as ['http=//chandoo.org/wp/def-def'] output is http=//chandoo.org/, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'https=//abc.com/def'
# Output: 'https=//abc.com/'

def extract_url(input_str):
    try:
        url = input_str.split('=')[1].split('/')[0]
        return input_str.split('=')[0] + '=' + url + '/'
    except IndexError:
        return "Invalid input format"

# Test cases
print(extract_url('https=//abc.com/def'))  # Output: 'https=//abc.com/'
print(extract_url('http=//www.abc.com/def/cef'))  # Output: 'http=//www.abc.com'
print(extract_url('http=//chandoo.org/wp/def-def'))  # Output: 'http=//chandoo.org/'

# End time: 2024-03-30 18:40:27.984926
# Elapsed time in seconds: 3.3321635450000144
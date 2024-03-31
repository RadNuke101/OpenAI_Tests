# Start time: 2024-03-30 19:43:19.888690

# Content: Given that given input as ['https=//abc.com/def'] output is https=//abc.com/, given input as ['http=//www.abc.com/def/cef'] output is http=//www.abc.com, given input as ['http=//chandoo.org/wp/def-def'] output is http=//chandoo.org/, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'https=//abc.com/def'
# Output: 'https=//abc.com/'

def match_input_output(input_str):
    try:
        input_str = input_str.strip()
        protocol, url = input_str.split('=')
        url = url.split('/')[0]
        output_str = f'{protocol}={url}/'
        return output_str
    except Exception as e:
        return f'Error: {e}'

# Test cases
print(match_input_output('https=//abc.com/def'))
print(match_input_output('http=//www.abc.com/def/cef'))
print(match_input_output('http=//chandoo.org/wp/def-def'))

# End time: 2024-03-30 19:43:21.764799
# Elapsed time in seconds: 1.8760874539993893
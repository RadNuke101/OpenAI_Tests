# Start time: 2024-03-30 20:09:46.661013

# Content: Given that given input as ['valentine day=1915=50==7.1=45'] output is valentine day, given input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_title(input_str):
    try:
        # Input: 'valentine day=1915=50==7.1=45'
        # Output: 'valentine day'
        parts = input_str.split('=')
        title = parts[0]
        return title
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_title_with_comma(input_str):
    try:
        # Input: 'movie blah=2blahblah, The=1914=54==7.9=17'
        # Output: 'movie blah=2blahblah, The, '
        parts = input_str.split('=')
        title = '='.join(parts[:-4])
        return title
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
input_str1 = 'valentine day=1915=50==7.1=45'
input_str2 = 'movie blah=2blahblah, The=1914=54==7.9=17'

print(extract_title(input_str1))
print(extract_title_with_comma(input_str2))

# End time: 2024-03-30 20:09:48.937073
# Elapsed time in seconds: 2.2760392100008175
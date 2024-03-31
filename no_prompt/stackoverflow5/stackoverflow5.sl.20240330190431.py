# Start time: 2024-03-30 19:08:06.107942

# Content: Given that given input as ['valentine day=1915=50==7.1=45'] output is valentine day, given input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'valentine day=1915=50==7.1=45'
# Output: 'valentine day'

# Input: 'movie blah=2blahblah, The=1914=54==7.9=17'
# Output: 'movie blah=2blahblah, The'

def extract_title(input_str):
    try:
        parts = input_str.split('=')
        title = parts[0]
        return title
    except (IndexError, AttributeError):
        return ""

# Test cases
input1 = 'valentine day=1915=50==7.1=45'
input2 = 'movie blah=2blahblah, The=1914=54==7.9=17'

output1 = extract_title(input1)
output2 = extract_title(input2)

# End time: 2024-03-30 19:08:09.653493
# Elapsed time in seconds: 3.545447058999798
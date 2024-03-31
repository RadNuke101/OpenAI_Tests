# Start time: 2024-03-30 18:51:50.203090

# Content: Given that given input as ['valentine day=1915=50==7.1=45'] output is valentine day, given input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_title(input_str):
    try:
        # Input: 'valentine day=1915=50==7.1=45'
        parts = input_str.split('=')
        title = parts[0]
        return title
    except Exception as e:
        return None

# Test cases
input1 = 'valentine day=1915=50==7.1=45'
output1 = extract_title(input1)
print(output1)

input2 = 'movie blah=2blahblah, The=1914=54==7.9=17'
output2 = extract_title(input2)
print(output2)

# End time: 2024-03-30 18:51:52.949422
# Elapsed time in seconds: 2.7462607180000305
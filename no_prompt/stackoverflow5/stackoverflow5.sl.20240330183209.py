# Start time: 2024-03-30 18:35:27.816354

# Content: Given that given input as ['valentine day=1915=50==7.1=45'] output is valentine day, given input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_title(input_str):
    try:
        # Input: 'valentine day=1915=50==7.1=45'
        parts = input_str.split('=')
        title = parts[0]
        return title
    except Exception as e:
        print("Error: ", e)
        return None

# Test cases
input_str1 = 'valentine day=1915=50==7.1=45'
input_str2 = 'movie blah=2blahblah, The=1914=54==7.9=17'

output1 = extract_title(input_str1)
output2 = extract_title(input_str2)

print(output1)
print(output2)

# End time: 2024-03-30 18:35:29.207787
# Elapsed time in seconds: 1.3913975270000094
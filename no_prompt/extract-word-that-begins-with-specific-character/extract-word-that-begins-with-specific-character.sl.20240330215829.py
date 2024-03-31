# Start time: 2024-03-30 22:07:49.032273

# Content: Given that given input as ['this is a _username in the middle'] output is _username, given input as ['twitter names look like= _name'] output is _name, given input as ['with two _name1 and _name2'] output is _name1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'this is a _username in the middle'
# Output: _username

def extract_username(input_str):
    try:
        start_index = input_str.index('_')
        end_index = start_index + 1
        while end_index < len(input_str) and input_str[end_index].isalnum():
            end_index += 1
        return input_str[start_index:end_index]
    except ValueError:
        return None

# Test cases
print(extract_username('this is a _username in the middle'))  # Output: _username
print(extract_username('twitter names look like= _name'))      # Output: _name
print(extract_username('with two _name1 and _name2'))          # Output: _name1

# End time: 2024-03-30 22:07:52.281270
# Elapsed time in seconds: 3.248903245001202
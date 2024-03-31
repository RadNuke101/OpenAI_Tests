# Start time: 2024-03-30 20:27:31.698844

# Content: Given that given input as ['valentine day=1915=50==7.1=45'] output is valentine day, given input as ['movie blah=2blahblah, The=1914=54==7.9=17'] output is movie blah=2blahblah, The, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_title(input_str):
    try:
        # Input: 'valentine day=1915=50==7.1=45'
        parts = input_str.split('=')
        title = parts[0]
        return title
    except Exception as e:
        print(f"Error: {e}")
        return None

def extract_title_with_commas(input_str):
    try:
        # Input: 'movie blah=2blahblah, The=1914=54==7.9=17'
        parts = input_str.split('=')
        title = '='.join(parts[:-4])
        return title
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test cases
print(extract_title('valentine day=1915=50==7.1=45'))  # Output: valentine day
print(extract_title_with_commas('movie blah=2blahblah, The=1914=54==7.9=17'))  # Output: movie blah=2blahblah, The

# End time: 2024-03-30 20:27:35.618849
# Elapsed time in seconds: 3.9198956029995315
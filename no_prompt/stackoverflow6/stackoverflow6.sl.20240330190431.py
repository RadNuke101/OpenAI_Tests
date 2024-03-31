# Start time: 2024-03-30 19:17:37.816827

# Content: Given that given input as ['Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'] output is loren ipsum, given input as ['Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'] output is loren, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_text(input_string):
    try:
        # Input: 'Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'
        # Output: 'loren ipsum'
        # Input: 'Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'
        # Output: 'loren'
        
        # Split the input string by '='
        parts = input_string.split('=')
        
        # Get the last part after splitting by '=' and remove any leading or trailing spaces
        result = parts[-1].strip()
        
        return result
    except Exception as e:
        return str(e)

# Test cases
print(extract_text('Dec 2, 2014, 11=23 PM - +91 90000 80000= loren ipsum'))  # Output should be 'loren ipsum'
print(extract_text('Dec 2, 2014, 11=24 PM - +91 90000 80000= loren'))  # Output should be 'loren'

# End time: 2024-03-30 19:17:42.071264
# Elapsed time in seconds: 4.2543121579997205
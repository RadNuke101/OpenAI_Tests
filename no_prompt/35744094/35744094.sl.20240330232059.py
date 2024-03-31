# Start time: 2024-03-30 23:33:40.398044

# Content: Given that given input as ['http=//www.apple.com/uk/mac'] output is mac, given input as ['https=//www.microsoft.com/en-gb/windows'] output is windows, given input as ['https=//www.microsoft.com/'] output is microsoft, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_keyword(input_str):
    try:
        # Input: 'http=//www.apple.com/uk/mac'
        # Output: 'mac'
        
        # Input: 'https=//www.microsoft.com/en-gb/windows'
        # Output: 'windows'
        
        # Input: 'https=//www.microsoft.com/'
        # Output: 'microsoft'
        
        keyword = input_str.split('/')[-1]
        keyword = keyword.split('=')[-1]
        
        return keyword
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
print(extract_keyword('http=//www.apple.com/uk/mac'))  # mac
print(extract_keyword('https=//www.microsoft.com/en-gb/windows'))  # windows
print(extract_keyword('https=//www.microsoft.com/'))  # microsoft

# End time: 2024-03-30 23:33:42.981832
# Elapsed time in seconds: 2.5837096119976195
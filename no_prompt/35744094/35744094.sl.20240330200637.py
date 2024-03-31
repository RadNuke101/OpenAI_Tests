# Start time: 2024-03-30 20:20:59.005285

# Content: Given that given input as ['http=//www.apple.com/uk/mac'] output is mac, given input as ['https=//www.microsoft.com/en-gb/windows'] output is windows, given input as ['https=//www.microsoft.com/'] output is microsoft, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_keyword(input_str):
    try:
        # Input: 'http=//www.apple.com/uk/mac'
        # Output: 'mac'
        
        # Input: 'https=//www.microsoft.com/en-gb/windows'
        # Output: 'windows'
        
        # Input: 'https=//www.microsoft.com/'
        # Output: 'microsoft'
        
        key_value = input_str.split('=//')[-1]
        keyword = key_value.split('/')[-1]
        
        return keyword
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
print(extract_keyword('http=//www.apple.com/uk/mac'))
print(extract_keyword('https=//www.microsoft.com/en-gb/windows'))
print(extract_keyword('https=//www.microsoft.com/'))

# End time: 2024-03-30 20:21:02.083600
# Elapsed time in seconds: 3.078125822000402
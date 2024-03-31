# Start time: 2024-03-30 20:04:10.214447

# Content: Given that given input as ['http=//www.apple.com/uk/mac'] output is mac, given input as ['https=//www.microsoft.com/en-gb/windows'] output is windows, given input as ['https=//www.microsoft.com/'] output is microsoft, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(input_str):
    try:
        # Input: 'http=//www.apple.com/uk/mac'
        # Output: 'mac'
        
        # Input: 'https=//www.microsoft.com/en-gb/windows'
        # Output: 'windows'
        
        # Input: 'https=//www.microsoft.com/'
        # Output: 'microsoft'
        
        key_value = input_str.split('=//')
        domain = key_value[1].split('/')[0]
        parts = domain.split('.')
        if len(parts) > 1:
            return parts[-1]
        else:
            return parts[0]
    except Exception as e:
        print("Error:", e)

# Test cases
print(extract_info('http=//www.apple.com/uk/mac'))
print(extract_info('https=//www.microsoft.com/en-gb/windows'))
print(extract_info('https=//www.microsoft.com/'))

# End time: 2024-03-30 20:04:15.314895
# Elapsed time in seconds: 5.10036493700045
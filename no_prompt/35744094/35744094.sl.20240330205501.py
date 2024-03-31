# Start time: 2024-03-30 21:08:39.280102

# Content: Given that given input as ['http=//www.apple.com/uk/mac'] output is mac, given input as ['https=//www.microsoft.com/en-gb/windows'] output is windows, given input as ['https=//www.microsoft.com/'] output is microsoft, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'http=//www.apple.com/uk/mac'
# output: mac

# input: 'https=//www.microsoft.com/en-gb/windows'
# output: windows

# input: 'https=//www.microsoft.com/'
# output: microsoft

def extract_name(input_str):
    try:
        # Split the input string by '=' and '/'
        parts = input_str.split('=//')
        
        # Extract the last part after splitting by '/'
        name = parts[-1].split('/')[-1]
        
        return name
    except Exception as e:
        print("Error: {}".format(e))

# Test the function with the provided test cases
print(extract_name('http=//www.apple.com/uk/mac'))
print(extract_name('https=//www.microsoft.com/en-gb/windows'))
print(extract_name('https=//www.microsoft.com/'))

# End time: 2024-03-30 21:08:43.421417
# Elapsed time in seconds: 4.141220642999542
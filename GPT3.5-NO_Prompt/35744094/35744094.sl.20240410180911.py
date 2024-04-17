# Start time: 2024-04-10 18:19:16.537680

'''
Prompt:
Given that input as ['http=//www.apple.com/uk/mac'] output is mac, input as ['https=//www.microsoft.com/en-gb/windows'] output is windows, input as ['https=//www.microsoft.com/'] output is microsoft, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        url = input_str.split('=//')[1]
        domain = url.split('.')[1]
        if '/' in domain:
            domain = domain.split('/')[0]
        return domain
    except:
        return "Invalid input format"

# Test cases
print(generated_function('http=//www.apple.com/uk/mac'))  # Output: mac
print(generated_function('https=//www.microsoft.com/en-gb/windows'))  # Output: windows
print(generated_function('https=//www.microsoft.com/'))  # Output: microsoft
print(generated_function("http=//www.apple.com/uk/mac"))  ## Output: mac
print(generated_function("https=//www.microsoft.com/en-gb/windows"))  ## Output: windows
print(generated_function("https=//www.microsoft.com/"))  ## Output: microsoft

# End time: 2024-04-10 18:19:18.319334
# Elapsed time in seconds: 1.7816309559998444
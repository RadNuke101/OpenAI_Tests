# Start time: 2024-04-10 18:07:25.464846

'''
Prompt:
Given that input as ['http=//www.apple.com/uk/mac'] output is mac, input as ['https=//www.microsoft.com/en-gb/windows'] output is windows, input as ['https=//www.microsoft.com/'] output is microsoft, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Extracting the domain from the input string
        domain = input_str.split('=//')[1].split('.')[1]
        
        # Extracting the page from the input string
        page = input_str.split('/')[-1]
        
        # Removing any hyphens from the page name
        page = page.replace('-', ' ')
        
        return page if page != domain else domain
    except Exception as e:
        return "Invalid input"

# Test cases
print(generated_function('http=//www.apple.com/uk/mac'))  # mac
print(generated_function('https=//www.microsoft.com/en-gb/windows'))  # windows
print(generated_function('https=//www.microsoft.com/'))  # microsoft
print(generated_function("http=//www.apple.com/uk/mac"))  ## Output: mac
print(generated_function("https=//www.microsoft.com/en-gb/windows"))  ## Output: windows
print(generated_function("https=//www.microsoft.com/"))  ## Output: microsoft

# End time: 2024-04-10 18:07:27.645896
# Elapsed time in seconds: 2.181013105999682
# Start time: 2024-03-30 22:45:16.464769

# Content: Given that given input as ['http=//www.apple.com/uk/mac'] output is mac, given input as ['https=//www.microsoft.com/en-gb/windows'] output is windows, given input as ['https=//www.microsoft.com/'] output is microsoft, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'http=//www.apple.com/uk/mac'
# Output: mac

def extract_keyword(input_str):
    try:
        keyword = input_str.split('=//')[-1].split('/')[2]
        return keyword
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
print(extract_keyword('http=//www.apple.com/uk/mac'))  # mac
print(extract_keyword('https=//www.microsoft.com/en-gb/windows'))  # windows
print(extract_keyword('https=//www.microsoft.com/'))  # microsoft

# End time: 2024-03-30 22:45:17.934250
# Elapsed time in seconds: 1.4694445759996597
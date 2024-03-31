# Start time: 2024-03-30 21:49:05.505390

# Content: Given that given input as ['https=//exceljet.net/catalog'] output is exceljet.net/catalog, given input as ['https=//microsoft.com'] output is microsoft.com, given input as ['ftp=//someserver.com'] output is someserver.com, given input as ['sftp=//127.0.0.1'] output is 127.0.0.1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'https=//exceljet.net/catalog'
# Output: exceljet.net/catalog

def extract_domain(input_str):
    try:
        parts = input_str.split('=//')
        domain = parts[1]
        return domain
    except IndexError:
        return "Invalid input format"

# Test cases
print(extract_domain('https=//exceljet.net/catalog'))
print(extract_domain('https=//microsoft.com'))
print(extract_domain('ftp=//someserver.com'))
print(extract_domain('sftp=//127.0.0.1'))

# End time: 2024-03-30 21:49:09.143672
# Elapsed time in seconds: 3.6381773880002584
# Start time: 2024-03-30 20:59:55.804454

# Content: Given that given input as ['https=//exceljet.net/catalog'] output is exceljet.net/catalog, given input as ['https=//microsoft.com'] output is microsoft.com, given input as ['ftp=//someserver.com'] output is someserver.com, given input as ['sftp=//127.0.0.1'] output is 127.0.0.1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: 'https=//exceljet.net/catalog'
# Output: exceljet.net/catalog
# Input: 'https=//microsoft.com'
# Output: microsoft.com
# Input: 'ftp=//someserver.com'
# Output: someserver.com
# Input: 'sftp=//127.0.0.1'
# Output: 127.0.0.1

def extract_domain(input_str):
    try:
        # Split the input string by '=' and '//'
        parts = input_str.split('=//')
        
        # Extract the domain from the second part
        domain = parts[1]
        
        return domain
    except:
        return "Invalid input"

# Test the function with the provided test cases
print(extract_domain('https=//exceljet.net/catalog'))
print(extract_domain('https=//microsoft.com'))
print(extract_domain('ftp=//someserver.com'))
print(extract_domain('sftp=//127.0.0.1'))

# End time: 2024-03-30 21:00:02.086833
# Elapsed time in seconds: 6.2822281240005395
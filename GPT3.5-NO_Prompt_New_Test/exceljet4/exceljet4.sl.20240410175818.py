# Start time: 2024-04-10 18:02:13.254776

'''
Prompt:
Given that input as ['https=//exceljet.net/catalog'] output is exceljet.net/catalog, input as ['https=//microsoft.com'] output is microsoft.com, input as ['ftp=//someserver.com'] output is someserver.com, input as ['sftp=//127.0.0.1'] output is 127.0.0.1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        url = input_str.split('=//')[1]
        return url
    except IndexError:
        return "Invalid input format"

# Test cases
print(generated_function('https=//exceljet.net/catalog'))
print(generated_function('https=//microsoft.com'))
print(generated_function('ftp=//someserver.com'))
print(generated_function('sftp=//127.0.0.1'))
print(generated_function("https=//exceljet.net/catalog"))  ## Output: exceljet.net/catalog
print(generated_function("https=//microsoft.com"))  ## Output: microsoft.com
print(generated_function("ftp=//someserver.com"))  ## Output: someserver.com
print(generated_function("sftp=//127.0.0.1"))  ## Output: 127.0.0.1

# End time: 2024-04-10 18:02:14.897802
# Elapsed time in seconds: 1.642972846000248


# APPEND TEST SCRIPTS...
print(generated_function("https=//exceljet.net/catalog"))  ## Output: exceljet.net/catalog
print(generated_function("https=//microsoft.com"))  ## Output: microsoft.com
print(generated_function("ftp=//someserver.com"))  ## Output: someserver.com
print(generated_function("sftp=//127.0.0.1"))  ## Output: 127.0.0.1


print(generated_function("http=//localhost:2763/mywebsite"))  ### Output: localhost:2763/mywebsite
print(generated_function("https=//amazon.com"))  ### Output: amazon.com
print(generated_function("https=//exceljet.net/index.html"))  ### Output: exceljet.net/index.html
print(generated_function("ftp=//myserver.io"))  ### Output: myserver.io
print(generated_function("sftp=//127.0.0.1:12345/something"))  ### Output: 127.0.0.1:12345/something
print(generated_function("https=//localhost:2763/mywebsite/blog"))  ### Output: localhost:2763/mywebsite/blog

# TEST SCRIPTS APPENDED!


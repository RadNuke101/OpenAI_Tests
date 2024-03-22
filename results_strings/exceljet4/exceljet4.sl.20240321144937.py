# Prompt: return everything after the "//" in the inputted expression
# Input: ['https=//exceljet.net/catalog']
# Output: exceljet.net/catalog

def get_after_double_slash(input_str):
    return input_str.split("//")[1]

# Test cases
print(get_after_double_slash('https=//exceljet.net/catalog'))  # Output: exceljet.net/catalog
print(get_after_double_slash('https=//microsoft.com'))  # Output: microsoft.com
print(get_after_double_slash('ftp=//someserver.com'))  # Output: someserver.com
print(get_after_double_slash('sftp=//127.0.0.1'))  # Output: 127.0.0.1
exceljet.net/catalog
microsoft.com
someserver.com
127.0.0.1

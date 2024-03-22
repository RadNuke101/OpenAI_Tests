# Prompt: return everything after the "//" in the inputted expression
# Input: ['https=//exceljet.net/catalog']
# Output: exceljet.net/catalog

def extract_domain(input_str):
    return input_str.split("//")[1]

# Test cases
print(extract_domain('https=//exceljet.net/catalog'))  # Output: exceljet.net/catalog
print(extract_domain('https=//microsoft.com'))  # Output: microsoft.com
print(extract_domain('ftp=//someserver.com'))  # Output: someserver.com
print(extract_domain('sftp=//127.0.0.1'))  # Output: 127.0.0.1
exceljet.net/catalog
microsoft.com
someserver.com
127.0.0.1

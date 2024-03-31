# Start time: 2024-03-30 23:24:33.632890

# Content: Given that given input as ['Name= ABC Retailers'] output is ABC Retailers, given input as [' ame= XYZ Suppliers'] output is XYZ Suppliers, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_name(input_str):
    try:
        # Input: 'Name= ABC Retailers'
        # Output: 'ABC Retailers'
        
        # Removing any leading or trailing whitespaces
        input_str = input_str.strip()
        
        # Splitting the input string at '=' and taking the second part
        name = input_str.split('=')[1].strip()
        
        return name
    except (IndexError, AttributeError) as e:
        print("Invalid input format. Please provide input in the format 'Name= Company Name'")
        return None

# Test cases
print(extract_name('Name= ABC Retailers'))
print(extract_name(' ame= XYZ Suppliers'))
print(extract_name('Name=DEF Distributors'))
print(extract_name('Name= GHI Wholesalers'))
print(extract_name('Name=JKL Manufacturers'))

# End time: 2024-03-30 23:24:35.248069
# Elapsed time in seconds: 1.615125258002081
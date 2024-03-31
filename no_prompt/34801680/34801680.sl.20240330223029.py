# Start time: 2024-03-30 22:36:34.438348

# Content: Given that given input as ['Name= ABC Retailers'] output is ABC Retailers, given input as [' ame= XYZ Suppliers'] output is XYZ Suppliers, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_name(input_str):
    try:
        # Input: 'Name= ABC Retailers'
        # Output: 'ABC Retailers'
        
        # Split the input string at '=' and get the second part
        name = input_str.split('=')[1].strip()
        
        return name
    except (IndexError, AttributeError):
        return "Invalid input format"

# Test cases
print(extract_name('Name= ABC Retailers'))  # Output: ABC Retailers
print(extract_name(' ame= XYZ Suppliers'))  # Output: XYZ Suppliers
print(extract_name('Invalid input'))  # Output: Invalid input format

# End time: 2024-03-30 22:36:36.819763
# Elapsed time in seconds: 2.3813581520007574
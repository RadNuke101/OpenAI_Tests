# Start time: 2024-03-30 19:54:50.765374

# Content: Given that given input as ['Name= ABC Retailers'] output is ABC Retailers, given input as [' ame= XYZ Suppliers'] output is XYZ Suppliers, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_name(input_str):
    try:
        # Input: 'Name= ABC Retailers'
        # Output: 'ABC Retailers'
        
        # Handling input exceptions
        if not input_str.startswith('Name= '):
            raise ValueError("Input format is incorrect")
        
        return input_str.split('= ')[1]
    
    except Exception as e:
        print("Error:", e)

# Test cases
print(extract_name('Name= ABC Retailers'))  # Output: ABC Retailers
print(extract_name(' ame= XYZ Suppliers'))  # Error: Input format is incorrect

# End time: 2024-03-30 19:54:52.480384
# Elapsed time in seconds: 1.7149697120003111
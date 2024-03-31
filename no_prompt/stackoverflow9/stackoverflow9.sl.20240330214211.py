# Start time: 2024-03-30 21:55:06.569955

# Content: Given that given input as ['Sarah Jane Jones'] output is Jones, given input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_last_name(full_name):
    try:
        # Input: 'Sarah Jane Jones'
        # Output: 'Jones'
        
        # Input: 'Bob Jane Smithfield'
        # Output: 'Smithfield'
        
        # Split the full name into parts
        parts = full_name.split()
        
        # Return the last part of the full name
        return parts[-1]
    
    except Exception as e:
        print("Error: ", e)

# Test cases
print(extract_last_name('Sarah Jane Jones'))
print(extract_last_name('Bob Jane Smithfield'))

# End time: 2024-03-30 21:55:07.571631
# Elapsed time in seconds: 1.001646143000471
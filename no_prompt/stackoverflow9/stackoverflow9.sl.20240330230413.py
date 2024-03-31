# Start time: 2024-03-30 23:17:40.814820

# Content: Given that given input as ['Sarah Jane Jones'] output is Jones, given input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Sarah Jane Jones'
# Output: 'Jones'

# Input: 'Bob Jane Smithfield'
# Output: 'Smithfield'

def get_last_name(full_name):
    try:
        # Split the full name into parts
        parts = full_name.split()
        
        # Return the last part which represents the last name
        return parts[-1]
    
    except Exception as e:
        print("Error: ", e)
        return None

# Test cases
print(get_last_name('Sarah Jane Jones'))  # Output: Jones
print(get_last_name('Bob Jane Smithfield'))  # Output: Smithfield

# End time: 2024-03-30 23:17:43.789696
# Elapsed time in seconds: 2.974797088998457
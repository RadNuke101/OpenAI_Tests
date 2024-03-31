# Start time: 2024-03-30 22:10:49.680899

# Content: Given that given input as ['Sarah Jane Jones'] output is Jones, given input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_last_name(full_name):
    try:
        # Input: 'Sarah Jane Jones'
        # Output: 'Jones'
        
        # Input: 'Bob Jane Smithfield'
        # Output: 'Smithfield'
        
        # Extract last name by splitting the full name and returning the last element
        return full_name.split()[-1]
    
    except Exception as e:
        print("Error: ", e)

# Test cases
print(get_last_name('Sarah Jane Jones'))  # Output should be 'Jones'
print(get_last_name('Bob Jane Smithfield'))  # Output should be 'Smithfield'

# End time: 2024-03-30 22:10:54.512310
# Elapsed time in seconds: 4.83126699100103
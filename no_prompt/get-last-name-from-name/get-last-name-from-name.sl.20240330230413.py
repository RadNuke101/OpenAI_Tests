# Start time: 2024-03-30 23:18:10.903111

# Content: Given that given input as ['Park Kim'] output is Kim, given input as ['Lee Kim'] output is Kim, given input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: 'Park Kim', Output: 'Kim'
# Input: 'Lee Kim', Output: 'Kim'
# Input: 'Kim Lee', Output: 'Lee'

def get_last_name(full_name):
    try:
        # Split the full name into parts
        parts = full_name.split()
        
        # Return the last part as the last name
        return parts[-1]
    except Exception as e:
        print(f"An error occurred: {e}")

# Test the function with the provided test cases
print(get_last_name('Park Kim'))
print(get_last_name('Lee Kim'))
print(get_last_name('Kim Lee'))

# End time: 2024-03-30 23:18:12.865043
# Elapsed time in seconds: 1.961880951999774
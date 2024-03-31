# Start time: 2024-03-30 18:20:48.290036

# Content: Given that given input as ['Susan Ann Chang'] output is Susan, given input as ['Ayako Tanaka'] output is Ayako, given input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Susan Ann Chang'
# Output: Susan

# Input: 'Ayako Tanaka'
# Output: Ayako

# Input: 'Bobby T. smth'
# Output: Bobby

def get_first_name(full_name):
    try:
        # Split the full name by space
        name_parts = full_name.split()
        
        # Return the first part of the name
        return name_parts[0]
    except (IndexError, AttributeError):
        return "Invalid input"

# Test cases
print(get_first_name('Susan Ann Chang'))
print(get_first_name('Ayako Tanaka'))
print(get_first_name('Bobby T. smth'))

# End time: 2024-03-30 18:20:50.209331
# Elapsed time in seconds: 1.919247141000028
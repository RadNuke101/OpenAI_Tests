# Start time: 2024-03-30 23:23:21.014903

# Content: Given that given input as ['Nancy FreeHafer'] output is Nancy, given input as ['Andrew Cencici'] output is Andrew, given input as ['Jan Kotas'] output is Jan, given input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Nancy FreeHafer'
# Output: Nancy

def get_first_name(full_name):
    try:
        # Split the full name by space
        parts = full_name.split()
        
        # Return the first part as the first name
        return parts[0]
    except Exception as e:
        print("Error: ", e)
        return None

# Test cases
print(get_first_name('Nancy FreeHafer'))  # Output: Nancy
print(get_first_name('Andrew Cencici'))    # Output: Andrew
print(get_first_name('Jan Kotas'))         # Output: Jan
print(get_first_name('Mariya Sergienko'))  # Output: Mariya

# End time: 2024-03-30 23:23:24.384300
# Elapsed time in seconds: 3.3690918879983656
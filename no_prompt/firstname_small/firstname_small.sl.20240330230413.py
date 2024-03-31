# Start time: 2024-03-30 23:11:50.404712

# Content: Given that given input as ['Nancy FreeHafer'] output is Nancy, given input as ['Andrew Cencici'] output is Andrew, given input as ['Jan Kotas'] output is Jan, given input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_first_name(full_name):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Nancy'
        
        # Input: 'Andrew Cencici'
        # Output: 'Andrew'
        
        # Input: 'Jan Kotas'
        # Output: 'Jan'
        
        # Input: 'Mariya Sergienko'
        # Output: 'Mariya'
        
        return full_name.split()[0]
    
    except Exception as e:
        print("Error: ", e)

# Test cases
print(get_first_name('Nancy FreeHafer'))
print(get_first_name('Andrew Cencici'))
print(get_first_name('Jan Kotas'))
print(get_first_name('Mariya Sergienko'))

# End time: 2024-03-30 23:11:52.046497
# Elapsed time in seconds: 1.6417330660005973
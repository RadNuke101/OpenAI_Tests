# Start time: 2024-03-30 18:21:38.530454

# Content: Given that given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Dr. Nancy'
        
        # Input: 'Andrew Cencici'
        # Output: 'Dr. Andrew'
        
        # Input: 'Jan Kotas'
        # Output: 'Dr. Jan'
        
        # Input: 'Mariya Sergienko'
        # Output: 'Dr. Mariya'
        
        parts = name.split()
        if len(parts) < 2:
            raise ValueError("Input must contain at least two names")
        
        return "Dr. " + parts[0]
    
    except Exception as e:
        print("Error:", e)

# Test cases
print(format_name('Nancy FreeHafer'))
print(format_name('Andrew Cencici'))
print(format_name('Jan Kotas'))
print(format_name('Mariya Sergienko'))

# End time: 2024-03-30 18:21:40.930238
# Elapsed time in seconds: 2.3997301889999676
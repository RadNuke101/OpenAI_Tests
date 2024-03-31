# Start time: 2024-03-30 22:11:14.320981

# Content: Given that given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_str):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Nancy F.'
        
        # Input: 'Andrew Cencici'
        # Output: 'Andrew C.'
        
        # Input: 'Jan Kotas'
        # Output: 'Jan K.'
        
        # Input: 'Mariya Sergienko'
        # Output: 'Mariya S.'
        
        parts = input_str.split()
        first_name = parts[0]
        last_name = parts[1][0] + '.'
        
        return first_name + ' ' + last_name
    except IndexError:
        return "Invalid input format. Please provide both first name and last name separated by a space."

# Test cases
print(format_name('Nancy FreeHafer'))  # Output: Nancy F.
print(format_name('Andrew Cencici'))   # Output: Andrew C.
print(format_name('Jan Kotas'))        # Output: Jan K.
print(format_name('Mariya Sergienko')) # Output: Mariya S.

# End time: 2024-03-30 22:11:16.104962
# Elapsed time in seconds: 1.7839385720017162
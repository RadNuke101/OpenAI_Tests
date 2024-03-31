# Start time: 2024-03-30 18:35:29.268668

# Content: Given that given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        # Input: 'Nancy FreeHafer', Output: 'N.F.'
        # Input: 'Andrew Cencici', Output: 'A.C.'
        # Input: 'Jan Kotas', Output: 'J.K.'
        # Input: 'Mariya Sergienko', Output: 'M.S.'
        
        parts = name.split()
        formatted_name = parts[0][0].upper() + '.' + parts[1][0].upper() + '.'
        return formatted_name
    except Exception as e:
        print("Error:", e)

# Test cases
print(format_name('Nancy FreeHafer'))  # Output: N.F.
print(format_name('Andrew Cencici'))   # Output: A.C.
print(format_name('Jan Kotas'))        # Output: J.K.
print(format_name('Mariya Sergienko')) # Output: M.S.

# End time: 2024-03-30 18:35:31.769398
# Elapsed time in seconds: 2.5006599230000006
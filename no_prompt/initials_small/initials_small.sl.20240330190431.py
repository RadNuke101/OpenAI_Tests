# Start time: 2024-03-30 19:12:44.152906

# Content: Given that given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Nancy FreeHafer'
# Output: 'N.F.'

def format_name(name):
    try:
        # Split the name into first and last name
        parts = name.split()
        first_name = parts[0]
        last_name = parts[1]

        # Get the initials
        initials = first_name[0].upper() + '.' + last_name[0].upper() + '.'

        return initials
    except IndexError:
        print("Error: Please provide both first and last name.")
    except:
        print("Error: An unknown error occurred.")

# Test cases
print(format_name('Nancy FreeHafer'))  # Output: N.F.
print(format_name('Andrew Cencici'))    # Output: A.C.
print(format_name('Jan Kotas'))         # Output: J.K.
print(format_name('Mariya Sergienko'))  # Output: M.S.

# End time: 2024-03-30 19:12:47.633122
# Elapsed time in seconds: 3.4801117899996825
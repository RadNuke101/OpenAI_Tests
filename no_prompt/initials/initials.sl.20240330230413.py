# Start time: 2024-03-30 23:08:13.409121

# Content: Given that given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        # Input: 'Nancy FreeHafer'  Output: 'N.F.'
        # Input: 'Andrew Cencici'  Output: 'A.C.'
        # Input: 'Jan Kotas'  Output: 'J.K.'
        # Input: 'Mariya Sergienko'  Output: 'M.S.'
        
        # Split the name into first name and last name
        parts = name.split()
        first_name = parts[0]
        last_name = parts[1]

        # Get the first letter of the first name and last name, and format them
        formatted_name = f"{first_name[0]}.{last_name[0]}."

        return formatted_name
    except (IndexError, TypeError):
        print("Invalid input format. Please provide a full name with a space separating the first and last name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(format_name('Nancy FreeHafer'))  # Output: N.F.
print(format_name('Andrew Cencici'))   # Output: A.C.
print(format_name('Jan Kotas'))        # Output: J.K.
print(format_name('Mariya Sergienko')) # Output: M.S.

# End time: 2024-03-30 23:08:16.893322
# Elapsed time in seconds: 3.4841203289979603
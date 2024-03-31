# Start time: 2024-03-30 19:58:34.254790

# Content: Given that given input as ['Nancy FreeHafer'] output is N.F., given input as ['Andrew Cencici'] output is A.C., given input as ['Jan Kotas'] output is J.K., given input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Nancy FreeHafer'
# Output: 'N.F.'

def generate_initials(name):
    try:
        # Split the name into first name and last name
        first_name, last_name = name.split()

        # Get the first letter of the first name and last name
        initials = first_name[0].upper() + '.' + last_name[0].upper() + '.'

        return initials
    except ValueError:
        print("Please enter a first name and last name separated by a space.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(generate_initials('Nancy FreeHafer'))  # Output: 'N.F.'
print(generate_initials('Andrew Cencici'))   # Output: 'A.C.'
print(generate_initials('Jan Kotas'))        # Output: 'J.K.'
print(generate_initials('Mariya Sergienko')) # Output: 'M.S.'

# End time: 2024-03-30 19:58:36.783043
# Elapsed time in seconds: 2.528221157000189
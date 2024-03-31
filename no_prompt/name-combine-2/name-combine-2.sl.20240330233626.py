# Start time: 2024-03-30 23:47:43.429202

# Content: Given that given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Nancy FreeHafer'
# Output: 'Nancy F.'
# Input: 'Andrew Cencici'
# Output: 'Andrew C.'
# Input: 'Jan Kotas'
# Output: 'Jan K.'
# Input: 'Mariya Sergienko'
# Output: 'Mariya S.'

def format_name(input_str):
    try:
        # Split the input string into first name and last name
        names = input_str.split()
        first_name = names[0]
        last_name = names[1]

        # Get the first letter of the last name
        last_initial = last_name[0]

        # Format the output
        output = f"{first_name} {last_initial}."

        return output
    except IndexError:
        print("Error: Please provide both first name and last name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(format_name('Nancy FreeHafer'))
print(format_name('Andrew Cencici'))
print(format_name('Jan Kotas'))
print(format_name('Mariya Sergienko'))

# End time: 2024-03-30 23:47:45.722263
# Elapsed time in seconds: 2.293021581001085
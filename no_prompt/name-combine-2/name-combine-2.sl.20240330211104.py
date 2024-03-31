# Start time: 2024-03-30 21:22:59.713463

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
        first_name, last_name = input_str.split()
        
        # Get the first letter of the last name
        last_initial = last_name[0]
        
        # Format the output
        output = f"{first_name} {last_initial}."
        
        return output
    except ValueError:
        print("Please provide both first name and last name separated by a space.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(format_name('Nancy FreeHafer'))
print(format_name('Andrew Cencici'))
print(format_name('Jan Kotas'))
print(format_name('Mariya Sergienko'))

# End time: 2024-03-30 21:23:02.051460
# Elapsed time in seconds: 2.3376703489993815
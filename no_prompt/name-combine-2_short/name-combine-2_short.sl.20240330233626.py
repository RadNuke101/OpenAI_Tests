# Start time: 2024-03-30 23:48:50.234851

# Content: Given that given input as ['Nancy', 'FreeHafer'] output is Nancy F., given input as ['Andrew', 'Cencici'] output is Andrew C., given input as ['Jan', 'Kotas'] output is Jan K., given input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        first_name, last_name = name.split()
        return f"{first_name} {last_name[0]}."
    except ValueError:
        return "Invalid input format. Please provide first and last name separated by a space."

# Test cases
# print(format_name('Nancy FreeHafer'))  # Output: Nancy F.
# print(format_name('Andrew Cencici'))    # Output: Andrew C.
# print(format_name('Jan Kotas'))         # Output: Jan K.
# print(format_name('Mariya Sergienko'))  # Output: Mariya S.

# End time: 2024-03-30 23:48:52.151862
# Elapsed time in seconds: 1.916979308000009
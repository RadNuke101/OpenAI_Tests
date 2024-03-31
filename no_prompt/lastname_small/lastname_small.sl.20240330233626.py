# Start time: 2024-03-30 23:40:25.722133

# Content: Given that given input as ['Nancy FreeHafer'] output is FreeHafer, given input as ['Andrew Cencici'] output is Cencici, given input as ['Jan Kotas'] output is Kotas, given input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'Nancy FreeHafer', output: 'FreeHafer'
# input: 'Andrew Cencici', output: 'Cencici'
# input: 'Jan Kotas', output: 'Kotas'
# input: 'Mariya Sergienko', output: 'Sergienko'

def get_last_name(full_name):
    try:
        # Split the full name by space and get the last element
        last_name = full_name.split()[-1]
        return last_name
    except:
        return "Invalid input"

# Test cases
print(get_last_name('Nancy FreeHafer'))
print(get_last_name('Andrew Cencici'))
print(get_last_name('Jan Kotas'))
print(get_last_name('Mariya Sergienko'))

# End time: 2024-03-30 23:40:27.555518
# Elapsed time in seconds: 1.833358653999312
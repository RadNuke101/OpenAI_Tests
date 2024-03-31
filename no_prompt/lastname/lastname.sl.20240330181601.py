# Start time: 2024-03-30 18:24:09.770472

# Content: Given that given input as ['Nancy FreeHafer'] output is FreeHafer, given input as ['Andrew Cencici'] output is Cencici, given input as ['Jan Kotas'] output is Kotas, given input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Nancy FreeHafer'
# Output: 'FreeHafer'

def get_last_name(full_name):
    try:
        # Split the full name into first name and last name
        names = full_name.split()
        last_name = names[-1]
        return last_name
    except Exception as e:
        print("Error: ", e)

# Test cases
print(get_last_name('Nancy FreeHafer'))  # Output: FreeHafer
print(get_last_name('Andrew Cencici'))   # Output: Cencici
print(get_last_name('Jan Kotas'))         # Output: Kotas
print(get_last_name('Mariya Sergienko'))  # Output: Sergienko

# End time: 2024-03-30 18:24:11.461705
# Elapsed time in seconds: 1.6911947489999761
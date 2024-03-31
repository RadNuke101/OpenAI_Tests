# Start time: 2024-03-30 23:11:07.159210

# Content: Given that given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Nancy FreeHafer'
# Output: Dr. Nancy

def format_name(input_str):
    try:
        # Split the input string into first and last name
        names = input_str.split()
        first_name = names[0]
        
        # Check if the first name starts with 'Dr.'
        if first_name == 'Dr.':
            return input_str
        else:
            return 'Dr. ' + first_name
    except Exception as e:
        return 'Invalid input'

# Test cases
print(format_name('Nancy FreeHafer'))  # Output: Dr. Nancy
print(format_name('Andrew Cencici'))    # Output: Dr. Andrew
print(format_name('Jan Kotas'))         # Output: Dr. Jan
print(format_name('Mariya Sergienko'))  # Output: Dr. Mariya

# End time: 2024-03-30 23:11:09.534745
# Elapsed time in seconds: 2.3754758150025737
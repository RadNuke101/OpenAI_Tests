# Start time: 2024-03-30 19:41:21.005494

# Content: Given that given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_name):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Dr. Nancy'
        
        # Split the input name into first and last name
        name_parts = input_name.split()
        first_name = name_parts[0]
        
        # Check if the first name starts with 'Dr.'
        if first_name == 'Dr.':
            return input_name
        else:
            return 'Dr. ' + first_name
    except Exception as e:
        return 'Invalid input'

# Test cases
print(format_name('Nancy FreeHafer'))
print(format_name('Andrew Cencici'))
print(format_name('Jan Kotas'))
print(format_name('Mariya Sergienko'))

# End time: 2024-03-30 19:41:24.295909
# Elapsed time in seconds: 3.2903791159997127
# Start time: 2024-03-30 23:42:38.028203

# Content: Given that given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_name):
    try:
        # Input: 'Nancy FreeHafer'
        # Output: 'Dr. Nancy'
        name_parts = input_name.split()
        title = 'Dr.'
        first_name = name_parts[0]
        formatted_name = f'{title} {first_name}'
        return formatted_name
    except (IndexError, AttributeError) as e:
        print(f"Error: {e}")
        return None

# Test cases
print(format_name('Nancy FreeHafer'))  # Output: Dr. Nancy
print(format_name('Andrew Cencici'))    # Output: Dr. Andrew
print(format_name('Jan Kotas'))         # Output: Dr. Jan
print(format_name('Mariya Sergienko'))  # Output: Dr. Mariya

# End time: 2024-03-30 23:42:41.183874
# Elapsed time in seconds: 3.155550076000509
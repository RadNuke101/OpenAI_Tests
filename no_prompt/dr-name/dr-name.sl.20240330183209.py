# Start time: 2024-03-30 18:38:20.469809

# Content: Given that given input as ['Nancy FreeHafer'] output is Dr. Nancy, given input as ['Andrew Cencici'] output is Dr. Andrew, given input as ['Jan Kotas'] output is Dr. Jan, given input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(input_name):
    try:
        name = input_name.split()
        if len(name) != 2:
            raise ValueError("Input must contain first and last name only")
        
        title = "Dr. " + name[0]
        return title
    except ValueError as ve:
        return str(ve)

# Test cases
"""
Input: 'Nancy FreeHafer'
Output: 'Dr. Nancy'

Input: 'Andrew Cencici'
Output: 'Dr. Andrew'

Input: 'Jan Kotas'
Output: 'Dr. Jan'

Input: 'Mariya Sergienko'
Output: 'Dr. Mariya'
"""

# End time: 2024-03-30 18:38:23.149664
# Elapsed time in seconds: 2.6797792709999726
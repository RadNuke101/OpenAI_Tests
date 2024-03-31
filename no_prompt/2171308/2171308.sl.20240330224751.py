# Start time: 2024-03-30 22:55:03.277099

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'John Doe'
# Output: 'J Doe'

def format_name(name):
    try:
        first_name, last_name = name.split()
        formatted_name = first_name[0] + ' ' + last_name
        return formatted_name
    except ValueError:
        print("Please provide a full name with a space separating the first and last name.")

# Test cases
print(format_name('John Doe'))
print(format_name('Mayur Naik'))
print(format_name('Nimit Singh'))

# End time: 2024-03-30 22:55:05.378325
# Elapsed time in seconds: 2.1011755050003558
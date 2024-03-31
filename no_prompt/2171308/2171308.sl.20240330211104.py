# Start time: 2024-03-30 21:17:39.404952

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_shortened_name(full_name):
    try:
        # Input: 'John Doe'
        # Output: 'J Doe'
        
        # Input: 'Mayur Naik'
        # Output: 'M Naik'
        
        # Input: 'Nimit Singh'
        # Output: 'N Singh'
        
        first_name, last_name = full_name.split()
        shortened_name = first_name[0] + ' ' + last_name
        return shortened_name
    except (ValueError, IndexError):
        print("Invalid input format. Please provide a full name with a space in between.")
        return None

# Test cases
print(get_shortened_name('John Doe'))
print(get_shortened_name('Mayur Naik'))
print(get_shortened_name('Nimit Singh'))

# End time: 2024-03-30 21:17:43.155651
# Elapsed time in seconds: 3.7506099629990786
# Start time: 2024-03-30 19:41:32.654503

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
    except ValueError:
        print("Invalid input format. Please provide a full name with a space separating the first and last name.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(get_shortened_name('John Doe'))
print(get_shortened_name('Mayur Naik'))
print(get_shortened_name('Nimit Singh'))

# End time: 2024-03-30 19:41:35.636935
# Elapsed time in seconds: 2.9824000409998916
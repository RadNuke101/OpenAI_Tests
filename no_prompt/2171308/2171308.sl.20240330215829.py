# Start time: 2024-03-30 22:04:42.059270

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'John Doe'
# Output: 'J Doe'

def generate_short_name(full_name):
    try:
        first_name, last_name = full_name.split()
        short_name = first_name[0] + ' ' + last_name
        return short_name
    except ValueError:
        print("Please provide a full name with a space separating the first and last name.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(generate_short_name('John Doe'))  # Output: J Doe
print(generate_short_name('Mayur Naik'))  # Output: M Naik
print(generate_short_name('Nimit Singh'))  # Output: N Singh

# End time: 2024-03-30 22:04:44.954271
# Elapsed time in seconds: 2.8949170880005113
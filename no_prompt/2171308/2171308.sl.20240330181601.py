# Start time: 2024-03-30 18:21:54.322207

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        first_name, last_name = name.split()
        formatted_name = f"{first_name[0]} {last_name}"
        return formatted_name
    except ValueError:
        print("Input should contain first name and last name separated by a space.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
# Input: 'John Doe'
# Output: 'J Doe'
print(format_name('John Doe'))

# Input: 'Mayur Naik'
# Output: 'M Naik'
print(format_name('Mayur Naik'))

# Input: 'Nimit Singh'
# Output: 'N Singh'
print(format_name('Nimit Singh'))

# End time: 2024-03-30 18:21:56.359438
# Elapsed time in seconds: 2.0371830760000194
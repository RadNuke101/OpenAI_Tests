# Start time: 2024-03-30 23:26:46.421946

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'John Doe'
# Output: 'J Doe'

def format_name(name):
    try:
        first_name, last_name = name.split()
        formatted_name = f"{first_name[0]} {last_name}"
        return formatted_name
    except ValueError:
        print("Please enter a valid full name with a space in between the first and last name.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(format_name('John Doe'))
print(format_name('Mayur Naik'))
print(format_name('Nimit Singh'))

# End time: 2024-03-30 23:26:48.070344
# Elapsed time in seconds: 1.6483503989984456
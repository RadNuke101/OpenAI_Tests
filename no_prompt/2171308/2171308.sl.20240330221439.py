# Start time: 2024-03-30 22:20:31.465390

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'John Doe'
# Output: 'J Doe'

def get_short_name(full_name):
    try:
        names = full_name.split()
        if len(names) < 2:
            raise ValueError("Full name must contain at least two parts")
        
        first_initial = names[0][0]
        last_name = names[-1]
        
        return f"{first_initial} {last_name}"
    
    except ValueError as ve:
        print(f"Error: {ve}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(get_short_name('John Doe'))  # Output: J Doe
print(get_short_name('Mayur Naik'))  # Output: M Naik
print(get_short_name('Nimit Singh'))  # Output: N Singh

# End time: 2024-03-30 22:20:33.088164
# Elapsed time in seconds: 1.622729167000216
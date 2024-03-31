# Start time: 2024-03-30 20:13:19.069169

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_short_name(full_name):
    try:
        # Input: 'John Doe'
        # Output: 'J Doe'
        
        # Input: 'Mayur Naik'
        # Output: 'M Naik'
        
        # Input: 'Nimit Singh'
        # Output: 'N Singh'
        
        names = full_name.split()
        if len(names) < 2:
            raise ValueError("Full name must contain at least two parts separated by a space")
        
        first_initial = names[0][0]
        last_name = names[-1]
        
        return f"{first_initial} {last_name}"
    
    except Exception as e:
        return f"Error: {e}"

# Test cases
print(get_short_name('John Doe'))
print(get_short_name('Mayur Naik'))
print(get_short_name('Nimit Singh'))

# End time: 2024-03-30 20:13:22.418695
# Elapsed time in seconds: 3.3494818720000694
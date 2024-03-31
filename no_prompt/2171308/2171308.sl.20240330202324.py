# Start time: 2024-03-30 20:30:30.931680

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_name(name):
    try:
        # Input: 'John Doe'
        # Output: 'J Doe'
        
        # Input: 'Mayur Naik'
        # Output: 'M Naik'
        
        # Input: 'Nimit Singh'
        # Output: 'N Singh'
        
        parts = name.split()
        if len(parts) < 2:
            raise ValueError("Input must contain at least two parts separated by a space")
        
        first_initial = parts[0][0]
        last_name = parts[-1]
        
        return f"{first_initial} {last_name}"
    
    except Exception as e:
        print(f"Error: {e}")

# Test cases
print(format_name('John Doe'))
print(format_name('Mayur Naik'))
print(format_name('Nimit Singh'))

# End time: 2024-03-30 20:30:33.124995
# Elapsed time in seconds: 2.193255885000326
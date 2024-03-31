# Start time: 2024-03-30 19:11:15.048379

# Content: Given that given input as ['John Doe'] output is J Doe, given input as ['Mayur Naik'] output is M Naik, given input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'John Doe'
# Output: 'J Doe'

def generate_output(input_str):
    try:
        # Split the input string by space
        parts = input_str.split()
        
        # Get the first character of the first part and capitalize it
        first_initial = parts[0][0].upper()
        
        # Get the last name from the second part
        last_name = parts[1]
        
        # Concatenate the first initial and last name
        output_str = first_initial + ' ' + last_name
        
        return output_str
    except Exception as e:
        print("Error: Invalid input format")
        return None

# Test cases
print(generate_output('John Doe'))
print(generate_output('Mayur Naik'))
print(generate_output('Nimit Singh'))

# End time: 2024-03-30 19:11:17.130486
# Elapsed time in seconds: 2.082044200999917
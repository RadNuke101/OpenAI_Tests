# Start time: 2024-04-10 14:56:51.649408

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:
- The input column data consists of full names in the format of 'First Name Last Name'.

Summary for output column data:
- The output column data consists of initials of the first name followed by the last name.

Relationship between input and output:
- The relationship between the input and output is that the output column takes the first initial of the first name and combines it with the last name. This creates a shortened version of the full name that still retains some identifying information., and input as ['John Doe'] output is J Doe, input as ['Mayur Naik'] output is M Naik, input as ['Nimit Singh'] output is N Singh, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into first name and last name
    first_name, last_name = input_str.split()
    
    # Get the first initial of the first name
    first_initial = first_name[0]
    
    # Combine the first initial with the last name
    output_str = first_initial + ' ' + last_name
    
    return output_str

# Test cases
print(generated_function('John Doe'))
print(generated_function('Mayur Naik'))
print(generated_function('Nimit Singh'))
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh

# End time: 2024-04-10 14:56:53.395935
# Elapsed time in seconds: 1.7464753900001142


# APPEND TEST SCRIPTS...
print(generated_function("John Doe"))  ## Output: J Doe
print(generated_function("Mayur Naik"))  ## Output: M Naik
print(generated_function("Nimit Singh"))  ## Output: N Singh


print(generated_function("John Singh"))  ### Output: J Singh
print(generated_function("Mayur Doe"))  ### Output: M Doe
print(generated_function("Nimit Naik"))  ### Output: N Naik

# TEST SCRIPTS APPENDED!


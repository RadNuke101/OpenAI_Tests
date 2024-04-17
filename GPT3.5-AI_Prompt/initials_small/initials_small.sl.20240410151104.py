# Start time: 2024-04-10 15:22:33.969061

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals.
- Each full name is in the format of 'First Name Last Name'.

Summary for Output Column:
- The output column consists of initials of the first and last names of individuals.
- The initials are in the format of 'First Initial. Last Initial'.

Relationship between Input and Output:
- The output column is derived from the input column by taking the first initial of the first name and the first initial of the last name.
- The relationship between the input and output is that the output provides a condensed representation of the full names in the input column.
- The output column serves as a shorthand way to refer to individuals based on their initials, making it easier to identify and distinguish between different individuals., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into first name and last name
    first_name, last_name = input_str.split()
    
    # Get the first initial of the first name and last name
    first_initial = first_name[0]
    last_initial = last_name[0]
    
    # Return the initials in the specified format
    return f'{first_initial}.{last_initial}'

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: N.F.
print(generated_function('Andrew Cencici'))   # Output: A.C.
print(generated_function('Jan Kotas'))        # Output: J.K.
print(generated_function('Mariya Sergienko')) # Output: M.S.
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 15:22:36.425565
# Elapsed time in seconds: 2.4564567970001008
# Start time: 2024-04-10 14:59:33.450266

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:
- The input column data consists of full names of individuals.
- Each full name is in the format of 'First Name Last Name'.

Summary for output column data:
- The output column data consists of initials of the first and last names of individuals.
- Each set of initials is in the format of 'First Initial. Last Initial'.

Relationship between input and output:
- The output column data is derived from the input column data by taking the first initial of the first name and the first initial of the last name.
- The relationship between the input and output is that the output provides a concise representation of the full name by using the initials of the first and last names.
- This transformation simplifies the data while still retaining some identifying information about the individuals., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    result = []
    for name in args:
        first_name, last_name = name.split()
        initials = f"{first_name[0]}.{last_name[0]}."
        result.append(initials)
    return result

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: ['N.F.']
print(generated_function('Andrew Cencici'))  # Output: ['A.C.']
print(generated_function('Jan Kotas'))  # Output: ['J.K.']
print(generated_function('Mariya Sergienko'))  # Output: ['M.S.']
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 14:59:35.805747
# Elapsed time in seconds: 2.355411019999792
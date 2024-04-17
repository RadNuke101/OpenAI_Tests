# Start time: 2024-04-10 14:35:13.596492

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals.
- Each full name is in the format of 'First Name Last Name'.
- The names in the input column data are varied in terms of length and structure.

Summary for Output Column Data:
- The output column data consists of initials derived from the input full names.
- Each set of initials is in the format of 'First Initial. Last Initial'.
- The output column data provides a condensed representation of the input full names.

Relationship between Input and Output:
- The output column data is derived from the input full names by extracting the first letter of the first name and the first letter of the last name.
- The relationship between the input and output is a transformation process where the full names are condensed into initials.
- The output column serves as a simplified version of the input column, allowing for easier reference or identification., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
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

# End time: 2024-04-10 14:35:15.746325
# Elapsed time in seconds: 2.1497839940000176
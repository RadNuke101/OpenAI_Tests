# Start time: 2024-04-10 14:28:17.755506

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:
- The input column data consists of full names of individuals.
- Each name is composed of a first name and a last name.

Summary for output column data:
- The output column data consists of initials representing the first and last names of individuals.
- The initials are separated by a period.

Relationship between input and output:
- The output column data is derived from the input column data by taking the first letter of the first name and the first letter of the last name, and separating them with a period.
- The output provides a concise representation of the full name by using initials.
- This relationship allows for a quick and easy way to identify individuals based on their initials., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        first_name, last_name = name.split()
        initials = f"{first_name[0]}.{last_name[0]}."
        output.append(initials)
    return output

# Test cases
generated_function('Nancy FreeHafer', 'Andrew Cencici', 'Jan Kotas', 'Mariya Sergienko')
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 14:28:18.825593
# Elapsed time in seconds: 1.070071568000003
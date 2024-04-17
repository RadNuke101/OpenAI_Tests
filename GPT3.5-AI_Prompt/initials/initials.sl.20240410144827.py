# Start time: 2024-04-10 14:52:49.325537

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:
- The input column data consists of full names of individuals, with each name containing a first name and a last name.

Summary for output column:
- The output column consists of initials derived from the first and last names provided in the input column.

Relationship between input and output:
- The output column provides a condensed version of the input column data by representing each individual's name with their initials. This relationship allows for a more concise and standardized way of referencing individuals while maintaining their unique identities., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    result = []
    for name in args:
        first_name, last_name = name.split()
        initials = f"{first_name[0]}.{last_name[0]}."
        result.append(initials)
    return result

# Test cases
generated_function('Nancy FreeHafer', 'Andrew Cencici', 'Jan Kotas', 'Mariya Sergienko')
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 14:52:50.838012
# Elapsed time in seconds: 1.5124306230000002
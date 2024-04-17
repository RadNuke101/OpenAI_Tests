# Start time: 2024-04-10 15:00:29.869401

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals.
- Each name appears to have a first name followed by a last name.
- The names vary in length and may include different combinations of letters.

Summary for Output Column Data:
- The output column data consists of last names extracted from the input full names.
- The last names vary in length and may include different combinations of letters.
- The last names are extracted from the input full names based on a specific pattern.

Relationship between Input and Output:
- The output column data is derived from the last names of the input full names.
- The last names in the output column are extracted from the input full names by isolating the second part of the name.
- The relationship between the input and output is that the last name in the output is a subset of the full name in the input, specifically the second part of the full name., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        last_name = name.split()[-1]
        output.append(last_name)
    return output

# Test cases
generated_function('Nancy FreeHafer', 'Andrew Cencici', 'Jan Kotas', 'Mariya Sergienko')
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-10 15:00:30.755957
# Elapsed time in seconds: 0.8865212790001351
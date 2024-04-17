# Start time: 2024-04-10 14:32:14.687192

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of names of individuals, with titles such as 'Dr.' included in some cases.

Summary for Output Column:
- The output column consists of names with the title 'Dr.' added before the first name.

Relationship between Input and Output:
- The relationship between the input and output is that the title 'Dr.' is added before the first name in the output column based on the names provided in the input column. This suggests that the individuals listed in the input column have a professional title of 'Dr.' added to their names in the output column., and input as ['Nancy FreeHafer'] output is Dr. Nancy, input as ['Andrew Cencici'] output is Dr. Andrew, input as ['Jan Kotas'] output is Dr. Jan, input as ['Mariya Sergienko'] output is Dr. Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(name):
    # Split the input name into first and last name
    first_name = name.split()[0]
    # Add 'Dr.' before the first name
    output = 'Dr. ' + first_name
    return output

# Test cases
print(generated_function('Nancy FreeHafer'))
print(generated_function('Andrew Cencici'))
print(generated_function('Jan Kotas'))
print(generated_function('Mariya Sergienko'))
print(generated_function("Nancy FreeHafer"))  ## Output: Dr. Nancy
print(generated_function("Andrew Cencici"))  ## Output: Dr. Andrew
print(generated_function("Jan Kotas"))  ## Output: Dr. Jan
print(generated_function("Mariya Sergienko"))  ## Output: Dr. Mariya

# End time: 2024-04-10 14:32:16.137227
# Elapsed time in seconds: 1.450006395999992
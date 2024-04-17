# Start time: 2024-04-10 15:15:24.387375

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals.
- Each entry in the input column data follows the format of "First Name Last Name".

Summary for Output Column:
- The output column consists of initials derived from the input column data.
- Each entry in the output column represents the first initial of the first name followed by a period and then the first initial of the last name.

Relationship between Input and Output:
- The output column is generated by taking the first initial of the first name and the first initial of the last name from the input column data.
- The relationship between the input and output is that the output provides a concise representation of the input data by using initials., and input as ['Nancy FreeHafer'] output is N.F., input as ['Andrew Cencici'] output is A.C., input as ['Jan Kotas'] output is J.K., input as ['Mariya Sergienko'] output is M.S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
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
print(generated_function('Nancy FreeHafer'))  # Output: ['N.F.']
print(generated_function('Andrew Cencici'))  # Output: ['A.C.']
print(generated_function('Jan Kotas'))  # Output: ['J.K.']
print(generated_function('Mariya Sergienko'))  # Output: ['M.S.']
print(generated_function("Nancy FreeHafer"))  ## Output: N.F.
print(generated_function("Andrew Cencici"))  ## Output: A.C.
print(generated_function("Jan Kotas"))  ## Output: J.K.
print(generated_function("Mariya Sergienko"))  ## Output: M.S.

# End time: 2024-04-10 15:15:26.177456
# Elapsed time in seconds: 1.7900411290002012
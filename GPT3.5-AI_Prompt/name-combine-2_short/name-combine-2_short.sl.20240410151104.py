# Start time: 2024-04-10 15:29:03.961000

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:
- The input column data consists of pairs of first and last names.
- Each pair represents a person's full name.

Summary for output column data:
- The output column data consists of the first initial of the first name followed by a period.
- This format is consistent across all output values.

Relationship between input and output:
- The output column data is derived from the input column data by taking the first initial of the first name and adding a period.
- This relationship is consistent and follows a specific pattern for all input values.
- The output column data serves as a shortened version of the full name provided in the input column data., and input as ['Nancy', 'FreeHafer'] output is Nancy F., input as ['Andrew', 'Cencici'] output is Andrew C., input as ['Jan', 'Kotas'] output is Jan K., input as ['Mariya', 'Sergienko'] output is Mariya S., , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(first_name, last_name):
    # Extract the first initial of the first name and add a period
    output = first_name[0] + '.'
    
    return output

# Test cases
print(generated_function('Nancy', 'FreeHafer'))
print(generated_function('Andrew', 'Cencici'))
print(generated_function('Jan', 'Kotas'))
print(generated_function('Mariya', 'Sergienko'))
print(generated_function("Nancy", "FreeHafer"))  ## Output: Nancy F.
print(generated_function("Andrew", "Cencici"))  ## Output: Andrew C.
print(generated_function("Jan", "Kotas"))  ## Output: Jan K.
print(generated_function("Mariya", "Sergienko"))  ## Output: Mariya S.

# End time: 2024-04-10 15:29:05.271214
# Elapsed time in seconds: 1.310187027000211
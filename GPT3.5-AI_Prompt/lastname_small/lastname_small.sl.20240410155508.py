# Start time: 2024-04-10 16:00:12.078261

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names of individuals.
- Each entry in the input column follows the format of 'First Name Last Name'.

Output Column Summary:
- The output column consists of the last names extracted from the input column data.
- Each entry in the output column represents the last name of the corresponding individual in the input column.

Relationship Summary:
- The relationship between the input and output columns is that the last names in the output column are extracted from the full names in the input column.
- The output column serves as a simplified version of the input column, focusing solely on the last names of the individuals.
- This relationship allows for easy identification and categorization of individuals based on their last names., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Split the input string into first name and last name
    first_name, last_name = input_str.split(' ')
    
    # Return the last name extracted from the input string
    return last_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: FreeHafer
print(generated_function('Andrew Cencici'))  # Output: Cencici
print(generated_function('Jan Kotas'))  # Output: Kotas
print(generated_function('Mariya Sergienko'))  # Output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-10 16:00:14.484730
# Elapsed time in seconds: 2.406409015999998
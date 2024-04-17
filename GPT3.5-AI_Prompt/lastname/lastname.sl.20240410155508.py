# Start time: 2024-04-10 16:07:13.001083

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals, such as Nancy FreeHafer, Andrew Cencici, Jan Kotas, and Mariya Sergienko.

Summary for Output Column Data:
- The output column data consists of the last names of the individuals from the input column, such as FreeHafer, Cencici, Kotas, and Sergienko.

Relationship between Input and Output:
- The output column data represents the last names extracted from the full names provided in the input column. The last names serve as a distinct identifier for each individual in the input data. This relationship allows for easy reference and categorization based on the last names of the individuals., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string to extract the full name
    full_name = input_str.split()[1]
    # Return the last name
    return full_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: FreeHafer
print(generated_function('Andrew Cencici'))  # Output: Cencici
print(generated_function('Jan Kotas'))  # Output: Kotas
print(generated_function('Mariya Sergienko'))  # Output: Sergienko
print(generated_function("Nancy FreeHafer"))  ## Output: FreeHafer
print(generated_function("Andrew Cencici"))  ## Output: Cencici
print(generated_function("Jan Kotas"))  ## Output: Kotas
print(generated_function("Mariya Sergienko"))  ## Output: Sergienko

# End time: 2024-04-10 16:07:15.149784
# Elapsed time in seconds: 2.1486434180005745
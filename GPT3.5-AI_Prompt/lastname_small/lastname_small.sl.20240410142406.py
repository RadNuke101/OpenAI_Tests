# Start time: 2024-04-10 14:29:22.649784

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names of individuals.
- Each entry in the input column data includes a first name followed by a last name.
- The names in the input column data appear to be diverse and varied.

Summary for Output Column Data:
- The output column data consists of last names extracted from the input column data.
- Each entry in the output column data represents the last name of the corresponding individual in the input column data.
- The output column data specifically focuses on the last names of the individuals.

Relationship between Input and Output:
- The output column data serves as a subset of the input column data, specifically highlighting the last names of the individuals.
- By extracting and presenting only the last names, the output column data simplifies the information provided in the input column data.
- The output column data helps to identify and emphasize the commonality among the individuals based on their last names.
- Overall, the relationship between the input and output column data showcases a transformation from full names to last names, providing a more focused perspective on the data., and input as ['Nancy FreeHafer'] output is FreeHafer, input as ['Andrew Cencici'] output is Cencici, input as ['Jan Kotas'] output is Kotas, input as ['Mariya Sergienko'] output is Sergienko, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Split the input string into first name and last name
    name_parts = input_str.split()
    last_name = name_parts[-1]
    
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

# End time: 2024-04-10 14:29:24.202759
# Elapsed time in seconds: 1.552941015999977
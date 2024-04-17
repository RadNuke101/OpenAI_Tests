# Start time: 2024-04-10 15:58:55.634598

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of names of individuals such as Nancy FreeHafer, Andrew Cencici, Jan Kotas, and Mariya Sergienko.

Output Column Summary:
- The output column consists of the first names extracted from the input data, which are Nancy, Andrew, Jan, and Mariya.

Relationship Summary:
- The relationship between the input and output columns is that the output column contains the first names extracted from the input column data. The output column serves as a simplified version of the input data, focusing only on the first names of the individuals mentioned. This relationship helps in quickly identifying and referencing individuals by their first names., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string to extract the first name
    first_name = input_str.split()[0]
    
    # Return the first name
    return first_name

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: Nancy
print(generated_function('Andrew Cencici'))  # Output: Andrew
print(generated_function('Jan Kotas'))  # Output: Jan
print(generated_function('Mariya Sergienko'))  # Output: Mariya
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-10 15:58:57.479952
# Elapsed time in seconds: 1.8452856560006694
# Start time: 2024-04-10 14:55:48.470864

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names with varying formats, including first names, middle initials, and last names.

Output Column Summary:
- The output column consists of only the first names extracted from the input data.

Relationship Summary:
- The relationship between the input and output columns is that the output column extracts and displays only the first names from the input data. This process involves parsing the full names and isolating the first names, regardless of the presence of middle initials or last names. The output serves as a simplified version of the input, focusing solely on the first names provided., and input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string by whitespace
    name_parts = input_str.split()
    # Return the first element which is the first name
    return name_parts[0]

# Test cases
print(generated_function('Susan Ann Chang'))  # Output: Susan
print(generated_function('Ayako Tanaka'))  # Output: Ayako
print(generated_function('Bobby T. Smith'))  # Output: Bobby
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-10 14:55:50.074501
# Elapsed time in seconds: 1.6035974140002054
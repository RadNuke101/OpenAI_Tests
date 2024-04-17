# Start time: 2024-04-10 15:42:12.096998

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of names of individuals, with each entry containing a first name followed by a last name.

Output Column Summary:
- The output column data consists of only the first names extracted from the input column data.

Relationship Summary:
- The relationship between the input and output columns is that the output column extracts and presents only the first names from the input column data. This process involves separating the first name from the full name provided in the input. The output serves as a simplified version of the input, focusing solely on the first names of the individuals., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Split the input string into first name and last name
    first_name = input_str.split()[0]
    
    return first_name

# Test cases
print(generated_function('Nancy FreeHafer'))
print(generated_function('Andrew Cencici'))
print(generated_function('Jan Kotas'))
print(generated_function('Mariya Sergienko'))
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-10 15:42:13.736153
# Elapsed time in seconds: 1.6391261540002233
# Start time: 2024-04-10 16:02:34.775432

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of names in various formats, including full names with middle names or initials.

Output Column Summary:
- The output column data consists of the first names extracted from the input names.

Relationship Summary:
- The relationship between the input and output columns is that the output column extracts and presents only the first names from the input names. This process involves parsing and isolating the first name component from the full names provided in the input column. The output serves as a simplified version of the input, focusing solely on the first names of individuals., and input as ['Susan Ann Chang'] output is Susan, input as ['Ayako Tanaka'] output is Ayako, input as ['Bobby T. smth'] output is Bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into a list of names
    names = input_str.split()
    
    # Extract the first name from the list of names
    first_name = names[0]
    
    return first_name

# Test cases
print(generated_function('Susan Ann Chang'))  # Output: Susan
print(generated_function('Ayako Tanaka'))  # Output: Ayako
print(generated_function('Bobby T. Smith'))  # Output: Bobby
print(generated_function("Susan Ann Chang"))  ## Output: Susan
print(generated_function("Ayako Tanaka"))  ## Output: Ayako
print(generated_function("Bobby T. smth"))  ## Output: Bobby

# End time: 2024-04-10 16:02:36.400600
# Elapsed time in seconds: 1.6251243599999725
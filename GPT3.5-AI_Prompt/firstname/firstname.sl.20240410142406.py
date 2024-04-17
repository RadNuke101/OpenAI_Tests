# Start time: 2024-04-10 14:27:50.399419

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of names of individuals such as Nancy FreeHafer, Andrew Cencici, Jan Kotas, and Mariya Sergienko.

Output Column Summary:
- The output column consists of the first names extracted from the input column data, which are Nancy, Andrew, Jan, and Mariya.

Relationship Summary:
- The relationship between the input and output columns is that the output column only includes the first names of the individuals provided in the input column. The output column serves as a simplified version of the input column, focusing solely on the first names. This relationship highlights the process of extracting and simplifying information from the input data., and input as ['Nancy FreeHafer'] output is Nancy, input as ['Andrew Cencici'] output is Andrew, input as ['Jan Kotas'] output is Jan, input as ['Mariya Sergienko'] output is Mariya, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    # Initialize an empty list to store the output
    output = []
    
    # Iterate through each input argument
    for arg in args:
        # Split the input argument by space and extract the first element
        first_name = arg.split()[0]
        # Append the first name to the output list
        output.append(first_name)
    
    # Return the output list
    return output

# Test cases
print(generated_function('Nancy FreeHafer'))  # Output: ['Nancy']
print(generated_function('Andrew Cencici'))    # Output: ['Andrew']
print(generated_function('Jan Kotas'))         # Output: ['Jan']
print(generated_function('Mariya Sergienko'))  # Output: ['Mariya']
print(generated_function("Nancy FreeHafer"))  ## Output: Nancy
print(generated_function("Andrew Cencici"))  ## Output: Andrew
print(generated_function("Jan Kotas"))  ## Output: Jan
print(generated_function("Mariya Sergienko"))  ## Output: Mariya

# End time: 2024-04-10 14:27:52.250942
# Elapsed time in seconds: 1.851487502999987
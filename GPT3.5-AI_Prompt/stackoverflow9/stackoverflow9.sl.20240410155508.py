# Start time: 2024-04-10 16:11:36.991727

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names in the format of first name, middle name, and last name. The names appear to be in the format of "First Middle Last".

Output Column Summary:
- The output column consists of last names extracted from the input column data.

Relationship Summary:
- The relationship between the input and output columns is that the output column specifically focuses on extracting and displaying the last names from the input column data. This relationship indicates a pattern of extracting the last name from full names provided in the input column., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    # Initialize an empty list to store the output
    output = []
    
    # Iterate through each input argument
    for arg in args:
        # Split the input string into first, middle, and last names
        names = arg.split()
        # Extract the last name and append it to the output list
        output.append(names[-1])
    
    # Return the output list
    return output

# Test cases
generated_function('Sarah Jane Jones', 'Bob Jane Smithfield')
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-10 16:11:38.728486
# Elapsed time in seconds: 1.7367560080001567
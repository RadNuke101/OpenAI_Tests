# Start time: 2024-04-10 15:05:54.859322

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names in the format of first name, middle name, and last name.

Output Column Summary:
- The output column data consists of last names extracted from the input column data.

Relationship Summary:
- The relationship between the input and output columns is that the output column specifically focuses on extracting and displaying the last names from the input column data. This relationship indicates a transformation process where the last names are isolated and presented as standalone information., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into first name, middle name, and last name
    names = input_str.split()
    last_name = names[-1]  # Extract the last name
    return last_name

# Test cases
print(generated_function('Sarah Jane Jones'))  # Output: Jones
print(generated_function('Bob Jane Smithfield'))  # Output: Smithfield
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-10 15:05:56.540194
# Elapsed time in seconds: 1.680835331000253
# Start time: 2024-04-10 15:49:59.163834

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names in the format of first name, middle name, and last name.

Output Column Summary:
- The output column data consists of last names extracted from the full names in the input column.

Relationship Summary:
- The relationship between the input and output columns is that the output column specifically focuses on extracting and displaying the last names from the full names provided in the input column. This process involves identifying and isolating the last name component from the complete name string. The output column serves as a simplified version of the input column, highlighting only the last names for easier reference or analysis., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into first name, middle name, and last name
    names = input_str.split()
    # Extract and return the last name
    return names[-1]

# Test cases
print(generated_function('Sarah Jane Jones'))
print(generated_function('Bob Jane Smithfield'))
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-10 15:50:00.500523
# Elapsed time in seconds: 1.3366593569999168
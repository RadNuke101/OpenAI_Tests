# Start time: 2024-04-10 14:41:01.142794

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names in the format of first name, middle name, and last name.

Output Column Summary:
- The output column data consists of last names extracted from the input column data.

Relationship Summary:
- The relationship between the input and output columns is that the output column specifically focuses on extracting and displaying the last names from the input column data. This process involves identifying and isolating the last name component from the full names provided in the input column. The output column serves as a simplified representation of the last names present in the input data, allowing for easier analysis and categorization based on this specific attribute., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to extract last names from full names
def generated_function(*args):
    output = []
    for full_name in args:
        last_name = full_name.split()[-1]
        output.append(last_name)
    return output

# Test cases
print(generated_function('Sarah Jane Jones'))  # Output should be 'Jones'
print(generated_function('Bob Jane Smithfield'))  # Output should be 'Smithfield'
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-10 14:41:02.796694
# Elapsed time in seconds: 1.65386437199993
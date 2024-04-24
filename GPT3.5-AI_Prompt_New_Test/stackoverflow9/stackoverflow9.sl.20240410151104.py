# Start time: 2024-04-10 15:28:25.821523

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names in the format of first name, middle name, and last name.

Output Column Summary:
- The output column data consists of last names extracted from the input column data.

Relationship Summary:
- The relationship between the input and output columns is that the output column specifically focuses on extracting and displaying the last names from the input column data. This relationship allows for a clear and concise way to identify and present the last names of individuals based on their full names provided in the input column., and input as ['Sarah Jane Jones'] output is Jones, input as ['Bob Jane Smithfield'] output is Smithfield, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    # Initialize an empty list to store the output last names
    output = []
    
    # Iterate through each input argument
    for arg in args:
        # Split the input full name into a list of names
        names = arg.split()
        # Extract the last name from the list of names
        last_name = names[-1]
        # Append the last name to the output list
        output.append(last_name)
    
    # Return the list of last names as a single string
    return ', '.join(output)

# Test cases
print(generated_function('Sarah Jane Jones'))  # Output should be 'Jones'
print(generated_function('Bob Jane Smithfield'))  # Output should be 'Smithfield'
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield

# End time: 2024-04-10 15:28:28.377565
# Elapsed time in seconds: 2.555992429000071


# APPEND TEST SCRIPTS...
print(generated_function("Sarah Jane Jones"))  ## Output: Jones
print(generated_function("Bob Jane Smithfield"))  ## Output: Smithfield


print(generated_function("Jones Jane Sarah"))  ### Output: Sarah
print(generated_function("Smithfield Jane Bob"))  ### Output: Bob

# TEST SCRIPTS APPENDED!


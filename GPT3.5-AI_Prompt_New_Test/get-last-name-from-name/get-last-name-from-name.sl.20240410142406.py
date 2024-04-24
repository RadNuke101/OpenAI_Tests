# Start time: 2024-04-10 14:42:55.599861

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of full names in the format of [First Name Last Name].
- The names in the input column appear to be of Asian origin, with common surnames such as Park, Lee, and Kim.

Output Column Summary:
- The output column consists of the last names extracted from the input column data.
- The last names in the output column are consistently the second part of the full names in the input column.

Relationship Summary:
- The relationship between the input and output columns is that the output column extracts and presents the last names from the input column data.
- The output column serves as a way to isolate and focus on the common element of last names present in the input column data.
- This relationship highlights the importance of last names in identifying individuals and understanding their cultural background., and input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    # Initialize an empty list to store the output last names
    output = []
    
    # Iterate through each input argument
    for arg in args:
        # Split the input argument into first name and last name
        first_name, last_name = arg.split()
        # Append the last name to the output list
        output.append(last_name)
    
    # Return the list of last names as a single string
    return ', '.join(output)

# Test cases
generated_function('Park Kim', 'Lee Kim', 'Kim Lee')
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-10 14:42:57.346900
# Elapsed time in seconds: 1.7469988200000444


# APPEND TEST SCRIPTS...
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee


print(generated_function("Benjamin Hayes"))  ### Output: Hayes
print(generated_function("Emma Reynolds"))  ### Output: Reynolds
print(generated_function("Grace Harrison"))  ### Output: Harrison
print(generated_function("Caleb Mitchell"))  ### Output: Mitchell
print(generated_function("Olivia Parker"))  ### Output: Parker
print(generated_function("Jackson Turner"))  ### Output: Turner

# TEST SCRIPTS APPENDED!


# Start time: 2024-04-10 15:51:05.783591

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of names in the format of [First Name Last Name].
- The names in the input column data are diverse, with different combinations of first and last names.

Summary for Output Column Data:
- The output column data consists of last names extracted from the input column data.
- The last names in the output column data are consistent and follow the pattern of being the second part of the input names.

Relationship between Input and Output:
- The output column data consistently extracts the last names from the input column data.
- The relationship between the input and output is that the last names are extracted and presented as the output.
- The output column provides a simplified version of the input data by focusing on the last names only., and input as ['Park Kim'] output is Kim, input as ['Lee Kim'] output is Kim, input as ['Kim Lee'] output is Lee, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        output.append(name.split()[1])
    return output

# Test cases
generated_function('Park Kim', 'Lee Kim', 'Kim Lee')
print(generated_function("Park Kim"))  ## Output: Kim
print(generated_function("Lee Kim"))  ## Output: Kim
print(generated_function("Kim Lee"))  ## Output: Lee

# End time: 2024-04-10 15:51:06.816419
# Elapsed time in seconds: 1.0328049640002064


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


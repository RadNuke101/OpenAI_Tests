# Start time: 2024-04-10 15:36:23.726279

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names in the format last name, first name. 
- The names in the input column data are presented in a consistent format with the last name appearing before the first name.

Summary for Output Column Data:
- The output column data consists of full names in the format first name, last name.
- The names in the output column data are presented in a consistent format with the first name appearing before the last name.

Relationship between Input and Output:
- The relationship between the input and output columns is that the order of the names is reversed in the output compared to the input.
- The input column data provides the names in the format last name, first name, while the output column data presents the names in the format first name, last name.
- The transformation applied to the input data to generate the output data involves switching the order of the first and last names., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        last_name, first_name = name.split(',')
        output.append(f"{first_name.strip()},{last_name.strip()}")
    return output

# Test cases
generated_function('chang,amy', 'smith,bobby', 'lennox,aaron')
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-10 15:36:25.136502
# Elapsed time in seconds: 1.410171865999473


# APPEND TEST SCRIPTS...
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox


print(generated_function("hayes,benjamin"))  ### Output: benjamin,hayes
print(generated_function("parker,olivia"))  ### Output: olivia,parker
print(generated_function("turner,jackson"))  ### Output: jackson,turner

# TEST SCRIPTS APPENDED!


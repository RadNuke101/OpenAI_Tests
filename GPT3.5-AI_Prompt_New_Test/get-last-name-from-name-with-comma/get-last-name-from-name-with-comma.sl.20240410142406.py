# Start time: 2024-04-10 14:26:30.117592

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names in the format 'last name, first name'.
- The names in the input column data are in a consistent format with the last name appearing before the first name.

Summary for Output Column:
- The output column consists of rearranged full names in the format 'first name, last name'.
- The output column shows a consistent pattern of reversing the order of the names from the input column.

Relationship between Input and Output:
- The relationship between the input and output columns is that the names in the input column are rearranged to have the first name appear before the last name in the output column.
- The transformation applied to the input data involves reversing the order of the names while maintaining the original names themselves., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    output = []
    for name in args:
        last_name, first_name = name.split(',')
        rearranged_name = f"{first_name.strip()},{last_name.strip()}"
        output.append(rearranged_name)
    return output

# Test cases
generated_function('chang,amy', 'smith,bobby', 'lennox,aaron')
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-10 14:26:31.148819
# Elapsed time in seconds: 1.0312094630000104


# APPEND TEST SCRIPTS...
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox


print(generated_function("hayes,benjamin"))  ### Output: benjamin,hayes
print(generated_function("parker,olivia"))  ### Output: olivia,parker
print(generated_function("turner,jackson"))  ### Output: jackson,turner

# TEST SCRIPTS APPENDED!


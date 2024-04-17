# Start time: 2024-04-10 14:50:58.027942

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:
- The input column data consists of full names in the format last name, first name.

Summary for output column data:
- The output column data consists of full names in the format first name, last name.

Relationship between input and output:
- The relationship between the input and output is that the order of the first and last names is reversed. The input column data provides names in the format last name, first name, while the output column data presents names in the format first name, last name. This indicates a transformation where the order of the names is switched., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into last name and first name
    last_name, first_name = input_str.split(',')
    
    # Rearrange the names in the desired format
    output_str = f"{first_name.strip()},{last_name.strip()}"
    
    return output_str

# Test cases
print(generated_function('chang,amy'))  # Output: amy,chang
print(generated_function('smith,bobby'))  # Output: bobby,smith
print(generated_function('lennox,aaron'))  # Output: aaron,lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-10 14:50:59.777233
# Elapsed time in seconds: 1.7492390840000098
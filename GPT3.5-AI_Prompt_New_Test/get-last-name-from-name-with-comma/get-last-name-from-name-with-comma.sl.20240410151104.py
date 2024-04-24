# Start time: 2024-04-10 15:13:27.599198

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of names in the format "last name, first name."
- Each entry in the input column data follows the same pattern of last name followed by a comma and then the first name.

Summary for Output Column Data:
- The output column data consists of names in the format "first name, last name."
- Each entry in the output column data follows the pattern of first name followed by a comma and then the last name.

Relationship between Input and Output:
- The relationship between the input and output is a reversal of the order of the names.
- The input column data has the last name listed first followed by the first name, while the output column data has the first name listed first followed by the last name.
- The transformation involves switching the order of the names from the input to the output., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into last name and first name
    last_name, first_name = input_str.split(',')
    
    # Reorder the names and concatenate them with a comma
    output_str = f"{first_name.strip()},{last_name.strip()}"
    
    return output_str

# Test cases
print(generated_function('chang,amy')) # Output: amy,chang
print(generated_function('smith,bobby')) # Output: bobby,smith
print(generated_function('lennox,aaron')) # Output: aaron,lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-10 15:13:29.526753
# Elapsed time in seconds: 1.9275079459998778


# APPEND TEST SCRIPTS...
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox


print(generated_function("hayes,benjamin"))  ### Output: benjamin,hayes
print(generated_function("parker,olivia"))  ### Output: olivia,parker
print(generated_function("turner,jackson"))  ### Output: jackson,turner

# TEST SCRIPTS APPENDED!


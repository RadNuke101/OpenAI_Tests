# Start time: 2024-04-10 15:57:27.257889

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
- The input column data consists of full names in the format "last name, first name."

Summary for Output Column:
- The output column consists of rearranged full names in the format "first name, last name."

Relationship between Input and Output:
- The relationship between the input and output is that the full names in the input column are rearranged to have the first name come before the last name in the output column. This rearrangement is consistent across all input data, indicating a pattern in the transformation process., and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into last name and first name
    last_name, first_name = input_str.split(',')
    
    # Rearrange the full name to have first name before last name
    output_str = f"{first_name},{last_name}"
    
    return output_str

# Test cases
print(generated_function('chang,amy'))
print(generated_function('smith,bobby'))
print(generated_function('lennox,aaron'))
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-10 15:57:28.710942
# Elapsed time in seconds: 1.453019143000347
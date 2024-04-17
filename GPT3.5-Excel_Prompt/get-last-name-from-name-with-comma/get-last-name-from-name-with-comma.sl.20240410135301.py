# Start time: 2024-04-10 13:54:30.999892

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression, and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Split the input string at the comma
    parts = input_str.split(',')
    
    # Rearrange the parts and join them with a comma
    output = parts[1] + ',' + parts[0]
    
    return output

# Test cases
print(generated_function('chang,amy'))
print(generated_function('smith,bobby'))
print(generated_function('lennox,aaron'))
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-10 13:54:32.657404
# Elapsed time in seconds: 1.6582793070001571
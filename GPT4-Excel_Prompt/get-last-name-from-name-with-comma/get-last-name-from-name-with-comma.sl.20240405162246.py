# Start time: 2024-04-05 16:27:49.191084

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: first return everything after the "," in the inputted expression, followed by a comma, and then everything before the "," in the inputted expression, and input as ['chang,amy'] output is amy,chang, input as ['smith,bobby'] output is bobby,smith, input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression):
    # Split the input expression at the comma
    parts = expression.split(',')
    # Return the formatted string as per the prompt's instructions
    return parts[1] + ',' + parts[0]

# Test cases as per the prompt
print(generated_function('chang,amy'))  # Expected output: amy,chang
print(generated_function('smith,bobby'))  # Expected output: bobby,smith
print(generated_function('lennox,aaron'))  # Expected output: aaron,lennox
print(generated_function("chang,amy"))  ## Output: amy,chang
print(generated_function("smith,bobby"))  ## Output: bobby,smith
print(generated_function("lennox,aaron"))  ## Output: aaron,lennox

# End time: 2024-04-05 16:27:52.195965
# Elapsed time in seconds: 3.0048467420001543
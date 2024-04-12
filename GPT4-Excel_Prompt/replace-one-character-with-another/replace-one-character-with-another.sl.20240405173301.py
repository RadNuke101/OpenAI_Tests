# Start time: 2024-04-05 17:50:33.753324

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: replace spaces in input with "-", and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string):
    # Replace spaces in the input string with "-"
    return input_string.replace(" ", "-")

# Test cases
output1 = generated_function('801 456 8756')
output2 = generated_function('978 456 8756')
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-05 17:50:35.594467
# Elapsed time in seconds: 1.8410990929996842
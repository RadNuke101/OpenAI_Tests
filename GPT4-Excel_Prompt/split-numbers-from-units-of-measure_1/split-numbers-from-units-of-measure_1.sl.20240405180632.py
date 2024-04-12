# Start time: 2024-04-05 18:25:24.890644

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the numbers from first input, and input as ['80v', '3'] output is 80, input as ['10hrs', '3'] output is 10, input as ['7h', '2'] output is 7, input as ['500m', '4'] output is 500, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string, _):
    # Extracting digits from the input string and returning them
    return ''.join(filter(str.isdigit, input_string))

# Test cases
generated_function('80v', '3')  # Expected output: '80'
generated_function('10hrs', '3')  # Expected output: '10'
generated_function('7h', '2')  # Expected output: '7'
generated_function('500m', '4')  # Expected output: '500'
print(generated_function("80v", "3"))  ## Output: 80
print(generated_function("10hrs", "3"))  ## Output: 10
print(generated_function("7h", "2"))  ## Output: 7
print(generated_function("500m", "4"))  ## Output: 500

# End time: 2024-04-05 18:25:27.824785
# Elapsed time in seconds: 2.9340540209996107
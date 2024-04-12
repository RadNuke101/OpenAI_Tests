# Start time: 2024-04-05 16:02:08.132974

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if "-" present in the beginning of inputted expression (first column), remove it, and input as ['-%134'] output is %134, input as ['500'] output is 500, input as ['5.125'] output is 5.125, input as ['-%43.00'] output is %43.00, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression):
    # Check if the expression starts with '-'
    if expression.startswith('-'):
        # Remove the '-' from the beginning
        return expression[1:]
    else:
        # Return the expression as is if it doesn't start with '-'
        return expression

# Test cases
result1 = generated_function('-%134')
result2 = generated_function('500')
result3 = generated_function('5.125')
result4 = generated_function('-%43.00')
print(generated_function("-%134"))  ## Output: %134
print(generated_function("500"))  ## Output: 500
print(generated_function("5.125"))  ## Output: 5.125
print(generated_function("-%43.00"))  ## Output: %43.00

# End time: 2024-04-05 16:02:12.415129
# Elapsed time in seconds: 4.282026626000061
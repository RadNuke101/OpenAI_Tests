# Start time: 2024-04-05 16:47:10.714214

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the text before the last 3 numbers in inputted expression, and input as ['Ducati100'] output is Ducati, input as ['Honda125'] output is Honda, input as ['Ducati250'] output is Ducati, input as ['Honda250'] output is Honda, input as ['Honda550'] output is Honda, input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression):
    # Extract and return the text before the last 3 numbers in the inputted expression
    return expression[:-3]

# Test cases
result1 = generated_function('Ducati100')
result2 = generated_function('Honda125')
result3 = generated_function('Ducati250')
result4 = generated_function('Honda250')
result5 = generated_function('Honda550')
result6 = generated_function('Ducati125')
print(generated_function("Ducati100"))  ## Output: Ducati
print(generated_function("Honda125"))  ## Output: Honda
print(generated_function("Ducati250"))  ## Output: Ducati
print(generated_function("Honda250"))  ## Output: Honda
print(generated_function("Honda550"))  ## Output: Honda
print(generated_function("Ducati125"))  ## Output: Ducati

# End time: 2024-04-05 16:47:13.910411
# Elapsed time in seconds: 3.1961596619999
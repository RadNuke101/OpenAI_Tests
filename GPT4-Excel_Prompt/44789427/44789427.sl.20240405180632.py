# Start time: 2024-04-05 18:31:03.978238

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if second input (second column) is "1", return everything before "-" in expression, else if second input is "2", return everything after "-" in expression, and input as ['1/17/16-1/18/17', '1'] output is 1/17/16, input as ['1/17/16-1/18/17', '2'] output is 1/18/17, input as ['01/17/2016-01/18/2017', '1'] output is 01/17/2016, input as ['01/17/2016-01/18/2017', '2'] output is 01/18/2017, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(expression, option):
    # Split the expression at the "-" character
    parts = expression.split("-")
    # Check the option and return the corresponding part of the expression
    if option == '1':
        return parts[0]
    elif option == '2':
        return parts[1]
    else:
        return "Invalid option"

# Test cases
result1 = generated_function('1/17/16-1/18/17', '1')
result2 = generated_function('1/17/16-1/18/17', '2')
result3 = generated_function('01/17/2016-01/18/2017', '1')
result4 = generated_function('01/17/2016-01/18/2017', '2')

# The outputs of these test cases should match the given examples in the prompt.
print(generated_function("1/17/16-1/18/17", "1"))  ## Output: 1/17/16
print(generated_function("1/17/16-1/18/17", "2"))  ## Output: 1/18/17
print(generated_function("01/17/2016-01/18/2017", "1"))  ## Output: 01/17/2016
print(generated_function("01/17/2016-01/18/2017", "2"))  ## Output: 01/18/2017

# End time: 2024-04-05 18:31:09.826782
# Elapsed time in seconds: 5.848449492001237
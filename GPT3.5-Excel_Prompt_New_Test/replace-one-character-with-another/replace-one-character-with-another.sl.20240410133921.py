# Start time: 2024-04-10 13:45:22.702417

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: replace spaces in input with "-", and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    result = []
    for arg in args:
        result.append(arg.replace(" ", "-"))
    return result
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-10 13:45:23.510407
# Elapsed time in seconds: 0.8079714129999047


# APPEND TEST SCRIPTS...
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756


print(generated_function("456 801 8756"))  ### Output: 456-801-8756
print(generated_function("456 978 8756"))  ### Output: 456-978-8756

# TEST SCRIPTS APPENDED!


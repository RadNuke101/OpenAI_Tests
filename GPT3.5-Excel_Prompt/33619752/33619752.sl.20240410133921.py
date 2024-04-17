# Start time: 2024-04-10 13:47:37.729659

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: remove the words "Inc", "Company", "Corporation", or "Enterprises", and input as ['General Electric'] output is General Electric, input as ['General Electric Inc'] output is General Electric, input as ['General Electric Company'] output is General Electric, input as ['Microsoft'] output is Microsoft, input as ['Microsoft Corporation'] output is Microsoft, input as ['Nintendo'] output is Nintendo, input as ['Nintendo Enterprises'] output is Nintendo, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    for arg in args:
        if "Inc" in arg:
            return arg.replace(" Inc", "")
        elif "Company" in arg:
            return arg.replace(" Company", "")
        elif "Corporation" in arg:
            return arg.replace(" Corporation", "")
        elif "Enterprises" in arg:
            return arg.replace(" Enterprises", "")
        else:
            return arg
print(generated_function("General Electric"))  ## Output: General Electric
print(generated_function("General Electric Inc"))  ## Output: General Electric
print(generated_function("General Electric Company"))  ## Output: General Electric
print(generated_function("Microsoft"))  ## Output: Microsoft
print(generated_function("Microsoft Corporation"))  ## Output: Microsoft
print(generated_function("Nintendo"))  ## Output: Nintendo
print(generated_function("Nintendo Enterprises"))  ## Output: Nintendo

# End time: 2024-04-10 13:47:39.324316
# Elapsed time in seconds: 1.5946212419999028
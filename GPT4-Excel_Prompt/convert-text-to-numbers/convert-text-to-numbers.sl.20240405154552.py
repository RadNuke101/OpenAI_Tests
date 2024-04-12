# Start time: 2024-04-05 16:15:31.438867

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return the input, and input as ['101'] output is 101, input as ['1002'] output is 1002, input as ['743'] output is 743, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(*args):
    # If there's only one argument, return it directly after converting to int
    if len(args) == 1:
        return int(args[0])
    # If there are multiple arguments, convert each to int and return them as a list
    else:
        return [int(arg) for arg in args]

# Test cases
generated_function('101')
generated_function('1002')
generated_function('743')
print(generated_function("101"))  ## Output: 101
print(generated_function("1002"))  ## Output: 1002
print(generated_function("743"))  ## Output: 743

# End time: 2024-04-05 16:15:34.175686
# Elapsed time in seconds: 2.7367422859999806
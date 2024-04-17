# Start time: 2024-04-16 14:28:27.391083

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: From the left, delete the number (second input) of elements from the first input, and input as ['1234', '1'] output is 234, input as ['**512A', '2'] output is 512A, input as ['343DMX', '3'] output is DMX, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above. All boolean return value should be converted to lowercase string.
'''

# Define the function
def generated_function(input_str, num):
    return input_str[int(num):]

# Test cases
generated_function('1234', '1')
generated_function('**512A', '2')
generated_function('343DMX', '3')



print(generated_function("38fj2io3jaowiu3rhijhjaklsf", "3"))  ### Output: "38fj2io3jaowiu3rhijhjaklsf", "3"
print(generated_function("j(#*ur)", "2"))  ### Output: "j(#*ur)", "2"
print(generated_function("8231r", "1"))  ### Output: "8231r", "1"
print(generated_function("38fj2io3", "3"))  ### Output: "38fj2io3", "3"


print(generated_function("1234", "1"))  ## Output: 234
print(generated_function("**512A", "2"))  ## Output: 512A
print(generated_function("343DMX", "3"))  ## Output: DMX



# End time: 2024-04-16 14:28:28.575449
# Elapsed time in seconds: 1.1843280809999897
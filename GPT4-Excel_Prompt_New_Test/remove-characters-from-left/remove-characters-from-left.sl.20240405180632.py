# Start time: 2024-04-05 18:25:20.397165

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: From the left, delete the number (second input) of elements from the first input, and input as ['1234', '1'] output is 234, input as ['**512A', '2'] output is 512A, input as ['343DMX', '3'] output is DMX, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_string, num_to_delete):
    # Convert the second input to an integer to determine the number of characters to delete
    num_to_delete = int(num_to_delete)
    # Delete the specified number of characters from the left of the input string
    output_string = input_string[num_to_delete:]
    return output_string

# Test cases
output1 = generated_function('1234', '1')
output2 = generated_function('**512A', '2')
output3 = generated_function('343DMX', '3')

# The outputs can be checked against the expected results
print(generated_function("1234", "1"))  ## Output: 234
print(generated_function("**512A", "2"))  ## Output: 512A
print(generated_function("343DMX", "3"))  ## Output: DMX

# End time: 2024-04-05 18:25:24.829434
# Elapsed time in seconds: 4.432136432000334


# APPEND TEST SCRIPTS...
print(generated_function("1234", "1"))  ## Output: 234
print(generated_function("**512A", "2"))  ## Output: 512A
print(generated_function("343DMX", "3"))  ## Output: DMX


print(generated_function("38fj2io3jaowiu3rhijhjaklsf", "3"))  ### Output: j2io3jaowiu3rhijhjaklsf
print(generated_function("j(#*ur)", "2"))  ### Output: #*ur)
print(generated_function("8231r", "1"))  ### Output: 231r
print(generated_function("38fj2io3", "3"))  ### Output: j2io3

# TEST SCRIPTS APPENDED!


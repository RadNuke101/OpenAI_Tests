# Start time: 2024-04-10 14:33:35.779361

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: For the input column data, it appears to consist of phone numbers in different formats. Each input is preceded by a country code and followed by a series of numbers separated by hyphens. The numbers seem to be randomly generated and do not follow a specific pattern.

As for the output column, it consistently represents the last set of numbers in each input, which is separated by the last hyphen. This last set of numbers seems to be the focus of the output.

Therefore, the relationship between the input and output columns is that the output column consistently represents the last set of numbers in each input phone number. This suggests that the output is derived from the final segment of the input data., and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(*args):
    outputs = []
    for arg in args:
        output = arg.split('-')[-1]
        outputs.append(output)
    return outputs

# Test cases
generated_function('+106 769-858-438', '+83 973-757-831', '+62 647-787-775', '+172 027-507-632', '+72 001-050-856', '+95 310-537-401', '+6 775-969-238')
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238

# End time: 2024-04-10 14:33:37.633800
# Elapsed time in seconds: 1.8543970940000918
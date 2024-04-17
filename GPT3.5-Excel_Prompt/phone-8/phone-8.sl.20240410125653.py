# Start time: 2024-04-10 13:03:07.583320

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last three numbers in input, and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Split the input string by '-' and return the last element
    return input_str.split('-')[-1]

# Test cases
generated_function('+106 769-858-438')
generated_function('+83 973-757-831')
generated_function('+62 647-787-775')
generated_function('+172 027-507-632')
generated_function('+72 001-050-856')
generated_function('+95 310-537-401')
generated_function('+6 775-969-238')
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238

# End time: 2024-04-10 13:03:10.145981
# Elapsed time in seconds: 2.5626143540000044
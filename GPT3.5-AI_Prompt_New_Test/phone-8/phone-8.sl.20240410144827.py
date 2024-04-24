# Start time: 2024-04-10 14:57:57.090947

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: The input data consists of phone numbers in the format '+XX XXX-XXX-XXX', where XX represents the country code and the three sets of numbers represent different parts of the phone number. The output is always the last set of numbers, which represents the final digits of the phone number.

Based on the provided input data, it appears that the relationship between the input and output is that the output is always the last set of numbers in the phone number. This suggests that the output is derived directly from the input by extracting the final set of numbers.

Therefore, the summary for the relationship between the input and output is that the output is obtained by isolating and extracting the final set of numbers from the input phone number., and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(input_str):
    # Extract the last set of numbers from the input phone number
    output = input_str.split('-')[-1]
    
    return output
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238

# End time: 2024-04-10 14:57:58.010864
# Elapsed time in seconds: 0.9198906260000967


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238


print(generated_function("+95 310-401-537"))  ### Output: 537
print(generated_function("+6 775-238-969"))  ### Output: 969
print(generated_function("+172 027-632-507"))  ### Output: 507
print(generated_function("+72 001-856-050"))  ### Output: 050
print(generated_function("+106 769-438-858"))  ### Output: 858
print(generated_function("+62 647-775-787"))  ### Output: 787
print(generated_function("+83 973-831-757"))  ### Output: 757

# TEST SCRIPTS APPENDED!


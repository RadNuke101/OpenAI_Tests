# Start time: 2024-04-05 16:04:12.025343

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return last three numbers in input, and input as ['+106 769-858-438'] output is 438, input as ['+83 973-757-831'] output is 831, input as ['+62 647-787-775'] output is 775, input as ['+172 027-507-632'] output is 632, input as ['+72 001-050-856'] output is 856, input as ['+95 310-537-401'] output is 401, input as ['+6 775-969-238'] output is 238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    # Extracting the last three digits from the input phone number
    return phone_number[-3:]

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: 438
print(generated_function('+83 973-757-831'))   # Expected output: 831
print(generated_function('+62 647-787-775'))   # Expected output: 775
print(generated_function('+172 027-507-632'))  # Expected output: 632
print(generated_function('+72 001-050-856'))   # Expected output: 856
print(generated_function('+95 310-537-401'))   # Expected output: 401
print(generated_function('+6 775-969-238'))    # Expected output: 238
print(generated_function("+106 769-858-438"))  ## Output: 438
print(generated_function("+83 973-757-831"))  ## Output: 831
print(generated_function("+62 647-787-775"))  ## Output: 775
print(generated_function("+172 027-507-632"))  ## Output: 632
print(generated_function("+72 001-050-856"))  ## Output: 856
print(generated_function("+95 310-537-401"))  ## Output: 401
print(generated_function("+6 775-969-238"))  ## Output: 238

# End time: 2024-04-05 16:04:17.456483
# Elapsed time in seconds: 5.430977957000096
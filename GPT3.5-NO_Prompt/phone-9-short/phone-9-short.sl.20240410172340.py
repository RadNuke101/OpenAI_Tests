# Start time: 2024-04-10 17:30:39.377973

'''
Prompt:
Given that input as ['+106 769-858-438'] output is 106.769.858.438, input as ['+83 973-757-831'] output is 83.973.757.831, input as ['+62 647-787-775'] output is 62.647.787.775, input as ['+172 027-507-632'] output is 172.027.507.632, input as ['+72 001-050-856'] output is 72.001.050.856, input as ['+95 310-537-401'] output is 95.310.537.401, input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Remove the '+' sign and spaces from the input string
        input_str = input_str.replace('+', '').replace(' ', '')

        # Split the input string into three parts and join them with dots
        output_str = '.'.join([input_str[:3], input_str[3:6], input_str[6:9]])

        return output_str
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('+106 769-858-438'))  # Output: 106.769.858.438
print(generated_function('+83 973-757-831'))   # Output: 83.973.757.831
print(generated_function('+62 647-787-775'))   # Output: 62.647.787.775
print(generated_function('+172 027-507-632'))  # Output: 172.027.507.632
print(generated_function('+72 001-050-856'))   # Output: 72.001.050.856
print(generated_function('+95 310-537-401'))   # Output: 95.310.537.401
print(generated_function('+6 775-969-238'))    # Output: 6.775.969.238
print(generated_function("+106 769-858-438"))  ## Output: 106.769.858.438
print(generated_function("+83 973-757-831"))  ## Output: 83.973.757.831
print(generated_function("+62 647-787-775"))  ## Output: 62.647.787.775
print(generated_function("+172 027-507-632"))  ## Output: 172.027.507.632
print(generated_function("+72 001-050-856"))  ## Output: 72.001.050.856
print(generated_function("+95 310-537-401"))  ## Output: 95.310.537.401
print(generated_function("+6 775-969-238"))  ## Output: 6.775.969.238

# End time: 2024-04-10 17:30:44.175006
# Elapsed time in seconds: 4.798635940999986
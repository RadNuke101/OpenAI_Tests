# Start time: 2024-04-10 17:45:23.017406

'''
Prompt:
Given that input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(phone_number):
    try:
        country_code = int(phone_number.split()[0][1:])
        return country_code
    except (IndexError, ValueError):
        return None

# Test cases
print(generated_function('+106 769-858-438'))  # Output: 106
print(generated_function('+83 973-757-831'))   # Output: 83
print(generated_function('+62 647-787-775'))   # Output: 62
print(generated_function('+172 027-507-632'))  # Output: 172
print(generated_function('+72 001-050-856'))   # Output: 72
print(generated_function('+95 310-537-401'))   # Output: 95
print(generated_function('+6 775-969-238'))    # Output: 6
print(generated_function("+106 769-858-438"))  ## Output: 106
print(generated_function("+83 973-757-831"))  ## Output: 83
print(generated_function("+62 647-787-775"))  ## Output: 62
print(generated_function("+172 027-507-632"))  ## Output: 172
print(generated_function("+72 001-050-856"))  ## Output: 72
print(generated_function("+95 310-537-401"))  ## Output: 95
print(generated_function("+6 775-969-238"))  ## Output: 6

# End time: 2024-04-10 17:45:25.399341
# Elapsed time in seconds: 2.3793515500001376
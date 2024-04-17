# Start time: 2024-04-10 17:40:37.543027

'''
Prompt:
Given that input as ['+106 769-858-438'] output is 858, input as ['+83 973-757-831'] output is 757, input as ['+62 647-787-775'] output is 787, input as ['+172 027-507-632'] output is 507, input as ['+72 001-050-856'] output is 050, input as ['+95 310-537-401'] output is 537, input as ['+6 775-969-238'] output is 969, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        phone_number = input_str.split()[1]
        output = phone_number.split('-')[1]
        return output
    except IndexError:
        return "Invalid input format"

# Test cases
print(generated_function('+106 769-858-438'))  # Output: 858
print(generated_function('+83 973-757-831'))   # Output: 757
print(generated_function('+62 647-787-775'))   # Output: 787
print(generated_function('+172 027-507-632'))  # Output: 507
print(generated_function('+72 001-050-856'))   # Output: 050
print(generated_function('+95 310-537-401'))   # Output: 537
print(generated_function('+6 775-969-238'))    # Output: 969
print(generated_function("+106 769-858-438"))  ## Output: 858
print(generated_function("+83 973-757-831"))  ## Output: 757
print(generated_function("+62 647-787-775"))  ## Output: 787
print(generated_function("+172 027-507-632"))  ## Output: 507
print(generated_function("+72 001-050-856"))  ## Output: 050
print(generated_function("+95 310-537-401"))  ## Output: 537
print(generated_function("+6 775-969-238"))  ## Output: 969

# End time: 2024-04-10 17:40:39.935482
# Elapsed time in seconds: 2.392427127000019
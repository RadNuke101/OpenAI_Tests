# Start time: 2024-04-10 18:15:15.281004

'''
Prompt:
Given that input as ['+106 769-858-438'] output is 769, input as ['+83 973-757-831'] output is 973, input as ['+62 647-787-775'] output is 647, input as ['+172 027-507-632'] output is 027, input as ['+72 001-050-856'] output is 001, input as ['+95 310-537-401'] output is 310, input as ['+6 775-969-238'] output is 775, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        phone_number = input_str.split()[1]
        return phone_number.split('-')[0]
    except IndexError:
        return "Invalid input format"

# Test cases
print(generated_function('+106 769-858-438'))  # Output: 769
print(generated_function('+83 973-757-831'))    # Output: 973
print(generated_function('+62 647-787-775'))    # Output: 647
print(generated_function('+172 027-507-632'))   # Output: 027
print(generated_function('+72 001-050-856'))    # Output: 001
print(generated_function('+95 310-537-401'))    # Output: 310
print(generated_function('+6 775-969-238'))     # Output: 775
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+6 775-969-238"))  ## Output: 775

# End time: 2024-04-10 18:15:18.063319
# Elapsed time in seconds: 2.782265155999994
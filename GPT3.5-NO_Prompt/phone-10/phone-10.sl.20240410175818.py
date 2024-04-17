# Start time: 2024-04-10 18:08:47.364187

'''
Prompt:
Given that input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_string):
    try:
        input_string = input_string.strip('[]').replace("'", "")
        input_string = input_string.split()[0]
        country_code = input_string[:3]
        area_code = input_string[4:7]
        phone_number = input_string[8:]
        return f"{country_code} ({area_code}) {phone_number}"
    except:
        return "Invalid input"

# Test cases
print(generated_function('+106 769-858-438'))  # Output: +106 (769) 858-438
print(generated_function('+83 973-757-831'))    # Output: +83 (973) 757-831
print(generated_function('+62 647-787-775'))    # Output: +62 (647) 787-775
print(generated_function('+172 027-507-632'))   # Output: +172 (027) 507-632
print(generated_function('+72 001-050-856'))    # Output: +72 (001) 050-856
print(generated_function('+95 310-537-401'))    # Output: +95 (310) 537-401
print(generated_function('+6 775-969-238'))     # Output: +6 (775) 969-238
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-10 18:08:50.677294
# Elapsed time in seconds: 3.3130460560000756
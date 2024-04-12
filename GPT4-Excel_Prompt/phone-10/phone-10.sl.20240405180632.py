# Start time: 2024-04-05 18:38:12.040157

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return input with parentheses around the first three numbers before the first "-", and delete the first "-" and replace it with a space, and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    # Split the input string into parts before and after the first "-"
    parts = phone_number.split("-", 1)
    # Add parentheses around the first three numbers (area code) and replace the first "-" with a space
    formatted_number = parts[0] + ' (' + parts[1][:3] + ') ' + parts[1][3:]
    return formatted_number

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: +106 (769) 858-438
print(generated_function('+83 973-757-831'))   # Expected output: +83 (973) 757-831
print(generated_function('+62 647-787-775'))   # Expected output: +62 (647) 787-775
print(generated_function('+172 027-507-632'))  # Expected output: +172 (027) 507-632
print(generated_function('+72 001-050-856'))   # Expected output: +72 (001) 050-856
print(generated_function('+95 310-537-401'))   # Expected output: +95 (310) 537-401
print(generated_function('+6 775-969-238'))    # Expected output: +6 (775) 969-238
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-05 18:38:19.135800
# Elapsed time in seconds: 7.095505594001224
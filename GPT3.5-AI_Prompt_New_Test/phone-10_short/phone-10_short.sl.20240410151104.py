# Start time: 2024-04-10 15:32:53.258121

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: The input data consists of phone numbers with country codes and formatted in a specific way. The output data transforms the input phone numbers by adding parentheses around the area code. 

The relationship between the input and output is that the input data provides the full phone number with country code, while the output data formats the phone number by adding parentheses around the area code. This formatting change makes the phone numbers easier to read and understand, especially for individuals familiar with the standard phone number format. 

Overall, the transformation from input to output involves a simple formatting adjustment that enhances the readability and clarity of the phone numbers., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(phone_number):
    # Remove the '+' sign from the phone number
    phone_number = phone_number[1:]
    
    # Split the phone number into country code, area code, and local number
    country_code, area_code, local_number = phone_number.split()
    
    # Format the phone number with parentheses around the area code
    formatted_phone_number = f"+{country_code} ({area_code}) {local_number}"
    
    return formatted_phone_number

# Test cases
print(generated_function("+106 769-858-438"))
print(generated_function("+83 973-757-831"))
print(generated_function("+62 647-787-775"))
print(generated_function("+172 027-507-632"))
print(generated_function("+72 001-050-856"))
print(generated_function("+95 310-537-401"))
print(generated_function("+6 775-969-238"))
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-10 15:32:55.419922
# Elapsed time in seconds: 2.161759804000212


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238


print(generated_function("+172 050-856-001"))  ### Output: +172 (050) 856-001
print(generated_function("+83 787-775-647"))  ### Output: +83 (787) 775-647
print(generated_function("+72 537-401-310"))  ### Output: +72 (537) 401-310
print(generated_function("+106 757-831-973"))  ### Output: +106 (757) 831-973
print(generated_function("+62 507-632-027"))  ### Output: +62 (507) 632-027
print(generated_function("+95 969-238-775"))  ### Output: +95 (969) 238-775
print(generated_function("+6 858-438-769"))  ### Output: +6 (858) 438-769

# TEST SCRIPTS APPENDED!


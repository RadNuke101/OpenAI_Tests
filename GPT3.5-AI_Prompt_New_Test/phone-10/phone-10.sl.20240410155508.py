# Start time: 2024-04-10 16:15:58.727185

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers with country codes and formatted with dashes. Each entry starts with a country code followed by the phone number separated by dashes.

Summary for Output Column:
The output column data consists of phone numbers with country codes and formatted with parentheses for the area code. The format remains consistent with the input data, but the dashes are retained, and the area code is enclosed in parentheses.

Relationship between Input and Output:
The relationship between the input and output is that the country code remains the same in both, but the phone number format is slightly modified in the output. The area code in the phone number is enclosed in parentheses in the output, while the dashes are retained from the input. Overall, the output maintains the essential information from the input while presenting it in a slightly different format for clarity., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into country code and phone number
    country_code, phone_number = input_str.split(' ')[0], input_str.split(' ')[1]
    
    # Split the phone number into area code and the rest
    area_code, rest = phone_number.split('-')[0], '-'.join(phone_number.split('-')[1:])
    
    # Format the output with parentheses around the area code and dashes retained
    output_str = f"{country_code} ({area_code}) {rest}"
    
    return output_str

# Test cases
print(generated_function('+106 769-858-438'))
print(generated_function('+83 973-757-831'))
print(generated_function('+62 647-787-775'))
print(generated_function('+172 027-507-632'))
print(generated_function('+72 001-050-856'))
print(generated_function('+95 310-537-401'))
print(generated_function('+6 775-969-238'))
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-10 16:16:01.692385
# Elapsed time in seconds: 2.9651195719998213


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238


print(generated_function("+6 858-438-769"))  ### Output: +6 (858) 438-769
print(generated_function("+172 050-856-001"))  ### Output: +172 (050) 856-001
print(generated_function("+62 507-632-027"))  ### Output: +62 (507) 632-027
print(generated_function("+106 757-831-973"))  ### Output: +106 (757) 831-973
print(generated_function("+83 787-775-647"))  ### Output: +83 (787) 775-647
print(generated_function("+72 537-401-310"))  ### Output: +72 (537) 401-310
print(generated_function("+95 969-238-775"))  ### Output: +95 (969) 238-775

# TEST SCRIPTS APPENDED!


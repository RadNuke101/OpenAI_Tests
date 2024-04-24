# Start time: 2024-04-10 15:10:16.915022

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers with country codes. Each entry follows the format of '+XX YYY-ZZZ-ZZZ', where XX is the country code, YYY is the area code, and ZZZ-ZZZ is the phone number. The input data is qualitative and structured.

Summary for Output Column Data:
The output column data consists of formatted phone numbers with country codes enclosed in parentheses. Each entry follows the format of '+XX (YYY) ZZZ-ZZZ'. The output data is qualitative and structured.

Relationship between Input and Output:
The relationship between the input and output columns is that the output column transforms the input phone numbers by adding parentheses around the area code. The country code remains the same in both input and output. The output column enhances the readability and organization of the phone numbers provided in the input column., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Split the input string into country code, area code, and phone number
    country_code, area_code, phone_number = input_str.split()[0], input_str.split()[1].split('-')[0], input_str.split()[1].split('-')[1] + '-' + input_str.split()[1].split('-')[2]
    
    # Format the output phone number with parentheses around the area code
    output_str = f'{country_code} ({area_code}) {phone_number}'
    
    return output_str

# Test cases
test_input1 = '+106 769-858-438'
test_input2 = '+83 973-757-831'
test_input3 = '+62 647-787-775'
test_input4 = '+172 027-507-632'
test_input5 = '+72 001-050-856'
test_input6 = '+95 310-537-401'
test_input7 = '+6 775-969-238'

# Call the generated function with test inputs
output1 = generated_function(test_input1)
output2 = generated_function(test_input2)
output3 = generated_function(test_input3)
output4 = generated_function(test_input4)
output5 = generated_function(test_input5)
output6 = generated_function(test_input6)
output7 = generated_function(test_input7)
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-10 15:10:19.988112
# Elapsed time in seconds: 3.073016065000047


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


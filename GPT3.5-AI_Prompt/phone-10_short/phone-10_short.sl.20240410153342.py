# Start time: 2024-04-10 15:54:22.842692

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for input column data:
The input column data consists of phone numbers in the format '+XX YYY-ZZZ-ZZZ', where XX is the country code, YYY is the area code, and ZZZ-ZZZ is the phone number. Each input represents a unique phone number with different country codes.

Summary for output column data:
The output column data consists of formatted phone numbers in the format '+XX (YYY) ZZZ-ZZZ'. The output format includes the country code in the same format as input, but the area code is enclosed in parentheses and separated by a space from the phone number. The output column data is a formatted version of the input phone numbers.

Relationship between input and output:
The relationship between the input and output is that the output is a formatted version of the input phone numbers. The country code remains the same in both input and output, but the area code and phone number are formatted differently. The input provides the raw phone number, while the output provides a more visually appealing and standardized format for the phone number., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to format phone numbers
def generated_function(phone_number):
    # Split the input phone number into country code, area code, and phone number
    country_code = phone_number[1:phone_number.index(' ')]
    area_code = phone_number[phone_number.index(' ')+1:phone_number.index('-')]
    phone_num = phone_number[phone_number.index('-')+1:]
    
    # Format the phone number as per the output format
    formatted_number = f'+{country_code} ({area_code}) {phone_num}'
    
    return formatted_number

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

# End time: 2024-04-10 15:54:26.105857
# Elapsed time in seconds: 3.26307144600014
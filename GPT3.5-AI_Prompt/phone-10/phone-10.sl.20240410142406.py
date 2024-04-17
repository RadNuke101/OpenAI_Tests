# Start time: 2024-04-10 14:47:51.630986

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers with country codes and area codes separated by spaces and dashes. Each input follows the format of '+XX XXX-XXX-XXX', where X represents a digit. The country codes range from 2 to 3 digits, followed by the area code and the phone number separated by dashes.

Summary for Output Column Data:
The output column data consists of formatted phone numbers with country codes enclosed in parentheses and area codes separated by dashes. Each output follows the format of '+XX (XXX) XXX-XXX', where X represents a digit. The country codes are enclosed in parentheses, followed by the area code and the phone number separated by dashes.

Relationship between Input and Output:
The relationship between the input and output is that the input provides the raw phone number data with country codes, area codes, and phone numbers separated by spaces and dashes. The output transforms this raw data into a standardized format by enclosing the country code in parentheses and separating the area code and phone number with dashes. The output format enhances readability and consistency across different phone numbers., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(input_str):
    # Remove the brackets and split the input string into country code, area code, and phone number
    input_str = input_str.replace('[', '').replace(']', '')
    country_code, area_code, phone_number = input_str.split()[0][1:], input_str.split()[1].split('-')[0], input_str.split()[1].split('-')[1:]
    
    # Format the phone number with the specified format
    output = f'+{country_code} ({area_code}) {"-".join(phone_number)}'
    
    return output

# Test cases
print(generated_function('+106 769-858-438')) # Output: +106 (769) 858-438
print(generated_function('+83 973-757-831')) # Output: +83 (973) 757-831
print(generated_function('+62 647-787-775')) # Output: +62 (647) 787-775
print(generated_function('+172 027-507-632')) # Output: +172 (027) 507-632
print(generated_function('+72 001-050-856')) # Output: +72 (001) 050-856
print(generated_function('+95 310-537-401')) # Output: +95 (310) 537-401
print(generated_function('+6 775-969-238')) # Output: +6 (775) 969-238
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-10 14:47:55.618998
# Elapsed time in seconds: 3.9878951499999857
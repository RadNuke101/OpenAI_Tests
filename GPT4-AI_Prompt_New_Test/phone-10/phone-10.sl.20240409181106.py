# Start time: 2024-04-09 19:51:46.974686

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary

The input data consists of strings that represent phone numbers in an international format. Each string begins with a '+' sign followed by the country code, a space, and then the local number. The local number is divided into three parts by hyphens. The country code varies in length, ranging from one to three digits. The local number is consistently formatted with three groups of digits, but the number of digits within these groups can vary. The input data does not contain parentheses or any other formatting characters besides the '+' sign, space, and hyphens.

### Output Column Summary

The output data retains the same essential information as the input data but introduces a specific formatting change. The country code and the local number are still present, but the local number's format is altered for readability. The first part of the local number, previously separated by a space, is now enclosed in parentheses. The hyphens remain as separators for the latter two parts of the local number. This formatting change enhances the readability of the phone number, making it clearer where the area code ends and the local number begins. The '+' sign at the beginning and the overall sequence of digits remain unchanged.

### Relationship Summary

The transformation from the input to the output data involves a reformatting of the phone numbers to adhere to a common international phone number presentation style. The key changes include:

1. Enclosing the first part of the local number (the area code) in parentheses.
2. Retaining the country code, the '+' sign, and the overall sequence of digits without alteration.
3. Maintaining the use of hyphens to separate the latter two parts of the local number.

This transformation does not alter the numerical content or the order of the digits but improves the readability and standardizes the presentation of the phone numbers. The process respects the original data's integrity while making the numbers more accessible and visually structured for users., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    This function takes a phone number in international format as input and reformats it for readability.
    The first part of the local number is enclosed in parentheses, while the rest of the format is retained.
    
    :param phone_number: A string representing the phone number in international format.
    :return: A string representing the reformatted phone number.
    """
    # Split the input string into country code and local number parts
    parts = phone_number.split(' ', 1)
    country_code = parts[0]
    local_number = parts[1]
    
    # Split the local number into its three parts
    local_parts = local_number.split('-', 2)
    
    # Reformat the local number by enclosing the first part in parentheses
    reformatted_local_number = f"({local_parts[0]}) {local_parts[1]}-{local_parts[2]}"
    
    # Combine the country code and the reformatted local number
    reformatted_phone_number = f"{country_code} {reformatted_local_number}"
    
    return reformatted_phone_number

# Test cases
print(generated_function('+106 769-858-438'))  # Expected: +106 (769) 858-438
print(generated_function('+83 973-757-831'))   # Expected: +83 (973) 757-831
print(generated_function('+62 647-787-775'))   # Expected: +62 (647) 787-775
print(generated_function('+172 027-507-632'))  # Expected: +172 (027) 507-632
print(generated_function('+72 001-050-856'))   # Expected: +72 (001) 050-856
print(generated_function('+95 310-537-401'))   # Expected: +95 (310) 537-401
print(generated_function('+6 775-969-238'))    # Expected: +6 (775) 969-238
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-09 19:52:05.848859
# Elapsed time in seconds: 18.87381603099857


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


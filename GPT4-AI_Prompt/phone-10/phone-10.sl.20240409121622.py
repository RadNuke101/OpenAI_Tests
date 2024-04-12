# Start time: 2024-04-09 14:21:40.810223

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings representing phone numbers in an international format. Each string begins with a '+' sign, followed by a country code of one to three digits. After the country code, there is a space, and then the rest of the phone number is presented in a three-part format separated by hyphens. The first part, presumably the area code or a similar regional identifier, consists of three digits. The second and third parts of the phone number, likely representing the local number, are also three digits each. The input data uniformly follows this pattern, indicating a structured approach to representing international phone numbers.

### Output Column Summary:

The output data retains the same essential information as the input data but presents it in a slightly modified format that emphasizes the segmentation of the phone number. The '+' sign and country code remain unchanged, but the space following the country code is replaced with a space and parentheses around the first part of the phone number (the area code or regional identifier). The rest of the phone number follows the parentheses, maintaining the hyphen-separated format for the local number parts. This transformation suggests a standardization or localization of the phone number format, possibly making it more readable or aligning it with a specific formatting preference.

### Relationship Summary:

The transformation from the input to the output data involves a consistent reformatting of the phone numbers. The key changes include:

1. Enclosing the first part of the phone number (after the country code) in parentheses. This part is likely interpreted as an area code or a similar regional identifier.
2. Removing the space that originally followed the country code and replacing it with the parentheses that now enclose the first part of the phone number. 

These changes do not alter the essential information contained within each phone number but rather adjust the presentation for clarity, readability, or adherence to a specific formatting standard. The relationship between the input and output data is purely structural, with no alterations to the numerical content of the phone numbers. This process highlights a standardization practice that could be useful for databases, communication platforms, or any system that requires a uniform phone number format for international numbers., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    This function takes a phone number in the format '+<country_code> <area_code>-<part1>-<part2>'
    and reformats it to '+<country_code> (<area_code>) <part1>-<part2>'.
    
    :param phone_number: A string representing the phone number in international format.
    :return: A string representing the reformatted phone number.
    """
    # Splitting the input string into components based on space and hyphen
    parts = phone_number.split(' ')
    country_code = parts[0]
    rest = parts[1].split('-')
    
    # Reformatting the phone number
    reformatted_number = f"{country_code} ({rest[0]}) {rest[1]}-{rest[2]}"
    
    return reformatted_number

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

# End time: 2024-04-09 14:21:56.107555
# Elapsed time in seconds: 15.29687894900053
# Start time: 2024-04-09 16:23:27.191191

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of strings representing phone numbers in an international format. Each entry begins with a country code prefixed with a plus sign (+), followed by a space, and then the local part of the number which is divided into three groups by hyphens (-). The country codes vary in length, ranging from one to three digits. The local part of the number is consistently formatted as three groups of digits: the first group contains three digits, followed by two groups of three digits each, separated by hyphens. This format is consistent across all entries, indicating a structured approach to representing international phone numbers, albeit with a variation in the length of the country code.

### Output Column Summary:

The output data transforms the input phone numbers into a slightly different format. The transformation involves reformatting the local part of the number by enclosing the first group of digits (the area code) in parentheses and removing the space between the country code and the area code. The rest of the number remains unchanged, maintaining the two groups of three digits each, separated by a hyphen. This output format still adheres to international phone number conventions but emphasizes the area code by enclosing it in parentheses, which is a common formatting style in various countries. The consistency in the transformation across all entries suggests a standardized process for reformatting the input data to this specific output style.

### Relationship Between Input and Output:

The relationship between the input and output data lies in the systematic transformation of the format of international phone numbers. The transformation rules are applied uniformly across all entries, indicating a clear, defined process. The primary changes from input to output are:

1. **Enclosing the Area Code**: The first group of digits after the country code, representing the area code, is enclosed in parentheses in the output. This highlights the area code and is a common formatting preference in many regions.
   
2. **Removing the Space**: The space between the country code and the area code is removed in the output, creating a more compact representation of the phone number.

These transformations do not alter the essential components of the phone numbers but rather adjust their presentation for clarity, emphasis, or adherence to specific formatting preferences. The process respects the integrity of the original data while making subtle changes to its presentation., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms the input phone number from international format to a slightly different format
    by enclosing the area code in parentheses and removing the space between the country code
    and the area code.
    
    :param phone_number: A string representing a phone number in international format.
    :return: A string representing the transformed phone number.
    """
    # Split the input string into country code and the rest of the number
    parts = phone_number.split(' ', 1)
    country_code = parts[0]
    local_number = parts[1]
    
    # Split the local number into its components (area code and the rest)
    local_parts = local_number.split('-', 1)
    area_code = local_parts[0]
    rest_of_number = local_parts[1]
    
    # Format the output string as per the new requirements
    output_number = f"{country_code}({area_code})-{rest_of_number}"
    
    return output_number

# Test cases
print(generated_function('+106 769-858-438'))  # Expected: +106(769)-858-438
print(generated_function('+83 973-757-831'))   # Expected: +83(973)-757-831
print(generated_function('+62 647-787-775'))   # Expected: +62(647)-787-775
print(generated_function('+172 027-507-632'))  # Expected: +172(027)-507-632
print(generated_function('+72 001-050-856'))   # Expected: +72(001)-050-856
print(generated_function('+95 310-537-401'))   # Expected: +95(310)-537-401
print(generated_function('+6 775-969-238'))    # Expected: +6(775)-969-238
print(generated_function("+106 769-858-438"))  ## Output: +106 (769) 858-438
print(generated_function("+83 973-757-831"))  ## Output: +83 (973) 757-831
print(generated_function("+62 647-787-775"))  ## Output: +62 (647) 787-775
print(generated_function("+172 027-507-632"))  ## Output: +172 (027) 507-632
print(generated_function("+72 001-050-856"))  ## Output: +72 (001) 050-856
print(generated_function("+95 310-537-401"))  ## Output: +95 (310) 537-401
print(generated_function("+6 775-969-238"))  ## Output: +6 (775) 969-238

# End time: 2024-04-09 16:23:41.840327
# Elapsed time in seconds: 14.64902835400062


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


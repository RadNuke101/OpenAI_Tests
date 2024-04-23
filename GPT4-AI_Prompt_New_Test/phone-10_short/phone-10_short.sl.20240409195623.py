# Start time: 2024-04-09 21:41:35.012281

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input data consists of a series of strings that represent phone numbers in an international format. Each string begins with a plus sign (+) followed by a country code of one to three digits. After the country code, there is a space, and then the rest of the phone number is presented in three groups separated by hyphens. The first group after the country code typically contains three digits, which is followed by two more groups of three digits each. The input data showcases a variety of country codes, indicating a diverse set of international phone numbers. The format is consistent across the dataset, adhering to a "+country code XXX-XXX-XXX" structure, although the number of digits in the country code varies.

### Summary of Output Column Data:

The output data retains the same essential information as the input data but presents it in a slightly modified format that emphasizes the area code. The format changes to "+country code (XXX) XXX-XXX", where the first group of three digits after the country code is enclosed in parentheses to denote the area code. This format is commonly used in various countries to highlight the area code distinctly from the rest of the phone number. The transformation from the input to the output format involves adding parentheses around the first group of digits after the country code and ensuring the rest of the number remains unchanged. The output data maintains the international nature of the phone numbers and the diversity in country codes, with the primary alteration being the addition of parentheses for clarity and emphasis on the area code.

### Relationship Between Input and Output:

The transformation from the input to the output data involves a reformatting of the phone numbers to highlight the area code more prominently. The essential components of the phone numbers, including the country code and the sequence of digits, remain unchanged. The key difference is the stylistic change where the first group of digits following the country code is enclosed in parentheses in the output data. This alteration does not affect the numerical or qualitative value of the phone numbers but serves to make the area code stand out for easier identification. The relationship between the input and output data is a direct mapping that applies a consistent formatting rule across all entries, demonstrating a clear and systematic approach to enhancing the readability and presentation of international phone numbers., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms an international phone number from the format "+country code XXX-XXX-XXX"
    to the format "+country code (XXX) XXX-XXX" to emphasize the area code.
    
    :param phone_number: A string representing the phone number in international format.
    :return: A string representing the transformed phone number with the area code in parentheses.
    """
    # Split the phone number into parts: country code and the rest
    parts = phone_number.split(' ')
    country_code = parts[0]
    rest_of_number = parts[1]
    
    # Split the rest of the number into its components
    number_parts = rest_of_number.split('-')
    
    # Reformat the phone number to include parentheses around the area code
    reformatted_number = f"{country_code} ({number_parts[0]}) {number_parts[1]}-{number_parts[2]}"
    
    return reformatted_number

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

# End time: 2024-04-09 21:41:50.686265
# Elapsed time in seconds: 15.673842573000002


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


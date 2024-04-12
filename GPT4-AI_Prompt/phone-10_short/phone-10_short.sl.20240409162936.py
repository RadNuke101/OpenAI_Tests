# Start time: 2024-04-09 18:06:45.978389

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings that represent phone numbers in an international format. Each string begins with a '+' sign, followed by a country code of one to three digits, a space, and then a local number divided into three groups by hyphens. The first group after the country code consists of three digits, followed by two groups of three digits each. The format of the input data can be summarized as follows:

- Starts with a '+' sign.
- Followed by a 1 to 3 digit country code.
- A space separator.
- A local number divided into a pattern of 3-3-3 digits, separated by hyphens.

### Output Column Summary:

The output data transforms the format of the input phone numbers into a slightly different presentation while retaining all original information. The transformation involves:

- Keeping the '+' sign and the country code unchanged.
- Enclosing the first group of the local number (previously directly after the country code and space) within parentheses.
- Retaining the hyphen-separated format for the remaining two groups of the local number.

The output format can be summarized as follows:

- Starts with a '+' sign.
- Followed by the country code.
- The first group of the local number enclosed in parentheses.
- The remaining two groups of the local number separated by hyphens, as in the input.

### Relationship Summary:

The transformation from the input to the output format involves a reformatting of the phone numbers to enhance readability and possibly conform to a standardized presentation. The key steps in this transformation include:

- Maintaining the integrity of the country code and the '+' sign, indicating that the international dialing format is preserved.
- The introduction of parentheses around the first group of the local number, which is a common practice in various formatting styles to highlight the area or city code within the local number.
- The rest of the local number format remains unchanged, with the two groups of three digits each still separated by hyphens.

This transformation does not alter the numerical content of the phone numbers but changes their presentation to possibly align with specific formatting preferences or standards., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms the input phone number from international format to a slightly different presentation.
    
    Parameters:
    phone_number (str): A string representing a phone number in international format.
    
    Returns:
    str: The transformed phone number with the first group of the local number enclosed in parentheses.
    """
    # Splitting the input string into components: country code and local number
    parts = phone_number.split(' ')
    country_code = parts[0]
    local_number_parts = parts[1].split('-')
    
    # Reformatting the local number with the first group enclosed in parentheses
    new_local_number = f"({local_number_parts[0]}) {local_number_parts[1]}-{local_number_parts[2]}"
    
    # Combining the country code and the new local number format
    new_phone_number = f"{country_code} {new_local_number}"
    
    return new_phone_number

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

# End time: 2024-04-09 18:07:01.346655
# Elapsed time in seconds: 15.367808604001766
# Start time: 2024-04-09 16:23:56.680675

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings representing phone numbers in a specific format. Each string begins with a plus sign (+) followed by a country code of one to three digits. After the country code, there is a space, followed by a sequence of digits divided into three groups by hyphens. The first group after the country code contains three digits, the second group also contains three digits, and the third group contains three digits, making it a consistent pattern across all entries. The country codes vary in length and value, indicating that the phone numbers belong to different countries. The format of these strings is consistent, following the pattern: `+[Country Code] [XXX-XXX-XXX]`.

### Output Column Summary:

The output data transforms the format of the input phone numbers into a slightly different presentation while retaining all original information. The transformation involves reformatting the spacing and punctuation around the area code (the first group of three digits following the country code). Specifically, the area code is enclosed in parentheses, and the space that originally followed the country code is removed. Therefore, the output format is: `+[Country Code] ([Area Code]) XXX-XXX`, maintaining the original country code, area code, and the remaining digits of the phone number. This format is more commonly used in various contexts, possibly making the numbers easier to read or aligning with a standard presentation format for phone numbers in certain regions or systems.

### Relationship Summary:

The transformation from the input to the output format represents a standardization process for phone numbers, where the primary change is the inclusion of parentheses around the area code. This alteration does not change the essential information contained within each phone number but modifies its presentation for consistency, readability, or compliance with a specific formatting standard. The process respects the original country code and the sequence of digits, ensuring that the transformation is purely cosmetic and does not alter the phone number's functionality. This kind of transformation is typical in data processing tasks where uniformity in data presentation is required for documentation, databases, or communication systems., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms the input phone number from the format +[Country Code] [XXX-XXX-XXX]
    to the format +[Country Code] ([Area Code]) XXX-XXX.
    
    Parameters:
    phone_number (str): A string representing the phone number in the specified input format.
    
    Returns:
    str: The phone number transformed into the specified output format.
    """
    # Split the input string into components: country code, area code, and the rest
    parts = phone_number.split(" ")
    country_code = parts[0]
    rest = parts[1].split("-")
    area_code = rest[0]
    remaining = "-".join(rest[1:])
    
    # Format the output string according to the specified output format
    formatted_number = f"{country_code} ({area_code}) {remaining}"
    
    return formatted_number

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

# End time: 2024-04-09 16:24:09.789986
# Elapsed time in seconds: 13.109212281999135


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


# Start time: 2024-04-09 18:07:16.717142

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings representing phone numbers in an international format. Each string begins with a '+' sign, followed by a country code of one to three digits, a space, and then a local number divided into three groups by hyphens. The first group after the country code consists of three digits, followed by two groups of three digits each. The structure of these strings suggests they represent phone numbers from various countries, indicated by the varying lengths of the country codes (ranging from one to three digits). The consistent use of the '+' sign indicates an international dialing format. The data is qualitative, representing a standardized way to write phone numbers across different regions.

### Output Column Summary:

The output data transforms the input phone numbers into a slightly different format that maintains the original information while altering its presentation. The transformation involves:
1. Keeping the country code and the '+' sign unchanged.
2. Enclosing the first group of digits (the area code) after the country code in parentheses.
3. Retaining the last two groups of digits in their original form but separated by a hyphen.

This format is also commonly used in international communication, making the numbers easily recognizable while providing a clear distinction between the country code, area code, and the local number. The output retains the qualitative nature of the input data, focusing on the presentation of phone numbers in a format that might be preferred for clarity in certain contexts, such as written communication or databases.

### Relationship Summary:

The transformation from the input to the output column represents a standardized formatting change applied to international phone numbers. The essence of the data remains unchanged; the operation merely alters the presentation for potentially enhanced readability or to conform to a specific style guide. This process highlights the importance of consistent formatting in data management and communication, ensuring that phone numbers are presented in a universally understandable manner regardless of the original input format. The relationship between the input and output data underscores the adaptability of data presentation to meet various requirements or preferences without altering the underlying qualitative information., and input as ['+106 769-858-438'] output is +106 (769) 858-438, input as ['+83 973-757-831'] output is +83 (973) 757-831, input as ['+62 647-787-775'] output is +62 (647) 787-775, input as ['+172 027-507-632'] output is +172 (027) 507-632, input as ['+72 001-050-856'] output is +72 (001) 050-856, input as ['+95 310-537-401'] output is +95 (310) 537-401, input as ['+6 775-969-238'] output is +6 (775) 969-238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms an international phone number into a slightly different format.
    
    Parameters:
    phone_number (str): A string representing a phone number in international format.
    
    Returns:
    str: The transformed phone number.
    """
    # Splitting the input string into components based on spaces and hyphens
    parts = phone_number.split(' ')
    country_code = parts[0]  # Extracting the country code
    local_parts = parts[1].split('-')  # Splitting the local number into parts
    
    # Reformatting the phone number
    formatted_number = f"{country_code} ({local_parts[0]}) {local_parts[1]}-{local_parts[2]}"
    
    return formatted_number

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

# End time: 2024-04-09 18:07:28.786793
# Elapsed time in seconds: 12.07246244399721
# Start time: 2024-04-09 14:10:58.471161

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings that represent phone numbers in an international format. Each string begins with a '+' sign, followed by the country code, a space, and then the phone number itself divided into three parts by hyphens. The country codes vary in length, ranging from one to three digits. The phone numbers are consistently formatted, following the pattern of three groups of digits separated by hyphens. The first group after the country code contains three digits, and the subsequent two groups contain three and six digits, respectively. The input data represents a qualitative attribute, specifically the international phone numbers formatted in a standardized way.

### Summary of Output Column Data

The output data consists of integers that represent the country codes extracted from the input data. These country codes range from one to three digits, reflecting the diversity in the length of country codes worldwide. The output data is directly derived from the input data, specifically by isolating the country code part of the phone numbers. This transformation from the input to the output strips away the rest of the phone number, focusing solely on the country code as the significant piece of information.

### Relationship Between Input and Output

The relationship between the input and output data is a direct extraction process where the output is a subset of the input. Specifically, the output isolates and presents the country code part of the input phone numbers. This process involves identifying the '+' sign and the space that follows the country code in the input, then extracting the digits in between as the output. The transformation from input to output simplifies the data from a full phone number in an international format to just the country code, indicating the origin (in terms of country) of the phone number. This relationship highlights a focus on geographical identification over individual or specific phone number identification., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from a given phone number in international format.
    
    Parameters:
    phone_number (str): A string representing a phone number in international format.
    
    Returns:
    int: The country code extracted from the phone number.
    """
    # Find the index of the space character to determine the end of the country code
    space_index = phone_number.find(' ')
    # Extract the country code, which is between the '+' sign and the space
    country_code = phone_number[1:space_index]
    # Convert the country code to an integer and return it
    return int(country_code)

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: 106
print(generated_function('+83 973-757-831'))   # Expected output: 83
print(generated_function('+62 647-787-775'))   # Expected output: 62
print(generated_function('+172 027-507-632'))  # Expected output: 172
print(generated_function('+72 001-050-856'))   # Expected output: 72
print(generated_function('+95 310-537-401'))   # Expected output: 95
print(generated_function('+6 775-969-238'))    # Expected output: 6
print(generated_function("+106 769-858-438"))  ## Output: 106
print(generated_function("+83 973-757-831"))  ## Output: 83
print(generated_function("+62 647-787-775"))  ## Output: 62
print(generated_function("+172 027-507-632"))  ## Output: 172
print(generated_function("+72 001-050-856"))  ## Output: 72
print(generated_function("+95 310-537-401"))  ## Output: 95
print(generated_function("+6 775-969-238"))  ## Output: 6

# End time: 2024-04-09 14:11:12.356463
# Elapsed time in seconds: 13.884886408000057


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: 106
print(generated_function("+83 973-757-831"))  ## Output: 83
print(generated_function("+62 647-787-775"))  ## Output: 62
print(generated_function("+172 027-507-632"))  ## Output: 172
print(generated_function("+72 001-050-856"))  ## Output: 72
print(generated_function("+95 310-537-401"))  ## Output: 95
print(generated_function("+6 775-969-238"))  ## Output: 6


print(generated_function("+106 973-757-831"))  ### Output: 106
print(generated_function("+6 769-858-438"))  ### Output: 6
print(generated_function("+83 647-787-775"))  ### Output: 83
print(generated_function("+72 310-537-401"))  ### Output: 72
print(generated_function("+172 001-050-856"))  ### Output: 172
print(generated_function("+62 027-507-632"))  ### Output: 62
print(generated_function("+95 775-969-238"))  ### Output: 95

# TEST SCRIPTS APPENDED!


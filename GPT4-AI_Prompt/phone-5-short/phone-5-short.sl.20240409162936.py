# Start time: 2024-04-09 18:01:05.801690

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings that represent phone numbers in an international format. Each string begins with a plus sign (+), followed by the country code, a space, and then the phone number itself which is divided into three groups by hyphens. The country codes vary in length, ranging from one to three digits, indicating that the dataset includes phone numbers from various countries around the world. The rest of the number, following the country code, seems to be formatted consistently across the dataset, divided into three segments by hyphens, though the actual numbers vary. The input data is qualitative in nature, representing categorical information (country codes) and structured identifiers (phone numbers).

### Summary of Output Column Data

The output data consists of integers that represent the country codes extracted from the input strings. These country codes range from one to three digits, reflecting the diversity of the countries represented in the input data. The output is a direct extraction from the input, specifically isolating the first component (country code) of the structured phone number format. This output is qualitative as well, despite being represented by numbers, because it categorizes the phone numbers by their country of origin rather than quantifying any particular attribute.

### Relationship Between Input and Output

The relationship between the input and output data is a direct extraction process where the output is derived by isolating the country code from the input phone number string. The output effectively categorizes the input data by country, providing a simplified, categorical view of the diverse set of international phone numbers. This process transforms a detailed, structured identifier (the full phone number) into a simpler categorical variable (the country code), facilitating analysis or organization of the data based on the geographical origin of the phone numbers. The transformation from input to output strips away the specific details of the phone numbers, focusing solely on the country code to highlight the geographical distribution of the numbers in the dataset., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from a given phone number string in international format.
    
    Parameters:
    phone_number (str): A phone number in international format starting with '+'.
    
    Returns:
    int: The country code extracted from the phone number.
    """
    # Split the phone number string to isolate the country code
    parts = phone_number.split(' ')
    # The country code is the first part after the '+', remove the '+' and convert to integer
    country_code = int(parts[0][1:])
    return country_code

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

# End time: 2024-04-09 18:01:16.146388
# Elapsed time in seconds: 10.344393964001938
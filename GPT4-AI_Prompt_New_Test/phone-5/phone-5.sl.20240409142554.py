# Start time: 2024-04-09 16:14:37.066377

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings that represent phone numbers in an international format. Each string begins with a plus sign (+) followed by the country code, a space, and then the phone number itself which is divided into three groups by hyphens. The country codes vary in length, ranging from one to three digits. The phone numbers after the country code are consistently formatted with three groups of digits, although the number of digits in each group can vary. The input data represents a qualitative categorization of phone numbers by their country codes, which serves as an identifier for the geographical or regional origin of the phone number.

### Summary of Output Column Data

The output data extracts and presents the country code from each phone number in the input data as a standalone integer. This transformation from the input to the output strips away the rest of the phone number, focusing solely on the country code. The output data, therefore, represents a distilled, qualitative categorization of the input data, emphasizing the geographical or regional identifier inherent in each phone number. The output values range from single to triple-digit integers, reflecting the diversity of country codes worldwide.

### Relationship Between Input and Output

The relationship between the input and output data is a direct extraction and simplification process, where the output isolates and highlights the country code from the full phone number provided in the input. This process transforms a detailed piece of qualitative data (the full phone number) into a more abstract, yet still qualitative, representation (the country code). The country code serves as a key identifier, allowing for the classification or grouping of phone numbers by region without the need for the complete number. This transformation underscores the significance of the country code as a primary piece of information within the broader context of international phone numbers, facilitating analyses or operations that are concerned with geographical or regional categorizations rather than individual phone number details., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from a given phone number in international format.
    
    Parameters:
    phone_number (str): A phone number in international format starting with '+'.
    
    Returns:
    int: The country code extracted from the phone number.
    """
    # Split the phone number by space to separate the country code
    parts = phone_number.split(' ')
    # The country code is the first part, remove the '+' and convert to integer
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

# End time: 2024-04-09 16:14:47.516319
# Elapsed time in seconds: 10.44986513799995


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


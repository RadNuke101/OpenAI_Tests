# Start time: 2024-04-09 21:33:42.543766

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings representing phone numbers in an international format. Each string begins with a plus sign (+) followed by the country code, a space, and then the phone number itself which is divided into three groups by hyphens. The country codes vary in length, ranging from one to three digits. The phone numbers following the country code are consistently formatted with three groups of digits, although the number of digits within these groups can vary slightly. The input data represents a qualitative categorization of phone numbers by their country codes, indicating the origin or the regional association of each phone number.

### Summary of Output Column Data

The output data extracts and isolates the country code from each phone number in the input data. These country codes are integers ranging from one to three digits. The output serves as a qualitative identifier, categorizing each phone number by its country of origin or regional association based on the country code. The output simplifies the input data by focusing solely on the country code, disregarding the rest of the phone number.

### Relationship Between Input and Output

The relationship between the input and output data is a process of extraction and simplification. The output is derived directly from the input by isolating the first segment of each phone number—the country code—immediately following the plus sign. This process transforms a detailed and specific piece of information (the full phone number) into a more general categorization (the country code), making it easier to understand the regional origin of each number without the need to process the entire phone number. The transformation from input to output effectively reduces the qualitative data from a detailed individual identifier (a specific phone number) to a broader category of origin (country code), which can be useful for analyses that require understanding or categorizing phone numbers by region rather than by individual lines., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from a phone number string formatted in international format.
    
    Args:
    - phone_number (str): A string representing a phone number in international format.
    
    Returns:
    - str: The country code extracted from the phone number.
    """
    # Split the phone number string to isolate the country code
    parts = phone_number.split(" ")
    # The country code is the first part after the plus sign, remove the plus sign
    country_code = parts[0][1:]
    
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

# End time: 2024-04-09 21:33:51.455571
# Elapsed time in seconds: 8.91173017500114


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


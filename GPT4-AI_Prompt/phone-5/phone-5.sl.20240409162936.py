# Start time: 2024-04-09 17:58:36.600971

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Data

The input data consists of strings that represent phone numbers in an international format. Each string begins with a plus sign (+) followed by the country code, a space, and then the phone number itself which is divided into three groups by hyphens. The country codes vary in length, ranging from one to three digits. The format of the phone numbers after the country code is consistent, with three groups of digits separated by hyphens. The first group after the country code contains three digits, and the subsequent two groups contain three and six digits respectively, making the format look like this: `+<country code> <XXX-XXX-XXX>`.

### Summary of Output Data

The output data extracts and presents the country code from each input string as an integer. The country code is the sequence of digits immediately following the plus sign and preceding the first space in each input string. These country codes range from one to three digits, indicating the geographical area or country the phone number is associated with. The extraction process disregards the rest of the phone number, focusing solely on the country code.

### Relationship Between Input and Output

The relationship between the input and output data is a direct extraction process where the output is derived by isolating the country code from the input string. The output ignores all parts of the phone number except for the country code, which is identified as the sequence of digits following the initial plus sign and ending before the first space in the input string. This process treats the input data qualitatively, focusing on the structure and format of the input strings to extract the desired numerical country codes. The transformation from input to output does not involve any quantitative manipulation of the numbers themselves but rather a parsing of the string to identify and extract the relevant portion (the country code) as the output., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from a given phone number string in international format.
    
    Args:
    - phone_number (str): A phone number in the format +<country code> <XXX-XXX-XXX>
    
    Returns:
    - int: The country code extracted from the phone number.
    """
    # Find the index of the first space to isolate the country code
    space_index = phone_number.find(' ')
    # Extract the country code, which is between the plus sign and the first space
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

# End time: 2024-04-09 17:58:51.931616
# Elapsed time in seconds: 15.3301972320005
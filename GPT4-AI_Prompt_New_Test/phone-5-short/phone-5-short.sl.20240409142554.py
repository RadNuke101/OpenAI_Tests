# Start time: 2024-04-09 16:17:04.008525

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings representing phone numbers with an international dialing format. Each string begins with a plus sign (+) followed by the country code, a space, and then the phone number itself, which is divided into three groups by hyphens. The country codes vary in length, ranging from one to three digits. The phone numbers are consistent in their format, following the structure of three groups of digits, but the number of digits within these groups can vary slightly. The input data represents a qualitative aspect, focusing on the structure and pattern of international phone numbers rather than the numerical value of the digits themselves.

### Summary of Output Column Data

The output data consists of integers extracted from the input data, specifically the country codes from the international phone numbers. These country codes range from one to three digits and are integral in identifying the origin country of the phone number. The output data is qualitative in nature, as it categorizes the phone numbers by their country codes, providing a method to classify or group the phone numbers based on their geographical origin.

### Relationship Between Input and Output

The relationship between the input and output data is direct and functional. The output is derived from the input by extracting the country code portion of the international phone number. This process involves identifying the plus sign (+) at the beginning of the string, capturing the digits that immediately follow until a space is encountered, and then converting this substring into an integer. The country code serves as a key identifier that links each phone number to its country of origin, making it a crucial piece of information for categorizing or analyzing the phone numbers based on geographical criteria. This relationship underscores the importance of the country code in international communication systems, providing a systematic way to understand and organize phone numbers from around the world., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from an international phone number string.

    Parameters:
    phone_number (str): A string representing a phone number in international format.

    Returns:
    int: The country code extracted from the phone number.
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

# End time: 2024-04-09 16:17:14.360173
# Elapsed time in seconds: 10.351575147000403


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: 106
print(generated_function("+83 973-757-831"))  ## Output: 83
print(generated_function("+62 647-787-775"))  ## Output: 62
print(generated_function("+172 027-507-632"))  ## Output: 172
print(generated_function("+72 001-050-856"))  ## Output: 72
print(generated_function("+95 310-537-401"))  ## Output: 95
print(generated_function("+6 775-969-238"))  ## Output: 6


print(generated_function("+83 647-787-775"))  ### Output: 83
print(generated_function("+6 769-858-438"))  ### Output: 6
print(generated_function("+62 027-507-632"))  ### Output: 62
print(generated_function("+172 001-050-856"))  ### Output: 172
print(generated_function("+72 310-537-401"))  ### Output: 72
print(generated_function("+95 775-969-238"))  ### Output: 95
print(generated_function("+106 973-757-831"))  ### Output: 106

# TEST SCRIPTS APPENDED!


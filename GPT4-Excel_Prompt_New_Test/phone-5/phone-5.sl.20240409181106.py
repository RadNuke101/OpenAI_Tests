# Start time: 2024-04-09 19:41:56.429635

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input data consists of strings that represent phone numbers in an international format. Each string begins with a plus sign (+) followed by the country code, a space, and then the phone number itself divided into three groups by hyphens. The country codes vary in length, ranging from one to three digits. The phone numbers following the country code are consistently formatted but vary in their specific digits. The input data represents a qualitative attribute, specifically the format and structure of international phone numbers, with the focus on the variation in country codes.

### Summary of Output Column Data:

The output data extracts and presents the country code from each input string as an integer. This transformation from the input to the output isolates the initial segment of the input data (the country code) and discards the rest of the phone number. The output data, therefore, provides a qualitative overview of the diversity of country codes present in the input data, ranging from single-digit to triple-digit codes.

### Relationship Between Input and Output:

The relationship between the input and output data is a direct extraction process where the output is a specific component (the country code) of the input data (the international phone number). The output simplifies the input by removing the phone number's local part and retaining only the country code, which is a key identifier in the international dialing format. This process highlights the variation in country codes while discarding the individual phone number details, focusing on the geographical or regional aspect represented by the country code. The transformation from input to output underscores the importance of the country code in categorizing or identifying the origin of the phone number within the dataset., and input as ['+106 769-858-438'] output is 106, input as ['+83 973-757-831'] output is 83, input as ['+62 647-787-775'] output is 62, input as ['+172 027-507-632'] output is 172, input as ['+72 001-050-856'] output is 72, input as ['+95 310-537-401'] output is 95, input as ['+6 775-969-238'] output is 6, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Extracts the country code from an international phone number string.

    Parameters:
    phone_number (str): A string representing a phone number in international format.

    Returns:
    int: The country code extracted from the phone number.
    """
    # Split the phone number string to isolate the country code
    parts = phone_number.split(' ')
    # The country code is the first part, excluding the plus sign
    country_code = parts[0][1:]
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

# End time: 2024-04-09 19:42:09.507597
# Elapsed time in seconds: 13.077717546999338


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


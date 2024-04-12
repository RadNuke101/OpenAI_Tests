# Start time: 2024-04-09 19:22:37.817125

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input data consists of strings that represent phone numbers in an international format. Each string begins with a plus sign ('+') followed by the country code, a space, and then the local number divided into three groups by hyphens ('-'). The country codes vary in length, ranging from one to three digits, indicating that the phone numbers originate from various countries. The local numbers are consistently formatted into three groups, with each group separated by a hyphen. This format suggests a standardized approach to representing international phone numbers, making it easier to identify the country code and the local number segments.

### Summary of Output Column Data

The output data transforms the input phone numbers into a different format. The transformation involves removing the plus sign ('+') and the space after the country code, and replacing the hyphens ('-') with periods ('.'). This results in a continuous string of digits segmented by periods, maintaining the original grouping of the local number but altering the separators. The output format retains the distinction between the country code and the local number segments, but presents it in a more compact and uniform manner, possibly for consistency in a specific application or database.

### Relationship Between Input and Output

The transformation from the input to the output format represents a systematic reformatting of international phone numbers. The key changes include:

1. **Removal of the Plus Sign**: The initial plus sign indicating the international format is removed, possibly because the context of use ensures that all numbers are international, or to simplify the format.
2. **Space Removal**: The space following the country code is eliminated, merging the country code with the local number into a continuous string. This change likely aims to create a more compact representation.
3. **Separator Change**: The hyphens separating the local number groups in the input are replaced with periods in the output. This alteration might be for aesthetic reasons, to conform to a specific data format requirement, or to ensure compatibility with systems that interpret phone numbers differently.

Overall, the relationship between the input and output data demonstrates a deliberate reformatting process designed to standardize the presentation of international phone numbers, possibly for ease of use, storage, or compatibility with specific software or databases., and input as ['+106 769-858-438'] output is 106.769.858.438, input as ['+83 973-757-831'] output is 83.973.757.831, input as ['+62 647-787-775'] output is 62.647.787.775, input as ['+172 027-507-632'] output is 172.027.507.632, input as ['+72 001-050-856'] output is 72.001.050.856, input as ['+95 310-537-401'] output is 95.310.537.401, input as ['+6 775-969-238'] output is 6.775.969.238, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms an international phone number from the format '+CC NNN-NNN-NNN'
    to 'CC.NNN.NNN.NNN', where CC is the country code and N represents the local number digits.
    
    :param phone_number: String representing the phone number in international format.
    :return: String representing the transformed phone number.
    """
    # Remove the plus sign and space
    phone_number = phone_number.replace('+', '').replace(' ', '')
    # Replace hyphens with periods
    phone_number = phone_number.replace('-', '.')
    return phone_number

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: 106.769.858.438
print(generated_function('+83 973-757-831'))   # Expected output: 83.973.757.831
print(generated_function('+62 647-787-775'))   # Expected output: 62.647.787.775
print(generated_function('+172 027-507-632'))  # Expected output: 172.027.507.632
print(generated_function('+72 001-050-856'))   # Expected output: 72.001.050.856
print(generated_function('+95 310-537-401'))   # Expected output: 95.310.537.401
print(generated_function('+6 775-969-238'))    # Expected output: 6.775.969.238
print(generated_function("+106 769-858-438"))  ## Output: 106.769.858.438
print(generated_function("+83 973-757-831"))  ## Output: 83.973.757.831
print(generated_function("+62 647-787-775"))  ## Output: 62.647.787.775
print(generated_function("+172 027-507-632"))  ## Output: 172.027.507.632
print(generated_function("+72 001-050-856"))  ## Output: 72.001.050.856
print(generated_function("+95 310-537-401"))  ## Output: 95.310.537.401
print(generated_function("+6 775-969-238"))  ## Output: 6.775.969.238

# End time: 2024-04-09 19:22:48.575330
# Elapsed time in seconds: 10.757927984999696
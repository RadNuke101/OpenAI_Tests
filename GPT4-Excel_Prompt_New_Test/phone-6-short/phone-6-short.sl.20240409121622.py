# Start time: 2024-04-09 13:16:39.371827

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of strings that follow a specific format: a plus sign (+) followed by a country code, a space, and a phone number separated into three groups by hyphens. The country code varies in length, ranging from one to three digits. The phone number is consistently divided into three groups, with the first group immediately following the space after the country code. This first group of the phone number is what appears to be extracted for the output.

### Output Column Summary:

The output data consists of the first group of digits from the phone number part of the input string. These outputs are always three digits long, except in cases where the leading digit(s) of the first group is zero, in which case the output retains the leading zero(s). This suggests that the output is treated as a string rather than a numerical value, preserving any leading zeros.

### Relationship Summary:

The relationship between the input and output data is a straightforward extraction process focused on a specific part of the input string. The output is always the first group of digits from the phone number portion of the input, immediately following the country code and space. This extraction ignores the country code and the rest of the phone number, focusing solely on the initial segment of the phone number. The process treats the data qualitatively, as it preserves the formatting of the extracted segment, including any leading zeros, indicating that the output is not intended for numerical analysis but rather for identification or categorization purposes based on the initial segment of the phone numbers., and input as ['+106 769-858-438'] output is 769, input as ['+83 973-757-831'] output is 973, input as ['+62 647-787-775'] output is 647, input as ['+172 027-507-632'] output is 027, input as ['+72 001-050-856'] output is 001, input as ['+95 310-537-401'] output is 310, input as ['+6 775-969-238'] output is 775, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    # Extract the first group of digits from the phone number part of the input string
    return phone_number.split(' ')[1].split('-')[0]

# Test cases
print(generated_function('+106 769-858-438'))  # Expected output: 769
print(generated_function('+83 973-757-831'))   # Expected output: 973
print(generated_function('+62 647-787-775'))   # Expected output: 647
print(generated_function('+172 027-507-632'))  # Expected output: 027
print(generated_function('+72 001-050-856'))   # Expected output: 001
print(generated_function('+95 310-537-401'))   # Expected output: 310
print(generated_function('+6 775-969-238'))    # Expected output: 775
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+6 775-969-238"))  ## Output: 775

# End time: 2024-04-09 13:16:50.843312
# Elapsed time in seconds: 11.471275630000036


# APPEND TEST SCRIPTS...
print(generated_function("+106 769-858-438"))  ## Output: 769
print(generated_function("+83 973-757-831"))  ## Output: 973
print(generated_function("+62 647-787-775"))  ## Output: 647
print(generated_function("+172 027-507-632"))  ## Output: 027
print(generated_function("+72 001-050-856"))  ## Output: 001
print(generated_function("+95 310-537-401"))  ## Output: 310
print(generated_function("+6 775-969-238"))  ## Output: 775


print(generated_function("+106 858-769-438"))  ### Output: 858
print(generated_function("+83 757-973-831"))  ### Output: 757
print(generated_function("+72 050-001-856"))  ### Output: 050
print(generated_function("+172 507-027-632"))  ### Output: 507
print(generated_function("+95 537-310-401"))  ### Output: 537
print(generated_function("+62 787-647-775"))  ### Output: 787
print(generated_function("+6 969-775-238"))  ### Output: 969

# TEST SCRIPTS APPENDED!


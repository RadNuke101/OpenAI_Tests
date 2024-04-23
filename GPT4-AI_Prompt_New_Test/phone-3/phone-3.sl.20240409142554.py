# Start time: 2024-04-09 14:40:47.020374

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings formatted as phone numbers without parentheses around the area code. Each string is structured in a consistent "NNN-NNN-NNN" format, where "N" represents a digit from 0 to 9. The data does not provide any geographical or personal information directly; it simply follows a uniform pattern that resembles North American phone number formatting. The input data is qualitative, representing a specific way of writing phone numbers.

### Output Column Summary:

The output data transforms the format of the input phone numbers by incorporating parentheses around the first three digits (the area code) and maintaining the hyphen between the next three digits (the central office code) and the last four digits (the line number). The transformation results in a format that is commonly used in various contexts, such as business, personal, and official communications. The output format is "(NNN) NNN-NNN", which is more visually segmented and may be perceived as easier to read. This format is also qualitative, as it represents a standardized way of presenting phone numbers.

### Relationship Summary:

The relationship between the input and output data is a systematic transformation of the format in which phone numbers are presented. The transformation involves adding parentheses around the area code (the first three digits) of the phone number while keeping the rest of the number's structure unchanged. This process does not alter the numerical content of the phone numbers but changes their visual and textual representation. The transformation is consistent across all data points, indicating a rule-based approach to formatting phone numbers from a more linear "NNN-NNN-NNN" format to a segmented "(NNN) NNN-NNN" format. This change enhances the readability and standardization of phone numbers, aligning with common formatting practices in various communication settings., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms a phone number from 'NNN-NNN-NNN' format to '(NNN) NNN-NNN' format.

    Parameters:
    phone_number (str): A string representing a phone number in 'NNN-NNN-NNN' format.

    Returns:
    str: The phone number transformed to '(NNN) NNN-NNN' format.
    """
    # Split the phone number into its components
    area_code, central_office_code, line_number = phone_number.split('-')
    # Format and return the transformed phone number
    return f"({area_code}) {central_office_code}-{line_number}"

# Test cases
print(generated_function('938-242-504'))  # Expected output: (938) 242-504
print(generated_function('308-916-545'))  # Expected output: (308) 916-545
print(generated_function('623-599-749'))  # Expected output: (623) 599-749
print(generated_function('981-424-843'))  # Expected output: (981) 424-843
print(generated_function('118-980-214'))  # Expected output: (118) 980-214
print(generated_function('244-655-094'))  # Expected output: (244) 655-094
print(generated_function('830-941-991'))  # Expected output: (830) 941-991
print(generated_function("938-242-504"))  ## Output: (938) 242-504
print(generated_function("308-916-545"))  ## Output: (308) 916-545
print(generated_function("623-599-749"))  ## Output: (623) 599-749
print(generated_function("981-424-843"))  ## Output: (981) 424-843
print(generated_function("118-980-214"))  ## Output: (118) 980-214
print(generated_function("244-655-094"))  ## Output: (244) 655-094
print(generated_function("830-941-991"))  ## Output: (830) 941-991

# End time: 2024-04-09 14:40:58.401677
# Elapsed time in seconds: 11.381257903000005


# APPEND TEST SCRIPTS...
print(generated_function("938-242-504"))  ## Output: (938) 242-504
print(generated_function("308-916-545"))  ## Output: (308) 916-545
print(generated_function("623-599-749"))  ## Output: (623) 599-749
print(generated_function("981-424-843"))  ## Output: (981) 424-843
print(generated_function("118-980-214"))  ## Output: (118) 980-214
print(generated_function("244-655-094"))  ## Output: (244) 655-094
print(generated_function("830-941-991"))  ## Output: (830) 941-991


print(generated_function("599-623-749"))  ### Output: (599) 623-749
print(generated_function("242-938-504"))  ### Output: (242) 938-504
print(generated_function("424-981-843"))  ### Output: (424) 981-843
print(generated_function("980-118-214"))  ### Output: (980) 118-214
print(generated_function("655-244-094"))  ### Output: (655) 244-094
print(generated_function("941-830-991"))  ### Output: (941) 830-991
print(generated_function("916-308-545"))  ### Output: (916) 308-545

# TEST SCRIPTS APPENDED!


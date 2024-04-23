# Start time: 2024-04-09 16:47:44.395476

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings formatted as phone numbers without parentheses around the area code and with hyphens separating the three distinct parts of the phone numbers. Each string is structured as follows: a three-digit area code, followed by a three-digit central office code, and ending with a four-digit station number, all separated by hyphens (e.g., "XXX-XXX-XXXX"). The data appears to represent a standardized format for representing telephone numbers in a specific, yet unidentified, region or country. Each entry in the input column is unique, suggesting a diverse dataset without repetitions.

### Output Column Summary:

The output data transforms the format of the input telephone numbers by incorporating parentheses around the area code and maintaining the hyphen between the central office code and the station number. The transformation results in a format commonly used in various regions, particularly in the United States, to denote telephone numbers. The output format is "(XXX) XXX-XXXX", which enhances readability and conforms to a widely recognized standard for representing phone numbers. Like the input, each output entry is unique, indicating that the transformation process preserves the uniqueness of each telephone number.

### Relationship Summary:

The relationship between the input and output columns is a systematic format transformation of telephone numbers. The process involves:

1. Enclosing the area code (the first three digits) in parentheses.
2. Retaining the original hyphen that separates the central office code and the station number.
3. Preserving the integrity and uniqueness of each telephone number during the transformation.

This transformation does not alter the numerical part of the telephone numbers but changes their presentation to adhere to a specific formatting convention. The process is consistent across all entries, indicating a rule-based approach to formatting telephone numbers from a less formal representation to a more standardized one. This transformation is purely stylistic and does not affect the qualitative nature of the data, which remains a series of unique telephone numbers before and after the process., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms a phone number from 'XXX-XXX-XXXX' format to '(XXX) XXX-XXXX' format.

    Parameters:
    phone_number (str): A string representing a phone number in 'XXX-XXX-XXXX' format.

    Returns:
    str: The phone number transformed into '(XXX) XXX-XXXX' format.
    """
    # Split the phone number into its components based on the hyphen separator
    parts = phone_number.split('-')
    # Reformat the phone number by enclosing the area code in parentheses
    # and joining the parts with the appropriate separators
    formatted_number = f"({parts[0]}) {parts[1]}-{parts[2]}"
    return formatted_number

# Test cases
print(generated_function('938-242-504'))
print(generated_function('308-916-545'))
print(generated_function('623-599-749'))
print(generated_function('981-424-843'))
print(generated_function('118-980-214'))
print(generated_function('244-655-094'))
print(generated_function('830-941-991'))
print(generated_function("938-242-504"))  ## Output: (938) 242-504
print(generated_function("308-916-545"))  ## Output: (308) 916-545
print(generated_function("623-599-749"))  ## Output: (623) 599-749
print(generated_function("981-424-843"))  ## Output: (981) 424-843
print(generated_function("118-980-214"))  ## Output: (118) 980-214
print(generated_function("244-655-094"))  ## Output: (244) 655-094
print(generated_function("830-941-991"))  ## Output: (830) 941-991

# End time: 2024-04-09 16:47:52.160855
# Elapsed time in seconds: 7.765262911001628


# APPEND TEST SCRIPTS...
print(generated_function("938-242-504"))  ## Output: (938) 242-504
print(generated_function("308-916-545"))  ## Output: (308) 916-545
print(generated_function("623-599-749"))  ## Output: (623) 599-749
print(generated_function("981-424-843"))  ## Output: (981) 424-843
print(generated_function("118-980-214"))  ## Output: (118) 980-214
print(generated_function("244-655-094"))  ## Output: (244) 655-094
print(generated_function("830-941-991"))  ## Output: (830) 941-991


print(generated_function("980-118-214"))  ### Output: (980) 118-214
print(generated_function("655-244-094"))  ### Output: (655) 244-094
print(generated_function("242-938-504"))  ### Output: (242) 938-504
print(generated_function("916-308-545"))  ### Output: (916) 308-545
print(generated_function("599-623-749"))  ### Output: (599) 623-749
print(generated_function("424-981-843"))  ### Output: (424) 981-843
print(generated_function("941-830-991"))  ### Output: (941) 830-991

# TEST SCRIPTS APPENDED!


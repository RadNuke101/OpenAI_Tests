# Start time: 2024-04-09 12:30:27.040749

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings, each representing a phone number in a specific format. The format observed is 'NNN-NNN-NNN', where 'N' stands for a digit from 0 to 9. Each string is a unique combination of digits separated into three groups by hyphens. The groups are structured as follows: the first group contains three digits, the second group also contains three digits, and the third group contains three digits. This format is consistent across all entries in the input column, indicating a standardized way of representing phone numbers before transformation.

### Output Column Summary:

The output data retains the same numerical content as the input data but alters the format in which these numbers are presented. The transformation observed is from 'NNN-NNN-NNN' to '(NNN) NNN-NNN'. This means that the first group of three digits from the input is enclosed within parentheses, and the remaining two groups of digits are presented in the same order, separated by a hyphen. This format is a common way of representing phone numbers in several contexts, suggesting that the transformation aims to conform to a widely recognized phone number format.

### Relationship Summary:

The transformation from the input to the output column demonstrates a straightforward formatting change that does not alter the numerical content of the data. The process involves:

1. Enclosing the first group of three digits in parentheses.
2. Retaining the hyphen between the second and third groups of digits.
3. Keeping the digits within each group unchanged.

This transformation suggests a standardization process aimed at making the phone numbers more readable or conforming to a specific style often used in formal communications, databases, or user interfaces. The relationship between the input and output is purely cosmetic and does not involve any change in the actual numbers, indicating a focus on presentation rather than on the data itself., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms a phone number from 'NNN-NNN-NNN' format to '(NNN) NNN-NNN' format.
    
    :param phone_number: A string representing a phone number in 'NNN-NNN-NNN' format.
    :return: A string representing the phone number in '(NNN) NNN-NNN' format.
    """
    # Split the phone number into three groups using the hyphen as a separator
    parts = phone_number.split('-')
    # Reformat the phone number by enclosing the first group in parentheses
    # and joining the three groups with the appropriate separators
    formatted_number = f"({parts[0]}) {parts[1]}-{parts[2]}"
    return formatted_number

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

# End time: 2024-04-09 12:30:49.699847
# Elapsed time in seconds: 22.658637570999986


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


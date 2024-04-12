# Start time: 2024-04-09 12:40:26.374240

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input data consists of a series of strings, each representing a phone number in a specific format. The format used is a sequence of three groups of digits separated by hyphens, following the pattern `XXX-XXX-XXX`. Each group of digits varies, but they all conform to this structural pattern. The data is qualitative in nature, representing a standardized way of writing phone numbers. Each string is unique, indicating a distinct phone number within the dataset. The input data does not contain any additional information about the origin, geographical location, or the owner of these phone numbers.

### Summary of Output Column Data:

The output data transforms the format of the phone numbers from the input data. The transformation involves reformatting the structure from `XXX-XXX-XXX` to `(XXX) XXX-XXX`. This change involves enclosing the first group of digits in parentheses and maintaining the hyphen between the second and third groups of digits. The output retains the original digits from the input without altering them, ensuring that the identity of the phone numbers remains unchanged. The output format is commonly used in various contexts, suggesting a more standardized or formal representation of phone numbers.

### Relationship Between Input and Output:

The relationship between the input and output data is a systematic transformation of the format of phone numbers. The process involves reformatting the presentation of the numbers without altering the digits themselves. This transformation is consistent across all data points, indicating a rule-based approach to converting phone number formats. The change from a hyphenated separation to a combination of parentheses and hyphens in the output makes the phone numbers appear in a format that is widely recognized and possibly preferred in certain contexts, such as in business communications or official documents. The transformation does not infer or add any new information about the phone numbers but rather changes their visual presentation to adhere to a different stylistic standard., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms the format of a phone number from 'XXX-XXX-XXX' to '(XXX) XXX-XXX'.
    
    Parameters:
    phone_number (str): The phone number in 'XXX-XXX-XXX' format.
    
    Returns:
    str: The phone number in '(XXX) XXX-XXX' format.
    """
    # Split the input phone number by hyphens
    parts = phone_number.split('-')
    # Reformat the phone number to the desired output format
    transformed_phone_number = f"({parts[0]}) {parts[1]}-{parts[2]}"
    return transformed_phone_number

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

# End time: 2024-04-09 12:40:39.277849
# Elapsed time in seconds: 12.90326925799991
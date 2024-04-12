# Start time: 2024-04-09 18:22:04.097557

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input data consists of a series of strings that represent phone numbers in a specific format. Each string is structured as three groups of digits separated by hyphens. The first group contains three digits, the second group also contains three digits, and the third group contains three digits, following the pattern `XXX-XXX-XXX`. These strings do not contain any alphabetic characters or special symbols other than the hyphens used to separate the digit groups. The data appears to represent a standardized way of writing phone numbers, albeit not in the conventional format used for displaying such numbers in certain contexts, such as within parentheses or with different separators.

### Summary of Output Column Data:

The output data transforms the format of the input phone numbers into a different, yet also standardized, representation. In the output, each phone number is reformatted to follow the pattern `(XXX) XXX-XXX`. This involves enclosing the first group of three digits in parentheses, maintaining the hyphen between the second and third groups of digits, and removing the hyphen that originally separated the first and second groups of digits in the input. This output format is commonly used in various contexts, including business and personal communication, to present phone numbers in a clear and easily readable manner.

### Relationship Between Input and Output:

The transformation from the input to the output data represents a reformatting process that changes the visual presentation of phone numbers from one conventional style to another. The essence of the phone number—the digits themselves—remains unchanged. The process involves:

1. Enclosing the first group of digits in parentheses to highlight the area code or initial segment of the phone number, which is a common practice in many regions.
2. Removing the hyphen that originally separated the first and second groups of digits, which simplifies the visual separation of the number into its component parts.
3. Maintaining the hyphen between the second and third groups of digits, preserving a familiar element of the original format that helps in reading and understanding the number.

This transformation does not alter the numerical content of the phone numbers but rather adapts their format to meet different stylistic or regional preferences for displaying such numbers. It's a qualitative adjustment aimed at enhancing readability and conforming to widely recognized standards for presenting phone numbers in written form., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
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
    reformatted_number = f"({parts[0]}) {parts[1]}-{parts[2]}"
    
    return reformatted_number

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

# End time: 2024-04-09 18:22:14.299296
# Elapsed time in seconds: 10.201512093000929
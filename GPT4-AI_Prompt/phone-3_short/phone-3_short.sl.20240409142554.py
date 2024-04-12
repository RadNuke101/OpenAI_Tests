# Start time: 2024-04-09 14:49:06.335293

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input data consists of a series of strings formatted as phone numbers without parentheses around the area code. Each string is structured in a consistent format: three digits, followed by a hyphen, another set of three digits, another hyphen, and finally, a set of three digits. This pattern is consistent across all entries in the input column. The numbers range from 000-000-000 to 999-999-999 theoretically, but the provided dataset includes a variety of numbers without any apparent numerical sequence or pattern. The data is qualitative in nature, representing phone numbers in a specific format.

### Summary of Output Column Data:

The output data transforms the format of the input phone numbers into a different presentation style. Each output string takes the original phone number and encloses the first three digits (the area code) in parentheses, followed by a space, and then the rest of the number in the same sequence as the input (three digits, a hyphen, three digits). This transformation is consistent across all entries, indicating a systematic approach to reformatting the phone numbers from the input format to the output format. The output retains the qualitative nature of the data, focusing on the presentation style of phone numbers.

### Relationship Between Input and Output:

The relationship between the input and output data is a straightforward transformation of the format in which phone numbers are presented. The core data (the digits themselves) remains unchanged; only the presentation style is altered. The transformation involves:

1. Enclosing the first three digits (area code) of each phone number in parentheses.
2. Adding a space after the closing parenthesis.
3. Retaining the rest of the number in its original sequence.

This process suggests a standardization or normalization of phone number formats, possibly for aesthetic reasons or to adhere to a commonly accepted way of presenting phone numbers in certain contexts (e.g., in the United States). The transformation does not alter the qualitative nature of the data but enhances its readability and possibly its usability in contexts where this format is preferred or required., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms the format of a given phone number from 'XXX-XXX-XXX' to '(XXX) XXX-XXX'.
    
    Parameters:
    phone_number (str): The phone number in 'XXX-XXX-XXX' format.
    
    Returns:
    str: The phone number in '(XXX) XXX-XXX' format.
    """
    # Extract the area code and the rest of the number
    area_code = phone_number[:3]
    rest_of_number = phone_number[4:]
    
    # Format and return the new phone number
    return f"({area_code}) {rest_of_number}"

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

# End time: 2024-04-09 14:49:19.752317
# Elapsed time in seconds: 13.416969736999818
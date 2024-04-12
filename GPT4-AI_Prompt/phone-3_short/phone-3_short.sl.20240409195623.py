# Start time: 2024-04-09 20:15:37.906327

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings formatted as phone numbers without parentheses around the area code, following the pattern `NNN-NNN-NNN` where `N` represents a digit from 0 to 9. Each string is a unique combination of digits separated into three groups by hyphens: the first group of three digits, presumably the area code; the second group of three digits, which could be considered the central office or exchange code; and the last group of four digits, representing the line number. The data is qualitative, representing a standardized format for telephone numbers in many countries, particularly in the United States.

### Output Column Summary:

The output data transforms the format of the input telephone numbers by enclosing the first group of digits (the area code) in parentheses and maintaining the rest of the formatting intact. Thus, the output follows the pattern `(NNN) NNN-NNN`, where `N` again represents a digit from 0 to 9. This transformation adheres to another common formatting style for telephone numbers, particularly in contexts where the area code is highlighted or differentiated from the rest of the number. Like the input, the output data is qualitative, emphasizing a specific presentation style for telephone numbers.

### Relationship Summary:

The transformation from the input to the output column represents a reformatting process that changes the visual presentation of telephone numbers from one common style to another. Specifically, the process involves:

1. Identifying the first group of three digits (the area code) in the input.
2. Enclosing this group of digits in parentheses to highlight or differentiate the area code.
3. Retaining the original separation of the remaining digits with a hyphen, without altering the digit sequence itself.

This transformation does not alter the qualitative nature of the data but changes its format to suit different stylistic or regional preferences for displaying telephone numbers. The relationship between the input and output data is a direct, rule-based conversion that consistently applies to all entries in the dataset., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms a phone number from the format NNN-NNN-NNN to (NNN) NNN-NNN.

    Parameters:
    phone_number (str): The phone number in the format NNN-NNN-NNN.

    Returns:
    str: The phone number in the format (NNN) NNN-NNN.
    """
    # Split the input string into three parts based on the hyphen
    parts = phone_number.split('-')
    # Reformat the phone number by enclosing the area code in parentheses
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

# End time: 2024-04-09 20:15:47.761084
# Elapsed time in seconds: 9.854569639999681
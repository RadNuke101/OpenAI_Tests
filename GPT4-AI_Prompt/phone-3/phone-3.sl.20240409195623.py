# Start time: 2024-04-09 20:08:17.721778

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input data consists of a series of strings, each representing a phone number in a specific format. The format used is a sequence of three groups of digits separated by hyphens. Each string follows the pattern `XXX-XXX-XXX`, where `X` represents a digit from 0 to 9. The data is qualitative, representing phone numbers as a specific arrangement of digits and symbols without implying any numerical calculations or comparisons between them. Each entry is unique, indicating a diverse set of phone numbers without any apparent repetition or pattern in the choice of digits.

### Summary of Output Column Data:

The output data transforms the format of the input phone numbers into a new pattern. The transformation involves reformatting the string from `XXX-XXX-XXX` to `(XXX) XXX-XXX`. This involves enclosing the first group of three digits in parentheses and preserving the rest of the format as is, with a space inserted after the closing parenthesis. Like the input, the output is qualitative, focusing on the representation of phone numbers in a different visual arrangement. Each output entry corresponds directly to an input entry, maintaining the uniqueness and diversity of the dataset.

### Relationship Between Input and Output:

The relationship between the input and output data is a systematic transformation of the format in which phone numbers are presented. The process does not alter the digits themselves but changes how they are grouped and separated. This transformation is consistent across all entries, indicating a rule-based approach to reformatting phone numbers from one standard presentation to another. The purpose of such a transformation could be to adhere to a different stylistic or regional preference for displaying phone numbers, enhancing readability, or meeting specific formatting requirements. The data remains qualitative, with the transformation focusing solely on the visual arrangement of the digits and symbols that constitute a phone number., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms the format of a phone number from 'XXX-XXX-XXX' to '(XXX) XXX-XXX'.
    
    Parameters:
    phone_number (str): A string representing a phone number in the format 'XXX-XXX-XXX'.
    
    Returns:
    str: The phone number transformed into the format '(XXX) XXX-XXX'.
    """
    # Split the input string using '-' as the delimiter
    parts = phone_number.split('-')
    
    # Reformat the parts into the new pattern and return
    return f"({parts[0]}) {parts[1]}-{parts[2]}"

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

# End time: 2024-04-09 20:08:29.193586
# Elapsed time in seconds: 11.471550490998197
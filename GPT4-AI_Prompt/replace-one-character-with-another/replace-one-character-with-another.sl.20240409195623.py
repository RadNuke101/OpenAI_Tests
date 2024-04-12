# Start time: 2024-04-09 20:49:01.434175

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary

The input data consists of strings representing phone numbers in a specific format. Each string is a sequence of digits divided into three groups by spaces. The first group contains three digits, the second group also contains three digits, and the third group contains four digits. This format is consistent across all input data. The input data is qualitative, representing phone numbers as a sequence of characters rather than numerical values. The format suggests a standard North American phone number structure without the country code.

### Output Column Summary

The output data transforms the format of the phone numbers provided in the input. Each phone number is reformatted by replacing the spaces between the digit groups with hyphens. The output retains the three-part division of the original phone numbers: the first part with three digits, the second part with three digits, and the third part with four digits. This transformation results in a format that is commonly used for displaying phone numbers, making them easier to read and recognize. The output data, like the input, is qualitative, focusing on the representation of phone numbers.

### Relationship Summary

The relationship between the input and output data is a systematic transformation of the format in which phone numbers are presented. The transformation involves changing the separators between the digit groups of the phone numbers from spaces in the input to hyphens in the output. This change does not alter the sequence of digits or the grouping pattern; it only modifies the visual and textual representation of the phone numbers. The process is consistent across all data points, indicating a rule-based conversion that can be applied universally to any phone number presented in the input format. This transformation enhances the readability and standardization of phone numbers for contexts where the hyphen-separated format is preferred or required., and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    This function takes a phone number in the format 'XXX XXX XXXX' and converts it to 'XXX-XXX-XXXX'.
    
    :param phone_number: A string representing a phone number in the format 'XXX XXX XXXX'
    :return: A string representing the phone number in the format 'XXX-XXX-XXXX'
    """
    # Replace spaces with hyphens to transform the format
    return phone_number.replace(" ", "-")

# Test cases
print(generated_function('801 456 8756'))  # Expected output: 801-456-8756
print(generated_function('978 456 8756'))  # Expected output: 978-456-8756
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-09 20:49:07.480271
# Elapsed time in seconds: 6.045855290998588
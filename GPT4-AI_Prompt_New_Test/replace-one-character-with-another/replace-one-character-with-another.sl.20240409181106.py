# Start time: 2024-04-09 18:58:09.265539

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data

The input column consists of strings that represent phone numbers in a specific format. Each string is a sequence of digits divided into three groups by spaces. The first group contains three digits, the second group also contains three digits, and the third group contains four digits. This format follows the common North American Numbering Plan (NANP) format but uses spaces instead of dashes or other separators. The data is qualitative, representing a specific category of information (phone numbers) rather than numerical values for calculation. Each entry in the input column is unique but follows the same structural pattern.

### Summary of Output Column Data

The output column data transforms the format of the phone numbers from the input column. Each phone number retains the same sequence of digits but changes the separators from spaces to dashes. The output format is more conventional for displaying phone numbers in the United States, following the standard "XXX-XXX-XXXX" pattern. This transformation does not alter the qualitative nature of the data; it remains a representation of phone numbers. The output maintains the uniqueness of each entry, ensuring that the transformation is consistent across all data points.

### Relationship Between Input and Output

The relationship between the input and output columns is a direct format transformation of phone numbers from one conventional representation to another. The input data, which uses spaces to separate the digit groups in phone numbers, is systematically converted into a format that uses dashes for separation in the output data. This transformation does not alter the underlying data (the phone numbers themselves) but changes how they are presented. The process is consistent and applies the same transformation rule to all entries, ensuring that the qualitative nature of the data—its identity as phone numbers—is preserved while enhancing readability and standardization according to common formatting preferences., and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    This function takes a phone number in the format 'XXX XXX XXXX'
    and converts it to the format 'XXX-XXX-XXXX'.
    
    :param phone_number: A string representing a phone number in the format 'XXX XXX XXXX'
    :return: A string representing the phone number in the format 'XXX-XXX-XXXX'
    """
    # Replace spaces with dashes to transform the format
    return phone_number.replace(" ", "-")

# Test cases
print(generated_function('801 456 8756'))  # Expected output: 801-456-8756
print(generated_function('978 456 8756'))  # Expected output: 978-456-8756
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-09 18:58:15.001149
# Elapsed time in seconds: 5.735495007997088


# APPEND TEST SCRIPTS...
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756


print(generated_function("456 801 8756"))  ### Output: 456-801-8756
print(generated_function("456 978 8756"))  ### Output: 456-978-8756

# TEST SCRIPTS APPENDED!


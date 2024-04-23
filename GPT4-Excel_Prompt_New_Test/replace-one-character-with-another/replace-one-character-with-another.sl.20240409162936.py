# Start time: 2024-04-09 17:17:41.101249

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing strings that represent phone numbers in a specific format. Each entry in this column is a string that appears to follow a consistent structure: three groups of digits separated by spaces. The first group contains three digits, the second group also contains three digits, and the third group contains four digits. This format is consistent across all entries, suggesting that the data represents standard North American phone numbers without the country code. The input data is qualitative, representing a specific type of information (phone numbers) rather than numerical values to be calculated or analyzed statistically.

### Output Column Summary:

The output data, like the input, consists of a single column containing strings. However, the format of these strings has been altered slightly: instead of spaces, hyphens are used to separate the groups of digits. The structure remains the same with the first group containing three digits, the second group containing three digits, and the third group containing four digits. This transformation suggests a standardization or normalization process applied to the input data, converting it into a more commonly used or preferred phone number format. The output data retains its qualitative nature, representing phone numbers in a slightly different, yet consistent, format.

### Relationship Summary:

The relationship between the input and output columns is a straightforward transformation of format within the data representing phone numbers. The transformation involves replacing the spaces between the digit groups in the input data with hyphens in the output data. This change does not alter the qualitative nature of the data or the information it represents but standardizes the format to possibly align with common conventions or requirements for displaying or using phone numbers. The process suggests a focus on data cleaning or formatting for consistency, usability, or compliance with specific standards. This transformation is consistent across all entries, indicating a rule-based approach to data processing without exceptions or conditional alterations., and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    This function takes a phone number in the format 'XXX XXX XXXX' and converts it to 'XXX-XXX-XXXX'.
    
    :param phone_number: A string representing a phone number in the format 'XXX XXX XXXX'
    :return: A string representing the phone number in the format 'XXX-XXX-XXXX'
    """
    # Replace spaces with hyphens to transform the format
    formatted_number = phone_number.replace(" ", "-")
    return formatted_number

# Test cases
# Note: The output of these test cases is not included as per the instructions.
formatted_number1 = generated_function('801 456 8756')
formatted_number2 = generated_function('978 456 8756')
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-09 17:17:48.252309
# Elapsed time in seconds: 7.14462996599832


# APPEND TEST SCRIPTS...
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756


print(generated_function("456 801 8756"))  ### Output: 456-801-8756
print(generated_function("456 978 8756"))  ### Output: 456-978-8756

# TEST SCRIPTS APPENDED!


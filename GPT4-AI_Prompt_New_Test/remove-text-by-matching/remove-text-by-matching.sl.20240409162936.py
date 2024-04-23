# Start time: 2024-04-09 16:58:25.379729

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a single column containing strings that represent phone numbers in a standard North American format. Each entry in this column follows the pattern of a three-digit area code, followed by a hyphen, a three-digit central office code, followed by another hyphen, and finally a four-digit station number (e.g., 'XXX-XXX-XXXX'). The data is qualitative, representing categorical information rather than numerical values. The format is consistent across all entries, indicating a structured approach to data collection or entry. The presence of hyphens suggests that the data was formatted for readability or to adhere to a common standard of phone number representation.

### Output Column Summary:

The output data consists of a single column containing strings that represent the transformation of the input phone numbers into a continuous sequence of digits without any separators (e.g., 'XXXXXXXXXX'). This transformation results in a uniform, ten-digit numerical string for each entry. Despite the output appearing as numerical data, it retains its qualitative nature since it represents phone numbers, which are categorical identifiers rather than quantities or values that can be mathematically manipulated. The transformation process removes formatting elements (hyphens) without altering the order or content of the original digits, ensuring that the essential information—the phone number itself—remains intact and identifiable.

### Relationship Between Input and Output:

The relationship between the input and output columns is defined by a systematic transformation process that converts formatted phone numbers into a simplified, unformatted string of digits. This process involves removing the hyphens that separate the different parts of the phone number in the input data, resulting in a continuous string of digits in the output. The transformation preserves the sequence and integrity of the original digits, ensuring that the output remains a direct, albeit differently formatted, representation of the input. This process can be seen as a form of data normalization, where the goal is to standardize the format of the phone numbers for purposes that may include easier storage, comparison, or further processing. The relationship underscores a methodical approach to data manipulation, where the qualitative nature of the data is maintained while its presentation is simplified., and input as ['801-345-1987'] output is 8013451987, input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    This function takes a phone number in the format 'XXX-XXX-XXXX' and
    returns a continuous string of digits 'XXXXXXXXXX'.
    
    :param phone_number: A string representing a formatted phone number.
    :return: A string representing the unformatted phone number.
    """
    # Remove hyphens from the phone number to get a continuous string of digits
    return phone_number.replace('-', '')

# Test cases
print(generated_function('801-345-1987'))  # Expected output: 8013451987
print(generated_function('612-554-2000'))  # Expected output: 6125542000
print(generated_function("801-345-1987"))  ## Output: 8013451987
print(generated_function("612-554-2000"))  ## Output: 6125542000

# End time: 2024-04-09 16:58:41.260835
# Elapsed time in seconds: 15.880864906997886


# APPEND TEST SCRIPTS...
print(generated_function("801-345-1987"))  ## Output: 8013451987
print(generated_function("612-554-2000"))  ## Output: 6125542000


print(generated_function("345-801-1987"))  ### Output: 3458011987
print(generated_function("554-612-2000"))  ### Output: 5546122000

# TEST SCRIPTS APPENDED!


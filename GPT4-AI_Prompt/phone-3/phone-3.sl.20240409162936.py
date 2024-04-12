# Start time: 2024-04-09 16:40:58.948769

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Input Column Summary:

The input data consists of a series of strings formatted as phone numbers without parentheses around the area code and separated by hyphens. Each string is structured in a consistent "NNN-NNN-NNN" format, where "N" represents a digit from 0 to 9. The input data represents a collection of phone numbers, each with a three-digit area code, followed by a three-digit central office code, and ending with a four-digit station number. The input data does not include any country codes or international dialing prefixes, suggesting that these numbers could be assumed to be domestic (within a single country) or follow a specific national format.

### Output Column Summary:

The output data transforms the format of the input phone numbers by enclosing the area code (the first three digits) in parentheses and maintaining the separation between the remaining digits with a hyphen. The transformation results in a format that is often used in formal and informal contexts to represent phone numbers, specifically "(NNN) NNN-NNN". This format is widely recognized and used in various countries, particularly in the United States and Canada, to denote telephone numbers. The output retains the original digits of the input without alteration, ensuring that the phone number itself remains unchanged, only altering its presentation.

### Relationship Summary:

The relationship between the input and output data is a straightforward format transformation of phone numbers. The process involves taking a phone number formatted as "NNN-NNN-NNN" and converting it into "(NNN) NNN-NNN". This transformation is purely stylistic and does not alter the numerical content of the phone numbers. The purpose of this transformation could be to adhere to a specific style guide, improve readability, or prepare the data for a system that requires phone numbers to be in this specific format. The process is consistent across all data points, indicating a rule-based transformation that applies universally to all input strings, without exception. This transformation is typical in data preprocessing steps where data needs to be standardized or formatted according to specific requirements., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms a phone number from 'NNN-NNN-NNN' format to '(NNN) NNN-NNN' format.

    Parameters:
    phone_number (str): A string representing a phone number in 'NNN-NNN-NNN' format.

    Returns:
    str: The phone number transformed into '(NNN) NNN-NNN' format.
    """
    # Split the phone number into its components
    parts = phone_number.split('-')
    # Reformat the phone number
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

# End time: 2024-04-09 16:41:10.629442
# Elapsed time in seconds: 11.68054091599879
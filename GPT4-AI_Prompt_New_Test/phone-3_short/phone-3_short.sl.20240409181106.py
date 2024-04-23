# Start time: 2024-04-09 18:29:06.747752

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: ### Summary of Input Column Data:

The input data consists of a series of strings, each representing a phone number in a specific format. The format used is a sequence of three groups of digits separated by hyphens. The first group contains three digits, the second group also contains three digits, and the third group contains three digits, following the pattern `XXX-XXX-XXX`. Each string represents a unique phone number, and there are no repetitions or variations in the formatting style across the dataset. The data is qualitative, representing a standardized way of writing phone numbers, rather than quantitative values that could be manipulated mathematically.

### Summary of Output Column Data:

The output data transforms the format of the phone numbers from the input data. The transformation involves reformatting the string representation of each phone number into a slightly different pattern. The new format encloses the first group of three digits in parentheses, followed by a space, and then the second group of three digits, a hyphen, and the third group of three digits, following the pattern `(XXX) XXX-XXX`. This output format retains the same digits and the order of digits as the input; the change is purely in the presentation style of the phone numbers. The output data, like the input, is qualitative, focusing on the standardized representation of phone numbers.

### Relationship Between Input and Output:

The relationship between the input and output data is a direct transformation of the format in which phone numbers are presented. The transformation rules are consistent across all data points:

1. The first group of three digits in the input is enclosed in parentheses in the output.
2. A space is added after the closing parenthesis.
3. The remaining format of the second and third groups of digits, separated by a hyphen, remains unchanged.

This transformation does not alter the numerical or qualitative value of the phone numbers but changes their visual and textual representation to a different standard format. The process is deterministic, with each input string being mapped to a specific output format based on the described rules., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    Transforms the format of a phone number from 'XXX-XXX-XXX' to '(XXX) XXX-XXX'.
    
    Parameters:
    phone_number (str): The phone number in 'XXX-XXX-XXX' format.
    
    Returns:
    str: The phone number in '(XXX) XXX-XXX' format.
    """
    # Split the input string into three parts using the hyphen as a separator
    parts = phone_number.split('-')
    # Reformat the phone number according to the specified output pattern
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

# End time: 2024-04-09 18:29:18.255701
# Elapsed time in seconds: 11.507604685000842


# APPEND TEST SCRIPTS...
print(generated_function("938-242-504"))  ## Output: (938) 242-504
print(generated_function("308-916-545"))  ## Output: (308) 916-545
print(generated_function("623-599-749"))  ## Output: (623) 599-749
print(generated_function("981-424-843"))  ## Output: (981) 424-843
print(generated_function("118-980-214"))  ## Output: (118) 980-214
print(generated_function("244-655-094"))  ## Output: (244) 655-094
print(generated_function("830-941-991"))  ## Output: (830) 941-991


print(generated_function("980-118-214"))  ### Output: (980) 118-214
print(generated_function("655-244-094"))  ### Output: (655) 244-094
print(generated_function("242-938-504"))  ### Output: (242) 938-504
print(generated_function("916-308-545"))  ### Output: (916) 308-545
print(generated_function("599-623-749"))  ### Output: (599) 623-749
print(generated_function("424-981-843"))  ### Output: (424) 981-843
print(generated_function("941-830-991"))  ### Output: (941) 830-991

# TEST SCRIPTS APPENDED!


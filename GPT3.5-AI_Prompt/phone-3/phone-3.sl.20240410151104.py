# Start time: 2024-04-10 15:13:22.950522

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: For the input column data, the phone numbers provided are formatted in the pattern of XXX-XXX-XXX. Each phone number consists of three groups of numbers separated by hyphens.

For the output column data, the phone numbers are formatted in the pattern of (XXX) XXX-XXX. Each phone number consists of three groups of numbers enclosed in parentheses for the area code, followed by a space and the remaining seven digits separated by a hyphen.

The relationship between the input and output is that the input phone numbers are being reformatted to a different pattern in the output. The input phone numbers are being transformed from a XXX-XXX-XXX format to a (XXX) XXX-XXX format. This transformation involves adding parentheses around the area code and changing the hyphen separators to a space and a hyphen., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to reformat phone numbers
def generated_function(phone_number):
    # Split the input phone number into three groups
    area_code, first_three, last_four = phone_number.split('-')
    
    # Reformat the phone number with parentheses and hyphens
    formatted_number = f"({area_code}) {first_three}-{last_four}"
    
    return formatted_number

# Test cases
print(generated_function('938-242-504'))
print(generated_function('308-916-545'))
print(generated_function('623-599-749'))
print(generated_function('981-424-843'))
print(generated_function('118-980-214'))
print(generated_function('244-655-094'))
print(generated_function('830-941-991'))
print(generated_function("938-242-504"))  ## Output: (938) 242-504
print(generated_function("308-916-545"))  ## Output: (308) 916-545
print(generated_function("623-599-749"))  ## Output: (623) 599-749
print(generated_function("981-424-843"))  ## Output: (981) 424-843
print(generated_function("118-980-214"))  ## Output: (118) 980-214
print(generated_function("244-655-094"))  ## Output: (244) 655-094
print(generated_function("830-941-991"))  ## Output: (830) 941-991

# End time: 2024-04-10 15:13:25.123709
# Elapsed time in seconds: 2.1731370379998225
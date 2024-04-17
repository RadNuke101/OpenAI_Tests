# Start time: 2024-04-10 14:34:20.452932

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Input Column Summary:
- The input column data consists of phone numbers in the format XXX XXX XXXX, where each group of numbers is separated by a space.

Output Column Summary:
- The output column data consists of phone numbers in the format XXX-XXX-XXXX, where each group of numbers is separated by a hyphen.

Relationship Summary:
- The relationship between the input and output columns is that the input phone numbers are formatted with spaces between each group of numbers, while the output phone numbers are formatted with hyphens between each group of numbers. The transformation from input to output involves replacing the spaces with hyphens to standardize the phone number format., and input as ['801 456 8756'] output is 801-456-8756, input as ['978 456 8756'] output is 978-456-8756, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(phone_number):
    # Replace spaces with hyphens to transform the input phone number format
    output = phone_number.replace(" ", "-")
    
    # Return the transformed phone number
    return output

# Test cases
print(generated_function('801 456 8756'))  # Output: 801-456-8756
print(generated_function('978 456 8756'))  # Output: 978-456-8756
print(generated_function("801 456 8756"))  ## Output: 801-456-8756
print(generated_function("978 456 8756"))  ## Output: 978-456-8756

# End time: 2024-04-10 14:34:22.305128
# Elapsed time in seconds: 1.85215615300001
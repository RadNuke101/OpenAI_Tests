# Start time: 2024-04-10 14:26:24.773953

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers in the format XXX-XXX-XXX. Each phone number is unique and does not repeat in the dataset. The numbers are presented in a consistent format with three groups of numbers separated by hyphens.

Summary for Output Column:
The output column data consists of phone numbers formatted as (XXX) XXX-XXX. The transformation involves adding parentheses around the first three digits and changing the hyphen to a space between the second and third groups of numbers.

Relationship between Input and Output:
The relationship between the input and output is a formatting change. The input data represents phone numbers in a standard format, while the output data transforms this format into a more visually appealing and commonly used phone number format. The transformation involves adding parentheses around the first three digits and changing the hyphen to a space, making the phone numbers easier to read and remember., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(phone_number):
    # Split the input phone number into three groups
    groups = phone_number.split('-')
    
    # Format the phone number as (XXX) XXX-XXX
    formatted_number = f"({groups[0]}) {groups[1]}-{groups[2]}"
    
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

# End time: 2024-04-10 14:26:27.664736
# Elapsed time in seconds: 2.890723644000019
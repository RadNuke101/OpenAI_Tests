# Start time: 2024-04-10 15:37:44.009211

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers in the format '###-###-###'. Each phone number is unique and follows the same pattern of three sets of three-digit numbers separated by hyphens.

Summary for Output Column:
The output column data consists of phone numbers in the format '(###) ###-###'. Each output phone number is derived from the corresponding input phone number by adding parentheses around the first three digits and changing the hyphens to spaces.

Relationship between Input and Output:
The relationship between the input and output is a transformation of the phone number format. The input phone numbers are converted to a different format by adding parentheses around the first three digits and changing the hyphens to spaces. This transformation results in a more visually appealing and standardized phone number format., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to transform the input phone number format to the output format
def generated_function(input_phone):
    # Add parentheses around the first three digits and change hyphens to spaces
    output_phone = '(' + input_phone[:3] + ') ' + input_phone[4:7] + '-' + input_phone[8:]
    
    return output_phone

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

# End time: 2024-04-10 15:37:46.078977
# Elapsed time in seconds: 2.069720755999697
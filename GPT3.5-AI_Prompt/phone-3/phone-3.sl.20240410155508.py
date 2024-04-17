# Start time: 2024-04-10 15:57:22.034251

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers in the format '###-###-###'. Each phone number is unique and follows the same pattern of three sets of three-digit numbers separated by hyphens.

Summary for Output Column:
The output column data consists of phone numbers formatted as '(###) ###-###'. Each phone number in the output column follows the same pattern of three-digit numbers enclosed in parentheses, followed by a space, then three-digit numbers, a hyphen, and the final three-digit numbers.

Relationship between Input and Output:
The relationship between the input and output columns is that the input phone numbers are transformed into a different format in the output column. The transformation involves enclosing the first set of three digits in parentheses, adding a space, and maintaining the same pattern of hyphens between the sets of numbers. The output format makes the phone numbers more visually appealing and easier to read., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the generated function
def generated_function(phone_number):
    # Transform the input phone number into the desired output format
    output = '(' + phone_number[:3] + ') ' + phone_number[4:7] + '-' + phone_number[8:]
    
    return output

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

# End time: 2024-04-10 15:57:25.743378
# Elapsed time in seconds: 3.7090272850000474
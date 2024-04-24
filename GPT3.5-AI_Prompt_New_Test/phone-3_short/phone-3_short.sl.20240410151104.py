# Start time: 2024-04-10 15:14:57.594985

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: Summary for Input Column Data:
The input column data consists of phone numbers in the format '###-###-###'. Each phone number is unique and follows the same pattern of three sets of three digits separated by hyphens.

Summary for Output Column Data:
The output column data consists of phone numbers in the format '(###) ###-###'. Each output phone number is derived from the corresponding input phone number by adding parentheses around the first three digits and changing the hyphen to a space between the second and third sets of three digits.

Relationship between Input and Output:
The relationship between the input and output is a transformation of the phone number format. The input phone numbers are converted to the output format by adding parentheses around the first three digits and changing the hyphen to a space between the second and third sets of three digits. This transformation maintains the integrity of the original phone number while presenting it in a more standardized and visually appealing format., and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

# Define the function to transform input phone numbers to the desired output format
def generated_function(input_str):
    # Split the input phone number into three sets of three digits
    first_three = input_str[:3]
    second_three = input_str[4:7]
    third_three = input_str[8:]
    
    # Format the output phone number with parentheses and spaces
    output_str = f"({first_three}) {second_three}-{third_three}"
    
    return output_str

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

# End time: 2024-04-10 15:14:59.850136
# Elapsed time in seconds: 2.2550989369997296


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


# Start time: 2024-04-10 17:59:19.290819

'''
Prompt:
Given that input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        # Remove any non-digit characters from the input string
        phone_num = ''.join(filter(str.isdigit, input_str))

        # Format the phone number as (XXX) XXX-XXXX
        formatted_num = f"({phone_num[:3]}) {phone_num[3:6]}-{phone_num[6:]}"

        return formatted_num
    except Exception as e:
        return str(e)

# Test cases
print(generated_function('938-242-504'))  # Output: (938) 242-504
print(generated_function('308-916-545'))  # Output: (308) 916-545
print(generated_function('623-599-749'))  # Output: (623) 599-749
print(generated_function('981-424-843'))  # Output: (981) 424-843
print(generated_function('118-980-214'))  # Output: (118) 980-214
print(generated_function('244-655-094'))  # Output: (244) 655-094
print(generated_function('830-941-991'))  # Output: (830) 941-991
print(generated_function("938-242-504"))  ## Output: (938) 242-504
print(generated_function("308-916-545"))  ## Output: (308) 916-545
print(generated_function("623-599-749"))  ## Output: (623) 599-749
print(generated_function("981-424-843"))  ## Output: (981) 424-843
print(generated_function("118-980-214"))  ## Output: (118) 980-214
print(generated_function("244-655-094"))  ## Output: (244) 655-094
print(generated_function("830-941-991"))  ## Output: (830) 941-991

# End time: 2024-04-10 17:59:23.523358
# Elapsed time in seconds: 4.232431931000065
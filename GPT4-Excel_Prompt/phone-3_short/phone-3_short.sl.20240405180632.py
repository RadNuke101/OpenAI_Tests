# Start time: 2024-04-05 18:13:31.277685

'''
Prompt:
The prompt describes the relationship between the inputs and outputs. Given that the prompt is: return input with parentheses around the first three numbers and delete the first "-" and replace it with a space, and input as ['938-242-504'] output is (938) 242-504, input as ['308-916-545'] output is (308) 916-545, input as ['623-599-749'] output is (623) 599-749, input as ['981-424-843'] output is (981) 424-843, input as ['118-980-214'] output is (118) 980-214, input as ['244-655-094'] output is (244) 655-094, input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. If the input has multiple list elements, that means there are separate inputs that should be passed as separate arguments to the python function. Include the above input in test cases. Do not include the output of the test code in the python program. The generated python code should have only executable statements and comments. The function should return the output, not print it. Do not include assert statements. Name the generated python function as generated_function. Make sure to generate a python function as defined above.
'''

def generated_function(phone_number):
    """
    This function takes a phone number in the format 'XXX-XXX-XXX', puts the first three numbers in parentheses,
    removes the first dash, and replaces it with a space.
    """
    # Split the input string into parts using '-' as the separator
    parts = phone_number.split('-')
    
    # Reformat the phone number as required
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

# End time: 2024-04-05 18:13:41.826198
# Elapsed time in seconds: 10.548198640999544
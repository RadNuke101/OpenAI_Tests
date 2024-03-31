# Start time: 2024-03-30 23:39:08.782528

# Content: Given that given input as ['938-242-504'] output is 504, given input as ['308-916-545'] output is 545, given input as ['623-599-749'] output is 749, given input as ['981-424-843'] output is 843, given input as ['118-980-214'] output is 214, given input as ['244-655-094'] output is 094, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '938-242-504', output: 504
# input: '308-916-545', output: 545
# input: '623-599-749', output: 749
# input: '981-424-843', output: 843
# input: '118-980-214', output: 214
# input: '244-655-094', output: 094

def extract_last_number(phone_number):
    try:
        number = phone_number.split('-')[-1]
        return int(number)
    except (IndexError, ValueError):
        return None

# Test the function with the provided test cases
print(extract_last_number('938-242-504'))
print(extract_last_number('308-916-545'))
print(extract_last_number('623-599-749'))
print(extract_last_number('981-424-843'))
print(extract_last_number('118-980-214'))
print(extract_last_number('244-655-094'))

# End time: 2024-03-30 23:39:11.672809
# Elapsed time in seconds: 2.890301671999623
# Start time: 2024-03-30 23:36:27.709395

# Content: Given that given input as ['938-242-504'] output is 938, given input as ['308-916-545'] output is 308, given input as ['623-599-749'] output is 623, given input as ['981-424-843'] output is 981, given input as ['118-980-214'] output is 118, given input as ['244-655-094'] output is 244, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '938-242-504'
# Output: 938

def extract_first_number(input_str):
    try:
        number = input_str.split('-')[0]
        return int(number)
    except (IndexError, ValueError):
        return None

# Test cases
print(extract_first_number('938-242-504'))  # Output: 938
print(extract_first_number('308-916-545'))  # Output: 308
print(extract_first_number('623-599-749'))  # Output: 623
print(extract_first_number('981-424-843'))  # Output: 981
print(extract_first_number('118-980-214'))  # Output: 118
print(extract_first_number('244-655-094'))  # Output: 244

# End time: 2024-03-30 23:36:29.400233
# Elapsed time in seconds: 1.6907846620015334
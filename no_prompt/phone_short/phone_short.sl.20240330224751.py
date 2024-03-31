# Start time: 2024-03-30 22:47:54.642572

# Content: Given that given input as ['938-242-504'] output is 938, given input as ['308-916-545'] output is 308, given input as ['623-599-749'] output is 623, given input as ['981-424-843'] output is 981, given input as ['118-980-214'] output is 118, given input as ['244-655-094'] output is 244, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '938-242-504', output: 938
# input: '308-916-545', output: 308
# input: '623-599-749', output: 623
# input: '981-424-843', output: 981
# input: '118-980-214', output: 118
# input: '244-655-094', output: 244

def extract_first_number(phone_number):
    try:
        # Split the phone number by '-'
        parts = phone_number.split('-')
        
        # Extract the first part and convert it to an integer
        first_number = int(parts[0])
        
        return first_number
    except (IndexError, ValueError):
        print("Invalid input format")
        return None

# Test the function with the provided test cases
print(extract_first_number('938-242-504'))
print(extract_first_number('308-916-545'))
print(extract_first_number('623-599-749'))
print(extract_first_number('981-424-843'))
print(extract_first_number('118-980-214'))
print(extract_first_number('244-655-094'))

# End time: 2024-03-30 22:47:57.075760
# Elapsed time in seconds: 2.4341733379988
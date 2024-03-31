# Start time: 2024-03-30 20:36:56.364779

# Content: Given that given input as ['938-242-504'] output is 242, given input as ['308-916-545'] output is 916, given input as ['623-599-749'] output is 599, given input as ['981-424-843'] output is 424, given input as ['118-980-214'] output is 980, given input as ['244-655-094'] output is 655, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: '938-242-504', Output: 242
# Input: '308-916-545', Output: 916
# Input: '623-599-749', Output: 599
# Input: '981-424-843', Output: 424
# Input: '118-980-214', Output: 980
# Input: '244-655-094', Output: 655

def extract_middle_number(phone_number):
    try:
        # Split the phone number by '-'
        parts = phone_number.split('-')
        
        # Return the middle number
        return int(parts[1])
    except (IndexError, ValueError):
        return None

# Test the function with the provided test cases
print(extract_middle_number('938-242-504'))  # Output: 242
print(extract_middle_number('308-916-545'))  # Output: 916
print(extract_middle_number('623-599-749'))  # Output: 599
print(extract_middle_number('981-424-843'))  # Output: 424
print(extract_middle_number('118-980-214'))  # Output: 980
print(extract_middle_number('244-655-094'))  # Output: 655

# End time: 2024-03-30 20:37:03.301759
# Elapsed time in seconds: 6.936803894999684
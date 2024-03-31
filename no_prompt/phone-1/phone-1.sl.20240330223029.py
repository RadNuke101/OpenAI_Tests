# Start time: 2024-03-30 22:45:05.715012

# Content: Given that given input as ['938-242-504'] output is 242, given input as ['308-916-545'] output is 916, given input as ['623-599-749'] output is 599, given input as ['981-424-843'] output is 424, given input as ['118-980-214'] output is 980, given input as ['244-655-094'] output is 655, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '938-242-504', output: 242
# input: '308-916-545', output: 916
# input: '623-599-749', output: 599
# input: '981-424-843', output: 424
# input: '118-980-214', output: 980
# input: '244-655-094', output: 655

def extract_middle_number(phone_number):
    try:
        # Split the phone number by '-'
        parts = phone_number.split('-')
        
        # Extract the middle number
        middle_number = parts[1]
        
        return int(middle_number)
    except (IndexError, ValueError):
        print("Invalid input format. Please provide a valid phone number in the format '###-###-###'.")

# Test the function with the provided test cases
print(extract_middle_number('938-242-504'))
print(extract_middle_number('308-916-545'))
print(extract_middle_number('623-599-749'))
print(extract_middle_number('981-424-843'))
print(extract_middle_number('118-980-214'))
print(extract_middle_number('244-655-094'))

# End time: 2024-03-30 22:45:08.133763
# Elapsed time in seconds: 2.4186841959999583
# Start time: 2024-03-30 18:51:26.864800

# Content: Given that given input as ['938-242-504'] output is (938) 242-504, given input as ['308-916-545'] output is (308) 916-545, given input as ['623-599-749'] output is (623) 599-749, given input as ['981-424-843'] output is (981) 424-843, given input as ['118-980-214'] output is (118) 980-214, given input as ['244-655-094'] output is (244) 655-094, given input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_phone_number(phone_number):
    try:
        # Input: '938-242-504', Output: (938) 242-504
        # Input: '308-916-545', Output: (308) 916-545
        # Input: '623-599-749', Output: (623) 599-749
        # Input: '981-424-843', Output: (981) 424-843
        # Input: '118-980-214', Output: (118) 980-214
        # Input: '244-655-094', Output: (244) 655-094
        # Input: '830-941-991', Output: (830) 941-991
        phone_number = phone_number.replace('-', '')
        formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
        return formatted_number
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(format_phone_number('938-242-504'))  # Output: (938) 242-504
print(format_phone_number('308-916-545'))  # Output: (308) 916-545
print(format_phone_number('623-599-749'))  # Output: (623) 599-749
print(format_phone_number('981-424-843'))  # Output: (981) 424-843
print(format_phone_number('118-980-214'))  # Output: (118) 980-214
print(format_phone_number('244-655-094'))  # Output: (244) 655-094
print(format_phone_number('830-941-991'))  # Output: (830) 941-991

# End time: 2024-03-30 18:51:31.684982
# Elapsed time in seconds: 4.820071619999908
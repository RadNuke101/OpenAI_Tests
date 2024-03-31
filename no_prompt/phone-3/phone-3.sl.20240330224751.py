# Start time: 2024-03-30 22:49:58.088937

# Content: Given that given input as ['938-242-504'] output is (938) 242-504, given input as ['308-916-545'] output is (308) 916-545, given input as ['623-599-749'] output is (623) 599-749, given input as ['981-424-843'] output is (981) 424-843, given input as ['118-980-214'] output is (118) 980-214, given input as ['244-655-094'] output is (244) 655-094, given input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '938-242-504', output: (938) 242-504
# input: '308-916-545', output: (308) 916-545
# input: '623-599-749', output: (623) 599-749
# input: '981-424-843', output: (981) 424-843
# input: '118-980-214', output: (118) 980-214
# input: '244-655-094', output: (244) 655-094
# input: '830-941-991', output: (830) 941-991

def format_phone_number(phone_number):
    try:
        # Remove any non-digit characters from the input
        phone_number = ''.join(filter(str.isdigit, phone_number))

        # Format the phone number as (XXX) XXX-XXXX
        formatted_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"

        return formatted_number
    except Exception as e:
        return f"Error: {e}"

# Test the function with the provided test cases
print(format_phone_number('938-242-504'))
print(format_phone_number('308-916-545'))
print(format_phone_number('623-599-749'))
print(format_phone_number('981-424-843'))
print(format_phone_number('118-980-214'))
print(format_phone_number('244-655-094'))
print(format_phone_number('830-941-991'))

# End time: 2024-03-30 22:50:05.757402
# Elapsed time in seconds: 7.6682887179995305
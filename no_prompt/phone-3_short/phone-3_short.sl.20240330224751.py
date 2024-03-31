# Start time: 2024-03-30 22:51:00.280407

# Content: Given that given input as ['938-242-504'] output is (938) 242-504, given input as ['308-916-545'] output is (308) 916-545, given input as ['623-599-749'] output is (623) 599-749, given input as ['981-424-843'] output is (981) 424-843, given input as ['118-980-214'] output is (118) 980-214, given input as ['244-655-094'] output is (244) 655-094, given input as ['830-941-991'] output is (830) 941-991, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_phone_number(phone_number):
    try:
        if len(phone_number) != 12 or phone_number[3] != '-' or phone_number[7] != '-':
            raise ValueError("Invalid input format")
        
        area_code = phone_number[:3]
        first_part = phone_number[4:7]
        second_part = phone_number[8:]
        
        formatted_number = f"({area_code}) {first_part}-{second_part}"
        
        return formatted_number
    except ValueError as e:
        print(f"Error: {e}")

# Test cases
# Input: '938-242-504', Expected output: (938) 242-504
print(format_phone_number('938-242-504'))
# Input: '308-916-545', Expected output: (308) 916-545
print(format_phone_number('308-916-545'))
# Input: '623-599-749', Expected output: (623) 599-749
print(format_phone_number('623-599-749'))
# Input: '981-424-843', Expected output: (981) 424-843
print(format_phone_number('981-424-843'))
# Input: '118-980-214', Expected output: (118) 980-214
print(format_phone_number('118-980-214'))
# Input: '244-655-094', Expected output: (244) 655-094
print(format_phone_number('244-655-094'))
# Input: '830-941-991', Expected output: (830) 941-991
print(format_phone_number('830-941-991'))

# End time: 2024-03-30 22:51:07.063426
# Elapsed time in seconds: 6.782860727998923
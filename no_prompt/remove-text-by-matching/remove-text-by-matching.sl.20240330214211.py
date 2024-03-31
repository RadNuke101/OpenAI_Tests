# Start time: 2024-03-30 21:48:11.011201

# Content: Given that given input as ['801-345-1987'] output is 8013451987, given input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def clean_phone_number(phone_number):
    try:
        clean_number = phone_number.replace('-', '')
        return int(clean_number)
    except AttributeError:
        print("Input is not a string")
    except ValueError:
        print("Input contains non-numeric characters")

# Test cases
# Input: '801-345-1987'
# Output: 8013451987
print(clean_phone_number('801-345-1987'))

# Input: '612-554-2000'
# Output: 6125542000
print(clean_phone_number('612-554-2000'))

# End time: 2024-03-30 21:48:12.160019
# Elapsed time in seconds: 1.1487854839997453
# Start time: 2024-03-30 23:41:18.486866

# Content: Given that given input as ['801-345-1987'] output is 8013451987, given input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def format_phone_number(phone_number):
    try:
        # Input: '801-345-1987'
        # Output: 8013451987
        formatted_number = phone_number.replace('-', '')
        return int(formatted_number)
    except AttributeError:
        print("Error: Input must be a string.")
    except ValueError:
        print("Error: Input must contain only digits and dashes.")

# Test cases
print(format_phone_number('801-345-1987'))
print(format_phone_number('612-554-2000'))
print(format_phone_number(1234567890))
print(format_phone_number('abc-def-ghij'))

# End time: 2024-03-30 23:41:19.606127
# Elapsed time in seconds: 1.1192457670003932
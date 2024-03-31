# Start time: 2024-03-30 23:25:21.285496

# Content: Given that given input as ['801-345-1987'] output is 8013451987, given input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '801-345-1987'
# Output: 8013451987

def format_phone_number(phone_number):
    try:
        # Remove any non-digit characters from the phone number
        formatted_number = ''.join(filter(str.isdigit, phone_number))
        return formatted_number
    except Exception as e:
        print("Error: ", e)

# Test cases
print(format_phone_number('801-345-1987'))
print(format_phone_number('612-554-2000'))

# End time: 2024-03-30 23:25:22.744698
# Elapsed time in seconds: 1.459160886999598
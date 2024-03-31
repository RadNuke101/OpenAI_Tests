# Start time: 2024-03-30 19:09:50.058567

# Content: Given that given input as ['801-345-1987'] output is 8013451987, given input as ['612-554-2000'] output is 6125542000, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '801-345-1987'
# Output: 8013451987

def format_phone_number(phone_number):
    try:
        # Remove any dashes from the input phone number
        phone_number = phone_number.replace('-', '')
        
        # Convert the phone number to an integer and return
        return int(phone_number)
    except ValueError:
        print("Invalid input. Please enter a valid phone number.")
        return None

# Test cases
print(format_phone_number('801-345-1987'))
print(format_phone_number('612-554-2000'))
print(format_phone_number('123-456-7890'))

# End time: 2024-03-30 19:09:52.146050
# Elapsed time in seconds: 2.087421333000293
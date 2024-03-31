# Start time: 2024-03-30 20:07:58.403717

# Content: Given that given input as ['801-456-8765'] output is 8014568765, given input as ['<978> 654-0299'] output is 9786540299, given input as ['978.654.0299'] output is 9786540299, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def clean_phone_number(phone_number):
    try:
        # Input: '801-456-8765'
        phone_number = phone_number.replace('-', '').replace('(', '').replace(')', '').replace('<', '').replace('>', '').replace('.', '').replace(' ', '')
        
        # Input: '<978> 654-0299'
        # Input: '978.654.0299'
        return int(phone_number)
    except ValueError:
        print("Invalid phone number format")
        return None

# Test cases
print(clean_phone_number('801-456-8765'))  # Output: 8014568765
print(clean_phone_number('<978> 654-0299'))  # Output: 9786540299
print(clean_phone_number('978.654.0299'))  # Output: 9786540299

# End time: 2024-03-30 20:08:00.292621
# Elapsed time in seconds: 1.8888735639993683
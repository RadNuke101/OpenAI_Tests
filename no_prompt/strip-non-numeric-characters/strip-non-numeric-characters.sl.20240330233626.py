# Start time: 2024-03-30 23:49:52.382772

# Content: Given that given input as ['100 apples'] output is 100, given input as ['the price is %500 dollars'] output is 500, given input as ['serial number %003399'] output is 003399, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '100 apples'
# Output: 100

# Input: 'the price is %500 dollars'
# Output: 500

# Input: 'serial number %003399'
# Output: 003399

def extract_number(input_str):
    try:
        number = int(''.join(filter(str.isdigit, input_str)))
        return number
    except ValueError:
        try:
            number = int(input_str.split('%')[-1])
            return number
        except ValueError:
            print("Unable to extract number from input")
            return None

# Test cases
print(extract_number('100 apples'))
print(extract_number('the price is %500 dollars'))
print(extract_number('serial number %003399'))

# End time: 2024-03-30 23:49:54.467916
# Elapsed time in seconds: 2.0851127000023553
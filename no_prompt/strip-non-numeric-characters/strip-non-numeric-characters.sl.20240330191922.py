# Start time: 2024-03-30 19:33:00.290571

# Content: Given that given input as ['100 apples'] output is 100, given input as ['the price is %500 dollars'] output is 500, given input as ['serial number %003399'] output is 003399, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '100 apples', output: 100
# input: 'the price is %500 dollars', output: 500
# input: 'serial number %003399', output: 003399

def extract_number(input_str):
    try:
        # Find the number in the input string
        number = ''.join(filter(str.isdigit, input_str))
        return int(number)
    except ValueError:
        print("Error: Unable to extract number from input")
        return None

# Test the function with the provided test cases
print(extract_number('100 apples'))
print(extract_number('the price is %500 dollars'))
print(extract_number('serial number %003399'))

# End time: 2024-03-30 19:33:03.582676
# Elapsed time in seconds: 3.29200705500034
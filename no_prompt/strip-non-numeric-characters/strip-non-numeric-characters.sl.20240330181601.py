# Start time: 2024-03-30 18:29:09.844850

# Content: Given that given input as ['100 apples'] output is 100, given input as ['the price is %500 dollars'] output is 500, given input as ['serial number %003399'] output is 003399, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_number(input_string):
    try:
        number = ''.join(filter(str.isdigit, input_string))
        return number
    except Exception as e:
        print("Error: ", e)

# Test cases
# input_string = '100 apples'
# print(extract_number(input_string))  # Output: 100

# input_string = 'the price is %500 dollars'
# print(extract_number(input_string))  # Output: 500

# input_string = 'serial number %003399'
# print(extract_number(input_string))  # Output: 003399

# End time: 2024-03-30 18:29:12.614184
# Elapsed time in seconds: 2.7692536240000436
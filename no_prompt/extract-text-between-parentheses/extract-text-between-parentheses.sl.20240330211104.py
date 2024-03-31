# Start time: 2024-03-30 21:19:15.153100

# Content: Given that given input as ['Jones <60>'] output is 60, given input as ['Jones <57>'] output is 57, given input as ['Jones <55>'] output is 55, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Jones <60>'
# Output: 60

def extract_number(input_str):
    try:
        number = int(input_str.split('<')[1].strip('>').strip())
        return number
    except (ValueError, IndexError):
        return None

# Test cases
print(extract_number('Jones <60>'))  # Output: 60
print(extract_number('Jones <57>'))  # Output: 57
print(extract_number('Jones <55>'))  # Output: 55

# End time: 2024-03-30 21:19:17.982122
# Elapsed time in seconds: 2.828962715000671
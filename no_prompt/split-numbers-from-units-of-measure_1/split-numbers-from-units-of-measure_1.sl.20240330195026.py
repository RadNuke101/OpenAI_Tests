# Start time: 2024-03-30 19:58:47.929647

# Content: Given that given input as ['80v', '3'] output is 80, given input as ['10hrs', '3'] output is 10, given input as ['7h', '2'] output is 7, given input as ['500m', '4'] output is 500, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# input: '80v', '3'
# output: 80

def extract_number(input_str):
    try:
        number = ''
        for char in input_str:
            if char.isdigit():
                number += char
            else:
                break
        return int(number)
    except:
        return None

# Test cases
print(extract_number('80v'))  # Output: 80
print(extract_number('10hrs'))  # Output: 10
print(extract_number('7h'))  # Output: 7
print(extract_number('500m'))  # Output: 500

# End time: 2024-03-30 19:58:49.783277
# Elapsed time in seconds: 1.8535985850003271
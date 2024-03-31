# Start time: 2024-03-30 23:48:20.494111

# Content: Given that given input as ['736 miles'] output is 736, given input as ['1255 miles'] output is 1255, given input as ['1221 miles'] output is 1221, given input as ['790 miles'] output is 790, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# input: '736 miles'
# output: 736

def extract_number(input_str):
    try:
        number = int(input_str.split()[0])
        return number
    except (IndexError, ValueError):
        return None

# Test cases
print(extract_number('736 miles'))  # Output: 736
print(extract_number('1255 miles'))  # Output: 1255
print(extract_number('1221 miles'))  # Output: 1221
print(extract_number('790 miles'))  # Output: 790

# End time: 2024-03-30 23:48:21.776236
# Elapsed time in seconds: 1.2821045149976271
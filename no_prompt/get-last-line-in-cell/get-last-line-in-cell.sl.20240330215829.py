# Start time: 2024-03-30 22:11:02.672986

# Content: Given that given input as ['11/1/2015 - First call/n12/3/2015-order placed/n11/15/2015-follow-up,interested'] output is 11/15/2015-follow-up,interested, given input as ['11/1/2015 - First call/n12/3/2015-order placed'] output is 12/3/2015-order placed, given input as ['11/1/2015 - First call'] output is 11/1/2015 - First call, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_info(input_str):
    try:
        info = input_str.split('/n')[-1]
        return info
    except IndexError:
        return "Invalid input format"

# Test cases
input1 = '11/1/2015 - First call/n12/3/2015-order placed/n11/15/2015-follow-up,interested'
print(extract_info(input1))  # Output should be: 11/15/2015-follow-up,interested

input2 = '11/1/2015 - First call/n12/3/2015-order placed'
print(extract_info(input2))  # Output should be: 12/3/2015-order placed

input3 = '11/1/2015 - First call'
print(extract_info(input3))  # Output should be: 11/1/2015 - First call

# End time: 2024-03-30 22:11:04.454188
# Elapsed time in seconds: 1.781150932998571
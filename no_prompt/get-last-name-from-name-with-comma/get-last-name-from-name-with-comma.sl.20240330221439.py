# Start time: 2024-03-30 22:16:22.674812

# Content: Given that given input as ['chang,amy'] output is amy,chang, given input as ['smith,bobby'] output is bobby,smith, given input as ['lennox,aaron'] output is aaron,lennox, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def rearrange_names(input_str):
    try:
        names = input_str.split(',')
        reversed_names = names[::-1]
        output_str = ','.join(reversed_names)
        return output_str
    except Exception as e:
        return "Invalid input"

# Test cases
# Input: 'chang,amy'
# Expected Output: 'amy,chang'
print(rearrange_names('chang,amy'))

# Input: 'smith,bobby'
# Expected Output: 'bobby,smith'
print(rearrange_names('smith,bobby'))

# Input: 'lennox,aaron'
# Expected Output: 'aaron,lennox'
print(rearrange_names('lennox,aaron'))

# End time: 2024-03-30 22:16:24.465265
# Elapsed time in seconds: 1.7903743410006427
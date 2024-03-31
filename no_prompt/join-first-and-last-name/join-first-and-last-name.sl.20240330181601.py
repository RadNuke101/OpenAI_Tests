# Start time: 2024-03-30 18:28:30.496723

# Content: Given that given input as ['susan', 'chang'] output is susan chang, given input as ['aaron', 'kim'] output is aaron kim, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def combine_names(input_str):
    try:
        names = input_str.split(',')
        return ' '.join(names)
    except Exception as e:
        return "Invalid input"

# Test cases
# Input: 'susan, chang'
# Output: 'susan chang'
print(combine_names('susan, chang'))

# Input: 'aaron, kim'
# Output: 'aaron kim'
print(combine_names('aaron, kim'))

# End time: 2024-03-30 18:28:31.990859
# Elapsed time in seconds: 1.494090286999949
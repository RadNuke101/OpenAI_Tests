# Start time: 2024-03-30 21:22:24.761988

# Content: Given that given input as ['  The shawshank'] output is The shawshank, given input as ['The    godfather'] output is The godfather, given input as ['    pulp   fiction'] output is pulp fiction, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: '  The shawshank'
# Output: 'The shawshank'

# Input: 'The    godfather'
# Output: 'The godfather'

# Input: '    pulp   fiction'
# Output: 'pulp fiction'

def clean_string(input_str):
    try:
        cleaned_str = ' '.join(input_str.split())
        return cleaned_str
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
input1 = '  The shawshank'
input2 = 'The    godfather'
input3 = '    pulp   fiction'

output1 = clean_string(input1)
output2 = clean_string(input2)
output3 = clean_string(input3)

# End time: 2024-03-30 21:22:26.795297
# Elapsed time in seconds: 2.031037683998875
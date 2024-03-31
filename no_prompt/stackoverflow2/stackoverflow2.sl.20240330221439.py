# Start time: 2024-03-30 22:27:29.096505

# Content: Given that given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'india china japan'
# Output: 'india china'

def match_input(input_str):
    try:
        input_list = input_str.split()
        output_str = ' '.join(input_list[:-1])
        return output_str
    except Exception as e:
        print("Error: ", e)

# Test cases
print(match_input('india china japan'))  # Output: 'india china'
print(match_input('indonesia korea'))    # Output: 'indonesia'

# End time: 2024-03-30 22:27:31.586948
# Elapsed time in seconds: 2.4903647809987888
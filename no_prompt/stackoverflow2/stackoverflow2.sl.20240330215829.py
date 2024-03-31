# Start time: 2024-03-30 22:11:16.174555

# Content: Given that given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_countries(input_str):
    try:
        # Input: 'india china japan'
        # Output: 'india china'
        
        # Input: 'indonesia korea'
        # Output: 'indonesia'
        
        words = input_str.split()
        if len(words) > 1:
            return ' '.join(words[:-1])
        else:
            return input_str
    except Exception as e:
        return "Error: Invalid input"

# Test cases
print(match_countries('india china japan'))
print(match_countries('indonesia korea'))

# End time: 2024-03-30 22:11:17.684491
# Elapsed time in seconds: 1.5098859740010084
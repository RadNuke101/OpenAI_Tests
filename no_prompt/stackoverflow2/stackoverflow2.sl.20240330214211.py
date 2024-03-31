# Start time: 2024-03-30 21:55:32.255621

# Content: Given that given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'india china japan'
# Output: 'india china'

def match_countries(input_str):
    try:
        countries = input_str.split()
        if len(countries) > 1:
            return ' '.join(countries[:-1])
        else:
            return countries[0]
    except Exception as e:
        return "Invalid input"

# Test cases
print(match_countries('india china japan'))  # Output: india china
print(match_countries('indonesia korea'))     # Output: indonesia

# End time: 2024-03-30 21:55:33.818045
# Elapsed time in seconds: 1.562383767000938
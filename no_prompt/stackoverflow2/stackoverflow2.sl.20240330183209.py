# Start time: 2024-03-30 18:45:23.042607

# Content: Given that given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_countries(input_str):
    try:
        countries = input_str.split()
        if len(countries) < 2:
            raise ValueError("Input must contain at least two countries")
        
        return ' '.join(countries[:2])
    
    except Exception as e:
        return str(e)

# Test cases
# Input: 'india china japan'
# Output: 'india china'
print(match_countries('india china japan'))

# Input: 'indonesia korea'
# Output: 'indonesia'
print(match_countries('indonesia korea'))

# End time: 2024-03-30 18:45:25.127045
# Elapsed time in seconds: 2.084429347000082
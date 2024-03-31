# Start time: 2024-03-30 21:07:49.868472

# Content: Given that given input as ['india china japan'] output is india china, given input as ['indonesia korea'] output is indonesia, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_countries(input_str):
    try:
        # Input: 'india china japan'
        # Output: 'india china'
        
        # Split the input string by space
        countries = input_str.split()
        
        # Return the first two countries
        return ' '.join(countries[:2])
    
    except Exception as e:
        print("Error: Invalid input format")

# Test cases
print(match_countries('india china japan'))  # Output: india china
print(match_countries('indonesia korea'))     # Output: indonesia

# End time: 2024-03-30 21:07:51.481156
# Elapsed time in seconds: 1.6126541600006021
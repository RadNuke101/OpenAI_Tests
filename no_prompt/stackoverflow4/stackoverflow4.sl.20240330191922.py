# Start time: 2024-03-30 19:19:35.812568

# Content: Given that given input as ['R/V<208,0,32>'] output is R/V 208 0 32, given input as ['R/S<184,28,16>'] output is R/S 184 28 16, given input as ['R/B<255,88,80>'] output is R/B 255 88 80, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'R/V<208,0,32>'
# Output: 'R/V 208 0 32'

def parse_input(input_str):
    try:
        # Remove unnecessary characters
        input_str = input_str.replace('<', ' ').replace('>', ' ').replace(',', ' ')
        
        # Split the string by spaces
        parts = input_str.split()
        
        # Extract the required values
        output_str = parts[0] + ' ' + parts[1] + ' ' + parts[2] + ' ' + parts[3] + ' ' + parts[4]
        
        return output_str
    except Exception as e:
        return "Invalid input"

# Test cases
print(parse_input('R/V<208,0,32>'))  # Output: R/V 208 0 32
print(parse_input('R/S<184,28,16>'))  # Output: R/S 184 28 16
print(parse_input('R/B<255,88,80>'))  # Output: R/B 255 88 80

# End time: 2024-03-30 19:19:39.522064
# Elapsed time in seconds: 3.7093093419998695
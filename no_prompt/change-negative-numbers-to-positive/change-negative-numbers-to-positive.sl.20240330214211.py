# Start time: 2024-03-30 21:49:28.012943

# Content: Given that given input as ['-%134'] output is %134, given input as ['500'] output is 500, given input as ['5.125'] output is 5.125, given input as ['-%43.00'] output is %43.00, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '-%134', output: %134
# input: '500', output: 500
# input: '5.125', output: 5.125
# input: '-%43.00', output: %43.00

def clean_input(input_str):
    try:
        # Remove any leading '-' character
        if input_str[0] == '-':
            input_str = input_str[1:]
        
        # Remove any leading '%' character
        if input_str[0] == '%':
            input_str = input_str[1:]
        
        # Convert the cleaned input to float if it contains a decimal point, otherwise to int
        if '.' in input_str:
            return float(input_str)
        else:
            return int(input_str)
    except Exception as e:
        print("Error:", e)

# Test the function with the provided test cases
print(clean_input('-%134'))  # Output: %134
print(clean_input('500'))    # Output: 500
print(clean_input('5.125'))  # Output: 5.125
print(clean_input('-%43.00'))  # Output: %43.00

# End time: 2024-03-30 21:49:32.141388
# Elapsed time in seconds: 4.128327705000629
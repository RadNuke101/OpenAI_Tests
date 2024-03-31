# Start time: 2024-03-30 21:00:33.245925

# Content: Given that given input as ['80v', '3'] output is v, given input as ['10hrs', '3'] output is hrs, given input as ['7h', '2'] output is h, given input as ['500m', '4'] output is m, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '80v', output: 'v'
# input: '10hrs', output: 'hrs'
# input: '7h', output: 'h'
# input: '500m', output: 'm'

def extract_unit(input_str):
    try:
        # Find the index of the first digit in the input string
        index = next(i for i, c in enumerate(input_str) if c.isdigit())
        
        # Extract the unit from the input string
        unit = input_str[index:]
        
        return unit
    except StopIteration:
        return "No unit found in input"

# Test the function with the given test cases
print(extract_unit('80v'))
print(extract_unit('10hrs'))
print(extract_unit('7h'))
print(extract_unit('500m'))

# End time: 2024-03-30 21:00:38.654139
# Elapsed time in seconds: 5.408073866999985
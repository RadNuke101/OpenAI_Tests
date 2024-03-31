# Start time: 2024-03-30 20:13:25.960687

# Content: Given that given input as ['80v', '3'] output is v, given input as ['10hrs', '3'] output is hrs, given input as ['7h', '2'] output is h, given input as ['500m', '4'] output is m, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '80v', '3'  output: 'v'
# input: '10hrs', '3'  output: 'hrs'
# input: '7h', '2'  output: 'h'
# input: '500m', '4'  output: 'm'

def extract_unit(input_str, num_str):
    try:
        num = int(num_str)
        unit = ''
        for char in input_str:
            if not char.isdigit():
                unit += char
        return unit
    except ValueError:
        return "Invalid input"

# Test cases
print(extract_unit('80v', '3'))  # Output: v
print(extract_unit('10hrs', '3'))  # Output: hrs
print(extract_unit('7h', '2'))  # Output: h
print(extract_unit('500m', '4'))  # Output: m

# End time: 2024-03-30 20:13:28.139029
# Elapsed time in seconds: 2.1783195919997524
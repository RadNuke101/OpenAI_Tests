# Start time: 2024-03-30 20:02:51.625009

# Content: Given that given input as ['zx66448', 'z'] output is x66448, given input as ['zx66448', 'x'] output is z66448, given input as ['zx66448', '6'] output is zx448, given input as ['zx66448', '4'] output is zx668, given input as ['zx66448', '8'] output is zx6644, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: 'zx66448', 'z' -> output: 'x66448'
# input: 'zx66448', 'x' -> output: 'z66448'
# input: 'zx66448', '6' -> output: 'zx448'
# input: 'zx66448', '4' -> output: 'zx668'
# input: 'zx66448', '8' -> output: 'zx6644'

def replace_char(input_str, char):
    try:
        if len(char) != 1:
            raise ValueError("Character input must be a single character")
        
        if char not in input_str:
            raise ValueError("Character not found in input string")
        
        return input_str.replace(char, '', 1)
    
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Test cases
print(replace_char('zx66448', 'z'))
print(replace_char('zx66448', 'x'))
print(replace_char('zx66448', '6'))
print(replace_char('zx66448', '4'))
print(replace_char('zx66448', '8'))

# End time: 2024-03-30 20:02:55.906676
# Elapsed time in seconds: 4.281600368999534
# Start time: 2024-03-30 21:38:32.140634

# Content: Given that given input as ['zx66448', 'z'] output is x66448, given input as ['zx66448', 'x'] output is z66448, given input as ['zx66448', '6'] output is zx448, given input as ['zx66448', '4'] output is zx668, given input as ['zx66448', '8'] output is zx6644, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def remove_char(input_str, char):
    try:
        index = input_str.index(char)
        output_str = input_str[:index] + input_str[index+1:]
        return output_str
    except ValueError:
        print("Character not found in input string")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# Input: 'zx66448', 'z'
# Output: 'x66448'
print(remove_char('zx66448', 'z'))

# Input: 'zx66448', 'x'
# Output: 'z66448'
print(remove_char('zx66448', 'x'))

# Input: 'zx66448', '6'
# Output: 'zx448'
print(remove_char('zx66448', '6'))

# Input: 'zx66448', '4'
# Output: 'zx668'
print(remove_char('zx66448', '4'))

# Input: 'zx66448', '8'
# Output: 'zx6644'
print(remove_char('zx66448', '8'))

# End time: 2024-03-30 21:38:39.857636
# Elapsed time in seconds: 7.71678368799985
# Start time: 2024-03-30 23:00:48.594563

# Content: Given that given input as ['zx66448', 'z'] output is x66448, given input as ['zx66448', 'x'] output is z66448, given input as ['zx66448', '6'] output is zx448, given input as ['zx66448', '4'] output is zx668, given input as ['zx66448', '8'] output is zx6644, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def remove_char(input_str, char):
    try:
        if len(char) != 1:
            raise ValueError("Character must be a single character")
        
        output_str = input_str.replace(char, "")
        return output_str
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")

# Test cases
# Input: 'zx66448', 'z' => Output: 'x66448'
# Input: 'zx66448', 'x' => Output: 'z66448'
# Input: 'zx66448', '6' => Output: 'zx448'
# Input: 'zx66448', '4' => Output: 'zx668'
# Input: 'zx66448', '8' => Output: 'zx6644'

print(remove_char('zx66448', 'z'))
print(remove_char('zx66448', 'x'))
print(remove_char('zx66448', '6'))
print(remove_char('zx66448', '4'))
print(remove_char('zx66448', '8'))

# End time: 2024-03-30 23:00:51.238644
# Elapsed time in seconds: 2.6440121380001074
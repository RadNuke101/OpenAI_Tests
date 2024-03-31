# Start time: 2024-03-30 23:21:55.376446

# Content: Given that given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_string(input_str):
    try:
        # Input: 'red ball, green sweater', 'red', 'green', 'pink'
        parts = input_str.split(', ')
        colors = parts[1].split()
        for color in colors:
            if color not in parts[2:]:
                return False
        return True
    except Exception as e:
        return False

# Test cases
print(check_string('red ball, green sweater', 'red', 'green', 'pink'))  # Output: True
print(check_string('pink ball, green sweater', 'red', 'green', 'pink'))  # Output: False
print(check_string('blue sea, pink ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_string('black sea, white ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_string('red green blue', 'red', 'blue', 'pink'))  # Output: True

# End time: 2024-03-30 23:21:57.547913
# Elapsed time in seconds: 2.1714175590022933
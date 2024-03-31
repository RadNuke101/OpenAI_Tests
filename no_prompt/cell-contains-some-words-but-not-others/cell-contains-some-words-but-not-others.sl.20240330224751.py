# Start time: 2024-03-30 22:48:45.456043

# Content: Given that given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_colors(input_str):
    try:
        input_list = input_str.split(', ')
        colors = input_list[1:]
        
        for color in colors:
            if color not in input_list[0]:
                return False
        
        return True
    except Exception as e:
        print("Error:", e)
        return False

# Test cases
print(check_colors('red ball, green sweater, red, green, pink'))  # Output: True
print(check_colors('pink ball, green sweater, red, green, pink'))  # Output: False
print(check_colors('blue sea, pink ribbon, red, blue, pink'))  # Output: False
print(check_colors('black sea, white ribbon, red, blue, pink'))  # Output: False
print(check_colors('red green blue, red, blue, pink'))  # Output: True

# End time: 2024-03-30 22:48:48.423749
# Elapsed time in seconds: 2.967685423000148
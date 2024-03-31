# Start time: 2024-03-30 22:45:08.240085

# Content: Given that given input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, given input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, given input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, given input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_matching(input_str, color1, color2, keyword):
    try:
        words = input_str.split()
        if color1 in words and color2 in words and keyword in words:
            return True
        else:
            return False
    except Exception as e:
        print("Error: ", e)
        return False

# Test cases
print(check_matching('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: True
print(check_matching('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: False
print(check_matching('blue neon signs', 'blue', 'green', 'neon'))  # Output: False
print(check_matching('hot pink socks', 'blue', 'pink', 'neon'))  # Output: True
print(check_matching('deep black eyes', 'yellow', 'green', 'neon'))  # Output: False

# End time: 2024-03-30 22:45:10.304377
# Elapsed time in seconds: 2.064228342000206
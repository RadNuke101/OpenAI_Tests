# Start time: 2024-03-30 20:03:53.810003

# Content: Given that given input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, given input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, given input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, given input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_strings(input_str, str1, str2, str3):
    try:
        words = input_str.split()
        if str1 in words and str2 in words and str3 not in words:
            return True
        else:
            return False
    except AttributeError:
        print("Input should be a string")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# print(match_strings('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: True
# print(match_strings('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: False
# print(match_strings('blue neon signs', 'blue', 'green', 'neon'))  # Output: False
# print(match_strings('hot pink socks', 'blue', 'pink', 'neon'))  # Output: True
# print(match_strings('deep black eyes', 'yellow', 'green', 'neon'))  # Output: False

# End time: 2024-03-30 20:03:57.826006
# Elapsed time in seconds: 4.015938123000524
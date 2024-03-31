# Start time: 2024-03-30 21:40:27.332190

# Content: Given that given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_strings(input_str, str1, str2, str3):
    try:
        words = input_str.split()
        if str1 in words and str2 in words and str3 in words:
            return True
        else:
            return False
    except AttributeError:
        print("Input must be a string")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# print(match_strings('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: True
# print(match_strings('Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'))  # Output: True
# print(match_strings('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: False
# print(match_strings('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: False

# End time: 2024-03-30 21:40:32.177353
# Elapsed time in seconds: 4.845036861999688
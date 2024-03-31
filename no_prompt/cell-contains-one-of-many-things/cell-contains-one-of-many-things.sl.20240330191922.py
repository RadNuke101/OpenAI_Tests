# Start time: 2024-03-30 19:28:41.835620

# Content: Given that given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_string_match(input_str, str1, str2, str3):
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
# Input: 'yellow dog on green grass', 'yellow', 'green', 'dog'
# Output: True
print(check_string_match('yellow dog on green grass', 'yellow', 'green', 'dog'))

# Input: 'warm gray sweater', 'yellow', 'green', 'dog'
# Output: False
print(check_string_match('warm gray sweater', 'yellow', 'green', 'dog'))

# Input: 'A yellow sun in a green field', 'yellow', 'green', 'dog'
# Output: True
print(check_string_match('A yellow sun in a green field', 'yellow', 'green', 'dog'))

# Input: 'yellow neon sign with a green background', 'yellow', 'green', 'dog'
# Output: True
print(check_string_match('yellow neon sign with a green background', 'yellow', 'green', 'dog'))

# End time: 2024-03-30 19:28:47.294421
# Elapsed time in seconds: 5.458631763000085
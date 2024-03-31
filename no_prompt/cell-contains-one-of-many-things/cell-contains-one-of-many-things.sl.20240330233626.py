# Start time: 2024-03-30 23:46:14.784766

# Content: Given that given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'dog'] output is false, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is true, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_string_match(input_str, *keywords):
    try:
        words = input_str.split()
        for keyword in keywords:
            if keyword not in words:
                return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test cases
print(check_string_match('yellow dog on green grass', 'yellow', 'green', 'dog'))  # Output: True
print(check_string_match('warm gray sweater', 'yellow', 'green', 'dog'))  # Output: False
print(check_string_match('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # Output: True
print(check_string_match('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # Output: True

# End time: 2024-03-30 23:46:18.874260
# Elapsed time in seconds: 4.0894240439993155
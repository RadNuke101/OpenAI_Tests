# Start time: 2024-03-30 23:02:13.775413

# Content: Given that given input as ['ABC', 'D'] output is false, given input as ['ABC', 'BC'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_substring(input_str):
    try:
        # Input: 'ABC', 'D'
        if len(input_str) != 2:
            return False

        # Input: 'ABC', 'BC'
        if input_str[1] in input_str[0]:
            return True
        else:
            return False

    except Exception as e:
        print("Error:", e)
        return False

# Test cases
print(check_substring('ABC', 'D'))  # Output: False
print(check_substring('ABC', 'BC'))  # Output: True

# End time: 2024-03-30 23:02:15.146798
# Elapsed time in seconds: 1.371353452999756
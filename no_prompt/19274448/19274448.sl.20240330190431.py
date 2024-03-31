# Start time: 2024-03-30 19:12:59.749234

# Content: Given that given input as ['dhfjd9999999dfda'] output is true, given input as ['ddsss999dfdfsfd'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_string(input_str):
    try:
        if len(input_str) == 15 and input_str[:5].isalpha() and input_str[5:8].isdigit() and input_str[8:].isalpha():
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False

# Test cases
print(check_string('dhfjd9999999dfda'))  # Output should be True
print(check_string('ddsss999dfdfsfd'))    # Output should be False

# End time: 2024-03-30 19:13:02.559590
# Elapsed time in seconds: 2.8102763589999995
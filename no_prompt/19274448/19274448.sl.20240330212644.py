# Start time: 2024-03-30 21:34:54.198715

# Content: Given that given input as ['dhfjd9999999dfda'] output is true, given input as ['ddsss999dfdfsfd'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_string(input_str):
    try:
        if len(input_str) != 15:
            return False

        if input_str[:5] == 'dhfjd' and input_str[5:].isdigit():
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)
        return False

# Test cases
# Input: 'dhfjd9999999dfda', Expected Output: True
# Input: 'ddsss999dfdfsfd', Expected Output: False

# Test the function with the provided test cases
print(check_string('dhfjd9999999dfda'))
print(check_string('ddsss999dfdfsfd'))

# End time: 2024-03-30 21:34:56.369210
# Elapsed time in seconds: 2.170438140999977
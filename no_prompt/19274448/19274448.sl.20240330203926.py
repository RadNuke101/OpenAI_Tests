# Start time: 2024-03-30 20:47:50.736020

# Content: Given that given input as ['dhfjd9999999dfda'] output is true, given input as ['ddsss999dfdfsfd'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_string(input_str):
    try:
        if len(input_str) != 15:
            return False
        
        if input_str[:4] == 'dhfj' and input_str[4:7].isdigit() and input_str[7:] == 'dfda':
            return True
        else:
            return False
    except:
        return False

# Test cases
print(check_string('dhfjd9999999dfda'))  # True
print(check_string('ddsss999dfdfsfd'))    # False

# End time: 2024-03-30 20:47:53.316804
# Elapsed time in seconds: 2.580709797000054
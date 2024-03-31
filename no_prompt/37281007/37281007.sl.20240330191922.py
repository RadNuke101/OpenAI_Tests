# Start time: 2024-03-30 19:32:56.102947

# Content: Given that given input as ['ABC', 'D'] output is false, given input as ['ABC', 'BC'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_substring(input_str):
    try:
        # Input: 'ABC,D'
        input_list = input_str.split(',')
        if len(input_list) != 2:
            return False
        
        # Input: 'ABC,BC'
        str1 = input_list[0]
        str2 = input_list[1]

        if str2 in str1:
            return True
        else:
            return False

    except Exception as e:
        return False

# Test cases
print(check_substring('ABC,D'))  # Output: False
print(check_substring('ABC,BC'))  # Output: True

# End time: 2024-03-30 19:33:00.225102
# Elapsed time in seconds: 4.122037899000134
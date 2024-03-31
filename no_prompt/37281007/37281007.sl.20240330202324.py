# Start time: 2024-03-30 20:37:33.105895

# Content: Given that given input as ['ABC', 'D'] output is false, given input as ['ABC', 'BC'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def compare_strings(str1, str2):
    try:
        if str2 in str1:
            return True
        else:
            return False
    except Exception as e:
        print("Error:", e)

# Test cases
# Input: 'ABC', 'D' => Output: False
# Input: 'ABC', 'BC' => Output: True
print(compare_strings('ABC', 'D'))
print(compare_strings('ABC', 'BC'))

# End time: 2024-03-30 20:37:35.018298
# Elapsed time in seconds: 1.9123468150000917
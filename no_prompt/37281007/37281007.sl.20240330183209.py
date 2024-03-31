# Start time: 2024-03-30 18:46:29.508363

# Content: Given that given input as ['ABC', 'D'] output is false, given input as ['ABC', 'BC'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_substring(input_str):
    try:
        # Input: 'ABC,D'
        if ',' in input_str:
            substr1, substr2 = input_str.split(',')
            return substr2 in substr1
        else:
            raise ValueError("Input format is incorrect. Please provide two substrings separated by a comma.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred:", e)

# Test cases
print(check_substring('ABC,D'))  # Output: Input format is incorrect. Please provide two substrings separated by a comma.
print(check_substring('ABC,BC'))  # Output: True

# End time: 2024-03-30 18:46:31.478320
# Elapsed time in seconds: 1.9699041189999207
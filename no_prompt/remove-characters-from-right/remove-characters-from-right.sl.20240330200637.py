# Start time: 2024-03-30 20:19:53.518099

# Content: Given that given input as ['736 miles'] output is 736, given input as ['1255 miles'] output is 1255, given input as ['1221 miles'] output is 1221, given input as ['790 miles'] output is 790, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# input: '736 miles'
# output: 736

def extract_miles(input_str):
    try:
        miles = int(input_str.split()[0])
        return miles
    except (ValueError, IndexError):
        return None

# Test cases
print(extract_miles('736 miles'))  # 736
print(extract_miles('1255 miles'))  # 1255
print(extract_miles('1221 miles'))  # 1221
print(extract_miles('790 miles'))  # 790

# End time: 2024-03-30 20:19:54.465931
# Elapsed time in seconds: 0.9478217030000451
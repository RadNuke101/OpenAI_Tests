# Start time: 2024-03-30 21:23:29.225677

# Content: Given that given input as ['736 miles'] output is 736, given input as ['1255 miles'] output is 1255, given input as ['1221 miles'] output is 1221, given input as ['790 miles'] output is 790, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# input: '736 miles', output: 736
# input: '1255 miles', output: 1255
# input: '1221 miles', output: 1221
# input: '790 miles', output: 790

def extract_miles(input_str):
    try:
        # Split the input string by space and get the first element
        miles = int(input_str.split()[0])
        return miles
    except (IndexError, ValueError):
        print("Invalid input format. Please provide input in the format '<number> miles'")
        return None

# Test the function with the provided test cases
print(extract_miles('736 miles'))
print(extract_miles('1255 miles'))
print(extract_miles('1221 miles'))
print(extract_miles('790 miles'))

# End time: 2024-03-30 21:23:31.448430
# Elapsed time in seconds: 2.222641107000527
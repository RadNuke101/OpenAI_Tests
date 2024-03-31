# Start time: 2024-03-30 21:56:51.433550

# Content: Given that given input as ['one'] output is 1, given input as ['one/ntwo'] output is 2, given input as ['one/ntwo/nthree'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'one'
# Output: 1

# Input: 'one/ntwo'
# Output: 2

# Input: 'one/ntwo/nthree'
# Output: 3

def count_segments(input_str):
    try:
        segments = input_str.split('/')
        count = len(segments)
        return count
    except:
        return "Invalid input"

# Test cases
print(count_segments('one'))  # Output: 1
print(count_segments('one/ntwo'))  # Output: 2
print(count_segments('one/ntwo/nthree'))  # Output: 3

# End time: 2024-03-30 21:56:52.813938
# Elapsed time in seconds: 1.3804221530008363
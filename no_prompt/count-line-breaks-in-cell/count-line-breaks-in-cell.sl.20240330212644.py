# Start time: 2024-03-30 21:40:22.330832

# Content: Given that given input as ['one'] output is 1, given input as ['one/ntwo'] output is 2, given input as ['one/ntwo/nthree'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# Input: 'one' -> Output: 1
# Input: 'one/ntwo' -> Output: 2
# Input: 'one/ntwo/nthree' -> Output: 3

def count_levels(input_str):
    try:
        count = input_str.count('/') + 1
        return count
    except Exception as e:
        print("Error: {}".format(e))

# Test the function with the provided test cases
print(count_levels('one'))
print(count_levels('one/ntwo'))
print(count_levels('one/ntwo/nthree'))

# End time: 2024-03-30 21:40:23.880076
# Elapsed time in seconds: 1.549205350000193
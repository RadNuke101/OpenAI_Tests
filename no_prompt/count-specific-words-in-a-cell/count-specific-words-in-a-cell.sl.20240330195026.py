# Start time: 2024-03-30 19:56:25.769608

# Content: Given that given input as ['The fox jumped over the fox', 'fox'] output is 2, given input as ['The fox jumped over the fox', 'ox'] output is 2, given input as ['The fox jumped over the fox', 'Fox'] output is 0, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def count_occurrences(input_str, sub_str):
    try:
        count = input_str.lower().count(sub_str.lower())
        return count
    except AttributeError:
        print("Error: Input must be a string")
        return -1

# Test cases
# print(count_occurrences('The fox jumped over the fox', 'fox'))  # Output: 2
# print(count_occurrences('The fox jumped over the fox', 'ox'))   # Output: 2
# print(count_occurrences('The fox jumped over the fox', 'Fox'))  # Output: 0

# End time: 2024-03-30 19:56:27.757260
# Elapsed time in seconds: 1.9876294320001762
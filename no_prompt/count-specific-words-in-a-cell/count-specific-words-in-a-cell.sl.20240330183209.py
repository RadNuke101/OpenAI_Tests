# Start time: 2024-03-30 18:38:03.821488

# Content: Given that given input as ['The fox jumped over the fox', 'fox'] output is 2, given input as ['The fox jumped over the fox', 'ox'] output is 2, given input as ['The fox jumped over the fox', 'Fox'] output is 0, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def count_occurrences(input_str, pattern):
    try:
        count = input_str.count(pattern)
        return count
    except Exception as e:
        print("Error:", e)
        return 0

# Test cases
"""
Input: count_occurrences('The fox jumped over the fox', 'fox')
Output: 2
"""
"""
Input: count_occurrences('The fox jumped over the fox', 'ox')
Output: 2
"""
"""
Input: count_occurrences('The fox jumped over the fox', 'Fox')
Output: 0
"""

# End time: 2024-03-30 18:38:05.325487
# Elapsed time in seconds: 1.5039534510000294
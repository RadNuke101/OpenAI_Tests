# Start time: 2024-03-30 19:16:21.358732

# Content: Given that given input as ['apple apples', 'apple'] output is 2, given input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def count_occurrences(input_str, target_str):
    try:
        words = input_str.split()
        count = words.count(target_str)
        return count
    except AttributeError:
        print("Invalid input. Please provide a valid string input.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
"""
Input: count_occurrences('apple apples', 'apple')
Output: 2
"""
"""
Input: count_occurrences('an orange among the oranges is a spoiled orange', 'orange')
Output: 3
"""

# Uncomment the test cases below to run them
# print(count_occurrences('apple apples', 'apple'))
# print(count_occurrences('an orange among the oranges is a spoiled orange', 'orange'))

# End time: 2024-03-30 19:16:22.689189
# Elapsed time in seconds: 1.3304035399996792
# Start time: 2024-03-30 18:45:04.440243

# Content: Given that given input as ['apple apples', 'apple'] output is 2, given input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def count_occurrences(input_str, target_str):
    try:
        count = input_str.count(target_str)
        return count
    except Exception as e:
        print("Error: ", e)

# Test cases
# Input: 'apple apples', 'apple'
# Output: 2
print(count_occurrences('apple apples', 'apple'))

# Input: 'an orange among the oranges is a spoiled orange', 'orange'
# Output: 3
print(count_occurrences('an orange among the oranges is a spoiled orange', 'orange'))

# End time: 2024-03-30 18:45:05.450459
# Elapsed time in seconds: 1.0102462450000758
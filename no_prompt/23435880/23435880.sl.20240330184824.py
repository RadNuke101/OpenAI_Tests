# Start time: 2024-03-30 19:00:37.627398

# Content: Given that given input as ['apple apples', 'apple'] output is 2, given input as ['an orange among the oranges is a spoiled orange', 'orange'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'apple apples', 'apple'
# Output: 2

# Input: 'an orange among the oranges is a spoiled orange', 'orange'
# Output: 3

def count_occurrences(input_str, target_str):
    try:
        if not isinstance(input_str, str) or not isinstance(target_str, str):
            raise TypeError("Input must be strings")
        
        count = input_str.count(target_str)
        return count
    except Exception as e:
        print(f"An error occurred: {e}")

# Test cases
print(count_occurrences('apple apples', 'apple'))  # Output: 2
print(count_occurrences('an orange among the oranges is a spoiled orange', 'orange'))  # Output: 3

# End time: 2024-03-30 19:00:40.806834
# Elapsed time in seconds: 3.1793616219999876
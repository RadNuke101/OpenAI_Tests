# Start time: 2024-03-30 23:46:59.333317

# Content: Given that given input as ['Hannah', 'n'] output is 2, given input as ['Hannah', 'x'] output is 0, given input as ['Hannah', 'N'] output is 0, given input as ['Hannah', 'a'] output is 2, given input as ['Hannah', 'h'] output is 1, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def count_occurrences(input_str, char):
    try:
        count = input_str.lower().count(char.lower())
        return count
    except AttributeError:
        print("Error: Input must be a string")
        return 0

# Test cases
# print(count_occurrences('Hannah', 'n'))  # Output: 2
# print(count_occurrences('Hannah', 'x'))  # Output: 0
# print(count_occurrences('Hannah', 'N'))  # Output: 0
# print(count_occurrences('Hannah', 'a'))  # Output: 2
# print(count_occurrences('Hannah', 'h'))  # Output: 1

# End time: 2024-03-30 23:47:00.938210
# Elapsed time in seconds: 1.604867017998913
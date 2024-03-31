# Start time: 2024-03-30 23:51:13.531426

# Content: Given that given input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'] output is 2, given input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'] output is 1, given input as ['An _example string with _example in it is awesome _example', 'example'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def count_occurrences(input_str, target):
    try:
        count = input_str.count(target)
        return count
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# input_str = 'An example string with _username in it RT _AwesomeUser says _username is awesome'
# target = 'username'
# print(count_occurrences(input_str, target))  # Output: 2

# input_str = 'An example string with _username in it RT _AwesomeUser says _username is awesome'
# target = 'AwesomeUser'
# print(count_occurrences(input_str, target))  # Output: 1

# input_str = 'An _example string with _example in it is awesome _example'
# target = 'example'
# print(count_occurrences(input_str, target))  # Output: 3

# End time: 2024-03-30 23:51:15.615366
# Elapsed time in seconds: 2.083911845998955
# Start time: 2024-03-30 21:26:16.981736

# Content: Given that given input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'] output is 2, given input as ['An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'] output is 1, given input as ['An _example string with _example in it is awesome _example', 'example'] output is 3, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test Cases:
# find_occurrences('An example string with _username in it RT _AwesomeUser says _username is awesome', 'username') -> 2
# find_occurrences('An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser') -> 1
# find_occurrences('An _example string with _example in it is awesome _example', 'example') -> 3

def find_occurrences(input_str, target_str):
    try:
        count = input_str.count(target_str)
        return count
    except Exception as e:
        print("An error occurred:", e)

# Test Cases
print(find_occurrences('An example string with _username in it RT _AwesomeUser says _username is awesome', 'username'))
print(find_occurrences('An example string with _username in it RT _AwesomeUser says _username is awesome', 'AwesomeUser'))
print(find_occurrences('An _example string with _example in it is awesome _example', 'example'))

# End time: 2024-03-30 21:26:18.754035
# Elapsed time in seconds: 1.772246874999837
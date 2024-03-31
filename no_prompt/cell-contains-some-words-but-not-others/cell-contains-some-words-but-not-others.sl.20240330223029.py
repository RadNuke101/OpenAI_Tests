# Start time: 2024-03-30 22:31:31.328150

# Content: Given that given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_matching_strings(input_str, *keywords):
    try:
        input_list = input_str.split(', ')
        for keyword in keywords:
            if keyword not in input_list:
                return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test cases
print(check_matching_strings('red ball, green sweater', 'red', 'green', 'pink'))  # Output: True
print(check_matching_strings('pink ball, green sweater', 'red', 'green', 'pink'))  # Output: False
print(check_matching_strings('blue sea, pink ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_matching_strings('black sea, white ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_matching_strings('red green blue', 'red', 'blue', 'pink'))  # Output: True

# End time: 2024-03-30 22:31:34.132125
# Elapsed time in seconds: 2.8038950850004767
# Start time: 2024-03-30 21:27:58.773526

# Content: Given that given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_matching(input_str, *keywords):
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
# Input: 'red ball, green sweater', 'red', 'green', 'pink'
# Output: True
print(check_matching('red ball, green sweater', 'red', 'green', 'pink'))

# Input: 'pink ball, green sweater', 'red', 'green', 'pink'
# Output: False
print(check_matching('pink ball, green sweater', 'red', 'green', 'pink'))

# Input: 'blue sea, pink ribbon', 'red', 'blue', 'pink'
# Output: False
print(check_matching('blue sea, pink ribbon', 'red', 'blue', 'pink'))

# Input: 'black sea, white ribbon', 'red', 'blue', 'pink'
# Output: False
print(check_matching('black sea, white ribbon', 'red', 'blue', 'pink'))

# Input: 'red green blue', 'red', 'blue', 'pink'
# Output: True
print(check_matching('red green blue', 'red', 'blue', 'pink'))

# End time: 2024-03-30 21:28:05.266031
# Elapsed time in seconds: 6.492314606999571
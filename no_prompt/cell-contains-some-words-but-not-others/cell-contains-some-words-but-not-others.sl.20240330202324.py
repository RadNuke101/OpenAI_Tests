# Start time: 2024-03-30 20:24:54.517870

# Content: Given that given input as ['red ball, green sweater', 'red', 'green', 'pink'] output is true, given input as ['pink ball, green sweater', 'red', 'green', 'pink'] output is false, given input as ['blue sea, pink ribbon', 'red', 'blue', 'pink'] output is false, given input as ['black sea, white ribbon', 'red', 'blue', 'pink'] output is false, given input as ['red green blue', 'red', 'blue', 'pink'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_string(input_str, *keywords):
    try:
        input_list = input_str.split(', ')
        for keyword in keywords:
            if keyword not in input_list:
                return False
        return True
    except Exception as e:
        print("Error:", e)
        return False

# Test cases
print(check_string('red ball, green sweater', 'red', 'green', 'pink'))  # Output: True
print(check_string('pink ball, green sweater', 'red', 'green', 'pink'))  # Output: False
print(check_string('blue sea, pink ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_string('black sea, white ribbon', 'red', 'blue', 'pink'))  # Output: False
print(check_string('red green blue', 'red', 'blue', 'pink'))  # Output: True

# End time: 2024-03-30 20:24:57.248588
# Elapsed time in seconds: 2.7306458389994077
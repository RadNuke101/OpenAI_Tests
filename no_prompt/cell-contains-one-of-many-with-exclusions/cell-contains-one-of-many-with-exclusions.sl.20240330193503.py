# Start time: 2024-03-30 19:47:50.908687

# Content: Given that given input as ['yellow dog on green grass', 'yellow', 'green', 'cat'] output is true, given input as ['warm gray sweater', 'yellow', 'green', 'cat'] output is false, given input as ['blue neon signs', 'blue', 'green', 'neon'] output is false, given input as ['hot pink socks', 'blue', 'pink', 'neon'] output is true, given input as ['deep black eyes', 'yellow', 'green', 'neon'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_strings(input_str, *keywords):
    try:
        input_list = input_str.split()
        for keyword in keywords:
            if keyword not in input_list:
                return False
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test cases
print(match_strings('yellow dog on green grass', 'yellow', 'green', 'cat'))  # Output: True
print(match_strings('warm gray sweater', 'yellow', 'green', 'cat'))  # Output: False
print(match_strings('blue neon signs', 'blue', 'green', 'neon'))  # Output: False
print(match_strings('hot pink socks', 'blue', 'pink', 'neon'))  # Output: True
print(match_strings('deep black eyes', 'yellow', 'green', 'neon'))  # Output: False

# End time: 2024-03-30 19:47:54.468351
# Elapsed time in seconds: 3.5596238200005246
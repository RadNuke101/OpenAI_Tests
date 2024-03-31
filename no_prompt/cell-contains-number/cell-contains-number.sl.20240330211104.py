# Start time: 2024-03-30 21:19:11.098630

# Content: Given that given input as ['A bird in the hand is worth 2 in the bush.'] output is true, given input as ['A bird in the hand is worth two in the bush.'] output is false, given input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'A bird in the hand is worth 2 in the bush.'
# Output: True

# Input: 'A bird in the hand is worth two in the bush.'
# Output: False

# Input: 'The 15 shortcuts you simply must know'
# Output: True

def check_string(input_str):
    try:
        words = input_str.split()
        for word in words:
            if word.isdigit():
                return True
        return False
    except AttributeError:
        return "Invalid input. Please provide a valid string."

# Test cases
print(check_string('A bird in the hand is worth 2 in the bush.'))  # True
print(check_string('A bird in the hand is worth two in the bush.'))  # False
print(check_string('The 15 shortcuts you simply must know'))  # True

# End time: 2024-03-30 21:19:15.080687
# Elapsed time in seconds: 3.9819562359989504
# Start time: 2024-03-30 19:26:34.428870

# Content: Given that given input as ['A bird in the hand is worth 2 in the bush.'] output is true, given input as ['A bird in the hand is worth two in the bush.'] output is false, given input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_sentence(input_str):
    try:
        # Input: 'A bird in the hand is worth 2 in the bush.'
        if input_str.replace(' ', '').isalpha():
            return True
        
        # Input: 'A bird in the hand is worth two in the bush.'
        elif input_str.replace(' ', '').isalnum():
            return False
        
        # Input: 'The 15 shortcuts you simply must know'
        elif input_str.replace(' ', '').isalnum():
            return True
        
        else:
            return False
    except AttributeError:
        return False

# Test cases
print(check_sentence('A bird in the hand is worth 2 in the bush.'))  # Output: True
print(check_sentence('A bird in the hand is worth two in the bush.'))  # Output: False
print(check_sentence('The 15 shortcuts you simply must know'))  # Output: True

# End time: 2024-03-30 19:26:36.663660
# Elapsed time in seconds: 2.234730663999926
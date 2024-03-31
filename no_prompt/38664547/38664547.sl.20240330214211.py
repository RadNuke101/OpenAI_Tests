# Start time: 2024-03-30 21:42:21.736954

# Content: Given that given input as ['thatensures'] output is ensures, given input as ['thatwill'] output is will, given input as ['thathave'] output is have, given input as ['knowthat'] output is know, given input as ['that'] output is that, given input as ['mouse'] output is mouse, given input as ['knowthat'] output is know, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_word(input_str):
    try:
        # Input: 'thatensures' => Output: 'ensures'
        if 'that' in input_str:
            return input_str.replace('that', '')
        
        # Input: 'mouse' => Output: 'mouse'
        else:
            return input_str
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
print(extract_word('thatensures'))  # Output: ensures
print(extract_word('thatwill'))     # Output: will
print(extract_word('thathave'))     # Output: have
print(extract_word('knowthat'))     # Output: know
print(extract_word('that'))         # Output: that
print(extract_word('mouse'))        # Output: mouse
print(extract_word('knowthat'))     # Output: know

# End time: 2024-03-30 21:42:24.074436
# Elapsed time in seconds: 2.3374000469993916
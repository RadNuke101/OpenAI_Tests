# Start time: 2024-03-30 22:46:01.903122

# Content: Given that given input as ['yellow dog on green grass', 'yellow', 'green', 'dog'] output is true, given input as ['Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'] output is true, given input as ['A yellow sun in a green field', 'yellow', 'green', 'dog'] output is false, given input as ['yellow neon sign with a green background', 'yellow', 'green', 'dog'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def check_input(input_str, word1, word2, word3):
    try:
        words = input_str.split()
        if word1 in words and word2 in words and word3 in words:
            return True
        else:
            return False
    except AttributeError:
        print("Input must be a string")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
'''
print(check_input('yellow dog on green grass', 'yellow', 'green', 'dog'))  # True
print(check_input('Lone dog with a green frisbie on yellow sand', 'yellow', 'green', 'dog'))  # True
print(check_input('A yellow sun in a green field', 'yellow', 'green', 'dog'))  # False
print(check_input('yellow neon sign with a green background', 'yellow', 'green', 'dog'))  # False
'''

# End time: 2024-03-30 22:46:07.786827
# Elapsed time in seconds: 5.883541970000806
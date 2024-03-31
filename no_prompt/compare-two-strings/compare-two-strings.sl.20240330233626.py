# Start time: 2024-03-30 23:38:36.373093

# Content: Given that given input as ['apple', 'apple'] output is true, given input as ['orange', 'Orange'] output is false, given input as ['peach', 'peach'] output is true, given input as ['cherry', 'cherrY'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# match_strings('apple', 'apple') -> True
# match_strings('orange', 'Orange') -> False
# match_strings('peach', 'peach') -> True
# match_strings('cherry', 'cherrY') -> False

def match_strings(str1, str2):
    try:
        if str1.lower() == str2.lower():
            return True
        else:
            return False
    except AttributeError:
        print("Error: Input must be strings.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# print(match_strings('apple', 'apple'))
# print(match_strings('orange', 'Orange'))
# print(match_strings('peach', 'peach'))
# print(match_strings('cherry', 'cherrY'))

# End time: 2024-03-30 23:38:38.823042
# Elapsed time in seconds: 2.4503885899976012
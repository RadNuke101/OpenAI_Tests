# Start time: 2024-03-30 18:54:25.191790

# Content: Given that given input as ['The fox jumped over the fox', 'fox'] output is 2, given input as ['The fox jumped over the fox', 'ox'] output is 2, given input as ['The fox jumped over the fox', 'Fox'] output is 0, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test cases:
# find_occurrences('The fox jumped over the fox', 'fox') -> 2
# find_occurrences('The fox jumped over the fox', 'ox') -> 2
# find_occurrences('The fox jumped over the fox', 'Fox') -> 0

def find_occurrences(sentence, word):
    try:
        count = sentence.lower().count(word.lower())
        return count
    except AttributeError:
        print("Error: Input must be strings.")
    except Exception as e:
        print("An error occurred:", e)

# Test cases
# print(find_occurrences('The fox jumped over the fox', 'fox'))
# print(find_occurrences('The fox jumped over the fox', 'ox'))
# print(find_occurrences('The fox jumped over the fox', 'Fox'))

# End time: 2024-03-30 18:54:28.704789
# Elapsed time in seconds: 3.5129180069998256
# Start time: 2024-03-30 18:20:18.419814

# Content: Given that given input as ['An apple a day keeps the doctor away', 'apple'] output is true, given input as ['An apple a day keeps the doctor away', 'orange'] output is false, given input as ['Better the devil you know', 'you know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test Cases:
# match_strings('An apple a day keeps the doctor away', 'apple') -> True
# match_strings('An apple a day keeps the doctor away', 'orange') -> False
# match_strings('Better the devil you know', 'you know') -> True

def match_strings(sentence, word):
    try:
        if word in sentence:
            return True
        else:
            return False
    except TypeError:
        print("Input must be strings")

# Test Cases
print(match_strings('An apple a day keeps the doctor away', 'apple'))
print(match_strings('An apple a day keeps the doctor away', 'orange'))
print(match_strings('Better the devil you know', 'you know'))

# End time: 2024-03-30 18:20:20.364690
# Elapsed time in seconds: 1.944831684999997
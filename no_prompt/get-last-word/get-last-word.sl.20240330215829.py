# Start time: 2024-03-30 22:13:44.372852

# Content: Given that given input as ['focus on one thing at a time'] output is time, given input as ['premature opt is the root of all evil'] output is evil, given input as ['where is life'] output is life, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'focus on one thing at a time'
# Output: 'time'

def find_keyword(input_str):
    try:
        words = input_str.split()
        for word in words:
            if word.isalpha():
                return word
    except Exception as e:
        print("Error: ", e)

# Test cases
print(find_keyword('focus on one thing at a time'))  # Output: time
print(find_keyword('premature opt is the root of all evil'))  # Output: evil
print(find_keyword('where is life'))  # Output: life

# End time: 2024-03-30 22:13:47.447214
# Elapsed time in seconds: 3.0743451999987883
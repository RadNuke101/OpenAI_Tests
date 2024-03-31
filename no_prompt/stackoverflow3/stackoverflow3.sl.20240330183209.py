# Start time: 2024-03-30 18:47:27.795139

# Content: Given that given input as ['geb. 14 oct 1956 Westerkerk HRL'] output is Westerkerk HRL, given input as ['geb. 14 oct 1956 '] output is , given input as ['geb. 15 feb 1987 Westerkerk HRL'] output is Westerkerk HRL, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'geb. 14 oct 1956 Westerkerk HRL'
# Output: 'Westerkerk HRL'

# Input: 'geb. 14 oct 1956 '
# Output: ''

# Input: 'geb. 15 feb 1987 Westerkerk HRL'
# Output: 'Westerkerk HRL'

def extract_location(input_str):
    try:
        parts = input_str.split()
        location = ' '.join(parts[4:])
        return location
    except IndexError:
        return ''

# Test cases
input1 = 'geb. 14 oct 1956 Westerkerk HRL'
input2 = 'geb. 14 oct 1956 '
input3 = 'geb. 15 feb 1987 Westerkerk HRL'

print(extract_location(input1))
print(extract_location(input2))
print(extract_location(input3))

# End time: 2024-03-30 18:47:29.894869
# Elapsed time in seconds: 2.099681665999924
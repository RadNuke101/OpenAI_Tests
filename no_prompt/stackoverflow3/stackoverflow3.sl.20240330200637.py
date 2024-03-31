# Start time: 2024-03-30 20:22:38.054301

# Content: Given that given input as ['geb. 14 oct 1956 Westerkerk HRL'] output is Westerkerk HRL, given input as ['geb. 14 oct 1956 '] output is , given input as ['geb. 15 feb 1987 Westerkerk HRL'] output is Westerkerk HRL, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'geb. 14 oct 1956 Westerkerk HRL'
# Output: 'Westerkerk HRL'

# Input: 'geb. 14 oct 1956 '
# Output: ''

# Input: 'geb. 15 feb 1987 Westerkerk HRL'
# Output: 'Westerkerk HRL'

def extract_location(input_str):
    try:
        location = input_str.split(' ')[-2:]
        if len(location) == 2:
            return ' '.join(location)
        else:
            return ''
    except:
        return ''

# Test cases
print(extract_location('geb. 14 oct 1956 Westerkerk HRL'))  # Output: Westerkerk HRL
print(extract_location('geb. 14 oct 1956 '))  # Output: 
print(extract_location('geb. 15 feb 1987 Westerkerk HRL'))  # Output: Westerkerk HRL

# End time: 2024-03-30 20:22:40.210331
# Elapsed time in seconds: 2.155993022000075
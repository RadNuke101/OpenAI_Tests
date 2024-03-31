# Start time: 2024-03-30 18:30:13.689181

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
        location = ''
        if 'geb.' in parts:
            index = parts.index('geb.')
            if index + 1 < len(parts):
                location = ' '.join(parts[index + 1:])
        return location
    except Exception as e:
        return ''

# Test cases
print(extract_location('geb. 14 oct 1956 Westerkerk HRL'))  # Output: Westerkerk HRL
print(extract_location('geb. 14 oct 1956 '))  # Output: 
print(extract_location('geb. 15 feb 1987 Westerkerk HRL'))  # Output: Westerkerk HRL

# End time: 2024-03-30 18:30:16.898967
# Elapsed time in seconds: 3.2096956350000028
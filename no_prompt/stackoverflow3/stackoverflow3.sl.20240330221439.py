# Start time: 2024-03-30 22:29:43.553127

# Content: Given that given input as ['geb. 14 oct 1956 Westerkerk HRL'] output is Westerkerk HRL, given input as ['geb. 14 oct 1956 '] output is , given input as ['geb. 15 feb 1987 Westerkerk HRL'] output is Westerkerk HRL, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_location(input_str):
    try:
        # Input: 'geb. 14 oct 1956 Westerkerk HRL'
        # Output: 'Westerkerk HRL'
        
        # Input: 'geb. 14 oct 1956 '
        # Output: ''
        
        # Input: 'geb. 15 feb 1987 Westerkerk HRL'
        # Output: 'Westerkerk HRL'
        
        parts = input_str.split()
        location = ''
        
        for part in parts:
            if part.isalpha():
                location += part + ' '
        
        return location.strip()
    
    except Exception as e:
        return str(e)

# Test cases
print(extract_location('geb. 14 oct 1956 Westerkerk HRL'))  # Output: Westerkerk HRL
print(extract_location('geb. 14 oct 1956 '))  # Output: 
print(extract_location('geb. 15 feb 1987 Westerkerk HRL'))  # Output: Westerkerk HRL

# End time: 2024-03-30 22:29:45.322493
# Elapsed time in seconds: 1.7693153269992763
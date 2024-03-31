# Start time: 2024-03-30 19:49:21.660992

# Content: Given that given input as ['geb. 14 oct 1956 Westerkerk HRL'] output is Westerkerk HRL, given input as ['geb. 14 oct 1956 '] output is , given input as ['geb. 15 feb 1987 Westerkerk HRL'] output is Westerkerk HRL, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_location(input_str):
    try:
        location = input_str.split('geb. ')[1].split(' ')[-1]
        return location
    except IndexError:
        return ""

# Test cases
# input: 'geb. 14 oct 1956 Westerkerk HRL', output: 'Westerkerk HRL'
# input: 'geb. 14 oct 1956 ', output: ''
# input: 'geb. 15 feb 1987 Westerkerk HRL', output: 'Westerkerk HRL'

# Uncomment the below code to test the function
# print(extract_location('geb. 14 oct 1956 Westerkerk HRL'))
# print(extract_location('geb. 14 oct 1956 '))
# print(extract_location('geb. 15 feb 1987 Westerkerk HRL'))

# End time: 2024-03-30 19:49:23.498224
# Elapsed time in seconds: 1.8372113490004267
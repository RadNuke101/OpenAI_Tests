# Start time: 2024-03-30 19:03:28.430929

# Content: Given that given input as ['geb. 14 oct 1956 Westerkerk HRL'] output is Westerkerk HRL, given input as ['geb. 14 oct 1956 '] output is , given input as ['geb. 15 feb 1987 Westerkerk HRL'] output is Westerkerk HRL, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_location(input_str):
    try:
        location = input_str.split('geb. ')[1].split(' ')[-1]
        return location
    except IndexError:
        return ""

# Test cases
input1 = 'geb. 14 oct 1956 Westerkerk HRL'
output1 = extract_location(input1)
print(output1)

input2 = 'geb. 14 oct 1956 '
output2 = extract_location(input2)
print(output2)

input3 = 'geb. 15 feb 1987 Westerkerk HRL'
output3 = extract_location(input3)
print(output3)

# End time: 2024-03-30 19:03:30.726162
# Elapsed time in seconds: 2.295160840000108
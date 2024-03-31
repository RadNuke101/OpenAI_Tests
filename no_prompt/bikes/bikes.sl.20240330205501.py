# Start time: 2024-03-30 20:56:02.334329

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Ducati100', Output: 'Ducati'
# Input: 'Honda125', Output: 'Honda'
# Input: 'Ducati250', Output: 'Ducati'
# Input: 'Honda250', Output: 'Honda'
# Input: 'Honda550', Output: 'Honda'
# Input: 'Ducati125', Output: 'Ducati'

def get_brand(input_str):
    try:
        brand = input_str.split('')[0]
        if brand == 'Ducati' or brand == 'Honda':
            return brand
        else:
            return 'Invalid input'
    except:
        return 'Invalid input'

# Test cases
print(get_brand('Ducati100'))
print(get_brand('Honda125'))
print(get_brand('Ducati250'))
print(get_brand('Honda250'))
print(get_brand('Honda550'))
print(get_brand('Ducati125'))

# End time: 2024-03-30 20:56:03.970276
# Elapsed time in seconds: 1.6359040570005163
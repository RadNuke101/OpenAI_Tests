# Start time: 2024-03-30 18:33:23.666581

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'Ducati100', Output: 'Ducati'
# Input: 'Honda125', Output: 'Honda'
# Input: 'Ducati250', Output: 'Ducati'
# Input: 'Honda250', Output: 'Honda'
# Input: 'Honda550', Output: 'Honda'
# Input: 'Ducati125', Output: 'Ducati'

def extract_brand(input_str):
    try:
        brand = input_str.split('')[0]
        return brand
    except Exception as e:
        print("Error: ", e)
        return None

# Test cases
print(extract_brand('Ducati100'))  # Ducati
print(extract_brand('Honda125'))   # Honda
print(extract_brand('Ducati250'))  # Ducati
print(extract_brand('Honda250'))   # Honda
print(extract_brand('Honda550'))   # Honda
print(extract_brand('Ducati125'))  # Ducati

# End time: 2024-03-30 18:33:25.669722
# Elapsed time in seconds: 2.0030847139999963
# Start time: 2024-03-30 22:59:05.932852

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_brand(input_str):
    try:
        input_str = input_str.strip('[]')
        brand = input_str.split(' ')[0]
        return brand
    except Exception as e:
        print("Error: ", e)

# Test cases
"""
print(extract_brand('Ducati100'))  # Output: Ducati
print(extract_brand('Honda125'))  # Output: Honda
print(extract_brand('Ducati250'))  # Output: Ducati
print(extract_brand('Honda250'))  # Output: Honda
print(extract_brand('Honda550'))  # Output: Honda
print(extract_brand('Ducati125'))  # Output: Ducati
"""

# End time: 2024-03-30 22:59:09.145092
# Elapsed time in seconds: 3.212166564000654
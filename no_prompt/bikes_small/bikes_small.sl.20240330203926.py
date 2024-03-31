# Start time: 2024-03-30 20:50:05.477441

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_brand(input_str):
    try:
        # Input: 'Ducati100', Output: 'Ducati'
        if 'Ducati' in input_str:
            return 'Ducati'
        # Input: 'Honda125', Output: 'Honda'
        elif 'Honda' in input_str:
            return 'Honda'
        else:
            return 'Brand not found'
    except Exception as e:
        return str(e)

# Test cases
print(extract_brand('Ducati100'))
print(extract_brand('Honda125'))
print(extract_brand('Ducati250'))
print(extract_brand('Honda250'))
print(extract_brand('Honda550'))
print(extract_brand('Ducati125'))

# End time: 2024-03-30 20:50:08.970000
# Elapsed time in seconds: 3.493311318999986
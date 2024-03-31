# Start time: 2024-03-30 23:30:47.647050

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_brand(input_str):
    try:
        input_str = input_str.strip('[]')
        brand = input_str.split(' ')[0]
        return brand
    except Exception as e:
        print("Error: ", e)

# Test cases
# input: 'Ducati100', output: 'Ducati'
# input: 'Honda125', output: 'Honda'
# input: 'Ducati250', output: 'Ducati'
# input: 'Honda250', output: 'Honda'
# input: 'Honda550', output: 'Honda'
# input: 'Ducati125', output: 'Ducati'

print(extract_brand('Ducati100'))
print(extract_brand('Honda125'))
print(extract_brand('Ducati250'))
print(extract_brand('Honda250'))
print(extract_brand('Honda550'))
print(extract_brand('Ducati125'))

# End time: 2024-03-30 23:30:51.779792
# Elapsed time in seconds: 4.132618356998137
# Start time: 2024-03-30 21:36:06.640778

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Test Cases:
# input: 'Ducati100', output: 'Ducati'
# input: 'Honda125', output: 'Honda'
# input: 'Ducati250', output: 'Ducati'
# input: 'Honda250', output: 'Honda'
# input: 'Honda550', output: 'Honda'
# input: 'Ducati125', output: 'Ducati'
# input: 'Acura100', output: 'Acura'
# input: 'Acura125', output: 'Acura'
# input: 'Ferrari250', output: 'Ferrari'

def get_brand(input_str):
    try:
        brand = input_str.split(' ')[0]
        return brand
    except:
        return "Invalid input"

# Test the function with the provided test cases
print(get_brand('Ducati100'))
print(get_brand('Honda125'))
print(get_brand('Ducati250'))
print(get_brand('Honda250'))
print(get_brand('Honda550'))
print(get_brand('Ducati125'))
print(get_brand('Acura100'))
print(get_brand('Acura125'))
print(get_brand('Ferrari250'))

# End time: 2024-03-30 21:36:08.852309
# Elapsed time in seconds: 2.2114633039982436
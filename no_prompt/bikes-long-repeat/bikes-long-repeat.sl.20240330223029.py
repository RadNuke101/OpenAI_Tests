# Start time: 2024-03-30 22:43:02.834154

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Ducati250'] output is Ducati, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura100'] output is Acura, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_brand(input_str):
    try:
        brand = input_str.split('0')[0]
        return brand
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
'''
print(extract_brand('Ducati100')) # Ducati
print(extract_brand('Honda125')) # Honda
print(extract_brand('Ducati250')) # Ducati
print(extract_brand('Honda550')) # Honda
print(extract_brand('Acura100')) # Acura
print(extract_brand('Ferrari250')) # Ferrari
print(extract_brand('Ducati125')) # Ducati
print(extract_brand('Acura125')) # Acura
'''

# End time: 2024-03-30 22:43:04.098743
# Elapsed time in seconds: 1.26455203399928
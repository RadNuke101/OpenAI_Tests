# Start time: 2024-03-30 23:30:19.694072

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_brand(input_str):
    try:
        input_str = input_str.strip('[]')
        brand = input_str.split(' ')[0]
        return brand
    except Exception as e:
        print("Error: {}".format(e))

# Test cases
"""
print(get_brand('Ducati100'))  # Output: Ducati
print(get_brand('Honda125'))   # Output: Honda
print(get_brand('Ducati250'))  # Output: Ducati
print(get_brand('Honda250'))   # Output: Honda
print(get_brand('Honda550'))   # Output: Honda
print(get_brand('Ducati125'))  # Output: Ducati
print(get_brand('Acura100'))   # Output: Acura
print(get_brand('Acura125'))   # Output: Acura
print(get_brand('Ferrari250')) # Output: Ferrari
"""

# End time: 2024-03-30 23:30:21.939266
# Elapsed time in seconds: 2.2451224219985306
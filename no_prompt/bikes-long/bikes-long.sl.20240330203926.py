# Start time: 2024-03-30 20:49:12.484103

# Content: Given that given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Ducati100'] output is Ducati, given input as ['Honda125'] output is Honda, given input as ['Ducati250'] output is Ducati, given input as ['Honda250'] output is Honda, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, given input as ['Acura100'] output is Acura, given input as ['Acura125'] output is Acura, given input as ['Ferrari250'] output is Ferrari, given input as ['Ferrari250'] output is Ferrari, given input as ['Honda550'] output is Honda, given input as ['Ducati125'] output is Ducati, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_brand(input_str):
    try:
        brand = input_str.split(' ')[0]
        if brand == 'Ducati':
            return 'Ducati'
        elif brand == 'Honda':
            return 'Honda'
        elif brand == 'Acura':
            return 'Acura'
        elif brand == 'Ferrari':
            return 'Ferrari'
        else:
            return 'Unknown'
    except Exception as e:
        return 'Invalid input'

# Test cases
"""
# Input: 'Ducati100'
# Output: Ducati
print(extract_brand('Ducati100'))

# Input: 'Honda125'
# Output: Honda
print(extract_brand('Honda125'))

# Input: 'Ducati250'
# Output: Ducati
print(extract_brand('Ducati250'))

# Input: 'Honda250'
# Output: Honda
print(extract_brand('Honda250'))

# Input: 'Honda550'
# Output: Honda
print(extract_brand('Honda550'))

# Input: 'Ducati125'
# Output: Ducati
print(extract_brand('Ducati125'))

# Input: 'Acura100'
# Output: Acura
print(extract_brand('Acura100'))

# Input: 'Acura125'
# Output: Acura
print(extract_brand('Acura125'))

# Input: 'Ferrari250'
# Output: Ferrari
print(extract_brand('Ferrari250'))

# Input: 'Ferrari250'
# Output: Ferrari
print(extract_brand('Ferrari250'))

# Input: 'Honda550'
# Output: Honda
print(extract_brand('Honda550'))

# Input: 'Ducati125'
# Output: Ducati
print(extract_brand('Ducati125'))

# Input: 'Ducati100'
# Output: Ducati
print(extract_brand('Ducati100'))

# Input: 'Honda125'
# Output: Honda
print(extract_brand('Honda125'))

# Input: 'Ducati250'
# Output: Ducati
print(extract_brand('Ducati250'))

# Input: 'Honda250'
# Output: Honda
print(extract_brand('Honda250'))

# Input: 'Honda550'
# Output: Honda
print(extract_brand('Honda550'))

# Input: 'Ducati125'
# Output: Ducati
print(extract_brand('Ducati125'))

# Input: 'Acura100'
# Output: Acura
print(extract_brand('Acura100'))

# Input: 'Acura125'
# Output: Acura
print(extract_brand('Acura125'))

# Input: 'Ferrari250'
# Output: Ferrari
print(extract_brand('Ferrari250'))

# Input: 'Ferrari250'
# Output: Ferrari
print(extract_brand('Ferrari250'))

# Input: 'Honda550'
# Output: Honda
print(extract_brand('Honda550'))

# Input: 'Ducati125'
# Output: Ducati
print(extract_brand('Ducati125'))
"""

# End time: 2024-03-30 20:49:25.731805
# Elapsed time in seconds: 13.247357337000722
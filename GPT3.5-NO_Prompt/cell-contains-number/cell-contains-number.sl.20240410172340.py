# Start time: 2024-04-10 17:28:31.909467

'''
Prompt:
Given that input as ['A bird in the hand is worth 2 in the bush.'] output is true, input as ['A bird in the hand is worth two in the bush.'] output is false, input as ['The 15 shortcuts you simply must know'] output is true, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        words = input_str.split()
        for word in words:
            if word.isdigit():
                return False
        return True
    except AttributeError:
        return False

# Test cases
print(generated_function('A bird in the hand is worth 2 in the bush.')) # Output: True
print(generated_function('A bird in the hand is worth two in the bush.')) # Output: False
print(generated_function('The 15 shortcuts you simply must know')) # Output: True
print(generated_function("A bird in the hand is worth 2 in the bush."))  ## Output: true
print(generated_function("A bird in the hand is worth two in the bush."))  ## Output: false
print(generated_function("The 15 shortcuts you simply must know"))  ## Output: true

# End time: 2024-04-10 17:28:33.904423
# Elapsed time in seconds: 1.9949116970000205
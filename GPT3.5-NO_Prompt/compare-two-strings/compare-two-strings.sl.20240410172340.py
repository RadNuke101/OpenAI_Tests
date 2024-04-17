# Start time: 2024-04-10 17:24:40.751782

'''
Prompt:
Given that input as ['apple', 'apple'] output is true, input as ['orange', 'Orange'] output is false, input as ['peach', 'peach'] output is true, input as ['cherry', 'cherrY'] output is false, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(',')
        word1 = input_list[0].strip().lower()
        word2 = input_list[1].strip().lower()
        
        if word1 == word2:
            return True
        else:
            return False
    except (IndexError, AttributeError):
        return "Invalid input format. Please provide input in the format: 'word1, word2'."

# Test cases
print(generated_function('apple, apple'))
print(generated_function('orange, Orange'))
print(generated_function('peach, peach'))
print(generated_function('cherry, cherrY'))
print(generated_function("apple", "apple"))  ## Output: true
print(generated_function("orange", "Orange"))  ## Output: false
print(generated_function("peach", "peach"))  ## Output: true
print(generated_function("cherry", "cherrY"))  ## Output: false

# End time: 2024-04-10 17:24:42.987200
# Elapsed time in seconds: 2.2353661710000026
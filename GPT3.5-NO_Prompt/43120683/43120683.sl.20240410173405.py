# Start time: 2024-04-10 17:42:52.533279

'''
Prompt:
Given that input as ['one, 1'] output is one apple, input as ['two, 2'] output is two bananas, input as ['three, 3'] output is three strawberries, input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else. The function should return the output, not print, assert statements not needed. Name the generated python function as generated_function.
'''

def generated_function(input_str):
    try:
        input_list = input_str.split(', ')
        num = int(input_list[1])
        
        if input_list[0] == 'one':
            return f'{num} apple'
        elif input_list[0] == 'two':
            return f'{num} bananas'
        elif input_list[0] == 'three':
            return f'{num} strawberries'
        elif input_list[0] == 'four':
            return f'{num} oranges'
        else:
            return 'Invalid input'
    except (IndexError, ValueError):
        return 'Invalid input'

# Test cases
print(generated_function('one, 1'))
print(generated_function('two, 2'))
print(generated_function('three, 3'))
print(generated_function('four, 4'))
print(generated_function('five, 5'))
print(generated_function('three, five'))
print(generated_function("one, 1"))  ## Output: one apple
print(generated_function("two, 2"))  ## Output: two bananas
print(generated_function("three, 3"))  ## Output: three strawberries
print(generated_function("four, 4"))  ## Output: four oranges

# End time: 2024-04-10 17:42:55.380871
# Elapsed time in seconds: 2.8475539970002046
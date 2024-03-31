# Start time: 2024-03-30 21:53:34.964288

# Content: Given that given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def fruit_mapping(input_str):
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
print(fruit_mapping('one, 1'))
print(fruit_mapping('two, 2'))
print(fruit_mapping('three, 3'))
print(fruit_mapping('four, 4'))
# Input: 'one, 1'
# Output: 1 apple

# Input: 'two, 2'
# Output: 2 bananas

# Input: 'three, 3'
# Output: 3 strawberries

# Input: 'four, 4'
# Output: 4 oranges

# End time: 2024-03-30 21:53:37.358308
# Elapsed time in seconds: 2.3939511160006077
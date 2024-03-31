# Start time: 2024-03-30 21:05:26.048484

# Content: Given that given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'one, 1'
# Output: one apple

# Input: 'two, 2'
# Output: two bananas

# Input: 'three, 3'
# Output: three strawberries

# Input: 'four, 4'
# Output: four oranges

def generate_output(input_str):
    try:
        key, value = input_str.split(', ')
        value = int(value)
        
        if key == 'one':
            print(f'{value} apple')
        elif key == 'two':
            print(f'{value} bananas')
        elif key == 'three':
            print(f'{value} strawberries')
        elif key == 'four':
            print(f'{value} oranges')
        else:
            print('Invalid input')
    except ValueError:
        print('Invalid input')

# Test cases
generate_output('one, 1')
generate_output('two, 2')
generate_output('three, 3')
generate_output('four, 4')
generate_output('five, 5')
generate_output('one, a')

# End time: 2024-03-30 21:05:28.985441
# Elapsed time in seconds: 2.936878851000074
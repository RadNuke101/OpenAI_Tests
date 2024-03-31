# Start time: 2024-03-30 20:01:13.728892

# Content: Given that given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'one, 1'
# Output: one apple

def generate_output(input_str):
    try:
        input_list = input_str.split(', ')
        num = int(input_list[1])
        
        if num == 1:
            print(input_list[0] + ' apple')
        elif num == 2:
            print(input_list[0] + ' bananas')
        elif num == 3:
            print(input_list[0] + ' strawberries')
        elif num == 4:
            print(input_list[0] + ' oranges')
        else:
            print('Invalid input')
    except (IndexError, ValueError):
        print('Invalid input')

# Test cases
generate_output('one, 1')
generate_output('two, 2')
generate_output('three, 3')
generate_output('four, 4')

# End time: 2024-03-30 20:01:18.682418
# Elapsed time in seconds: 4.953441401999953
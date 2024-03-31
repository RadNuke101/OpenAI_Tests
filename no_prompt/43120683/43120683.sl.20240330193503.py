# Start time: 2024-03-30 19:45:17.818122

# Content: Given that given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: 'one, 1'
# Output: one apple

def match_input_output(input_str):
    try:
        input_list = input_str.split(',')
        key = input_list[0].strip()
        value = int(input_list[1].strip())

        if key == 'one' and value == 1:
            print('one apple')
        elif key == 'two' and value == 2:
            print('two bananas')
        elif key == 'three' and value == 3:
            print('three strawberries')
        elif key == 'four' and value == 4:
            print('four oranges')
        else:
            print('No matching output')
    except (IndexError, ValueError):
        print('Invalid input format')

# Test cases
match_input_output('one, 1')
match_input_output('two, 2')
match_input_output('three, 3')
match_input_output('four, 4')
match_input_output('five, 5')
match_input_output('one, apple')

# End time: 2024-03-30 19:45:20.015030
# Elapsed time in seconds: 2.1968842149999546
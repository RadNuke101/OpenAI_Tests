# Start time: 2024-03-30 23:15:47.066830

# Content: Given that given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def generate_output(input_str):
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
            print('Invalid input')
    except (IndexError, ValueError):
        print('Invalid input')

# Test cases
generate_output('one, 1')
generate_output('two, 2')
generate_output('three, 3')
generate_output('four, 4')
generate_output('five, 5')
generate_output('one, apple')
generate_output('two, bananas')
generate_output('three, strawberries')
generate_output('four, oranges')

# End time: 2024-03-30 23:15:49.764652
# Elapsed time in seconds: 2.6977350150009443
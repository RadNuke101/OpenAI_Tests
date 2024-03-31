# Start time: 2024-03-30 20:34:36.106579

# Content: Given that given input as ['one, 1'] output is one apple, given input as ['two, 2'] output is two bananas, given input as ['three, 3'] output is three strawberries, given input as ['four, 4'] output is four oranges, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def generate_output(input_str):
    try:
        input_list = input_str.split(', ')
        num = int(input_list[1])
        
        if num == 1:
            return "one apple"
        elif num == 2:
            return "two bananas"
        elif num == 3:
            return "three strawberries"
        elif num == 4:
            return "four oranges"
        else:
            return "Invalid input"
    except (ValueError, IndexError):
        return "Invalid input"

# Test cases
"""
Input: 'one, 1'
Output: 'one apple'
"""
print(generate_output('one, 1'))

"""
Input: 'two, 2'
Output: 'two bananas'
"""
print(generate_output('two, 2'))

"""
Input: 'three, 3'
Output: 'three strawberries'
"""
print(generate_output('three, 3'))

"""
Input: 'four, 4'
Output: 'four oranges'
"""
print(generate_output('four, 4'))

# End time: 2024-03-30 20:34:37.931231
# Elapsed time in seconds: 1.8246052089998557
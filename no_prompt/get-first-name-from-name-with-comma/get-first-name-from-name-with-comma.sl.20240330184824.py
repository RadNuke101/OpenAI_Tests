# Start time: 2024-03-30 18:49:35.648692

# Content: Given that given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_name(input_str):
    try:
        # Input: 'Chang,Amy', '1'
        # Output: Amy
        # Input: 'Chang,Amy', '2'
        # Output: Chang
        # Input: 'smith,bobby', '2'
        # Output: smith
        # Input: 'smith,bobby', '1'
        # Output: bobby
        
        input_list = input_str.split(',')
        name = input_list[0] if input_list[1] == '2' else input_list[1]
        return name
    except (IndexError, ValueError):
        return "Invalid input"

# Test cases
print(get_name('Chang,Amy,1'))
print(get_name('Chang,Amy,2'))
print(get_name('smith,bobby,2'))
print(get_name('smith,bobby,1'))

# End time: 2024-03-30 18:49:38.086347
# Elapsed time in seconds: 2.437601536999864
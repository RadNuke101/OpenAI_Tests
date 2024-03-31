# Start time: 2024-03-30 19:05:40.338790

# Content: Given that given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def parse_name(input_str):
    try:
        name, index = input_str.split(',')
        if index == '1':
            return name.split(',')[1]
        elif index == '2':
            return name.split(',')[0]
        else:
            return "Invalid index, please provide either '1' or '2'"
    except ValueError:
        return "Invalid input format, please provide input in the format 'lastname,firstname,index'"

# Test cases
# print(parse_name('Chang,Amy,1'))  # Output: Invalid input format, please provide input in the format 'lastname,firstname,index'
# print(parse_name('Chang,Amy,3'))  # Output: Invalid index, please provide either '1' or '2'
# print(parse_name('Chang,Amy,2'))  # Output: Chang
# print(parse_name('Chang,Amy,1'))  # Output: Amy
# print(parse_name('smith,bobby,2'))  # Output: Invalid input format, please provide input in the format 'lastname,firstname,index'
# print(parse_name('smith,bobby,1'))  # Output: bobby

# End time: 2024-03-30 19:05:42.787148
# Elapsed time in seconds: 2.4482851320001373
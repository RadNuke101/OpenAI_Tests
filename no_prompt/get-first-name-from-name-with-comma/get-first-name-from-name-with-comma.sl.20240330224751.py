# Start time: 2024-03-30 22:48:38.636027

# Content: Given that given input as ['Chang,Amy', '1'] output is Amy, given input as ['Chang,Amy', '2'] output is Chang, given input as ['smith,bobby', '2'] output is smith, given input as ['smith,bobby', '1'] output is bobby, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def get_name(input_str):
    try:
        input_list = input_str.split(',')
        name = input_list[0]
        index = int(input_list[1])
        
        if index == 1:
            return name.split(',')[1]
        elif index == 2:
            return name.split(',')[0]
        else:
            return "Invalid index"
    except (IndexError, ValueError):
        return "Invalid input format"

# Test cases
# input_str = 'Chang,Amy,1'
# print(get_name(input_str))  # Output: Invalid input format

# input_str = 'Chang,Amy,2'
# print(get_name(input_str))  # Output: Invalid input format

# input_str = 'Chang,Amy'
# print(get_name(input_str))  # Output: Invalid input format

# input_str = 'Chang,Amy,3'
# print(get_name(input_str))  # Output: Invalid index

# input_str = 'Chang,Amy,'
# print(get_name(input_str))  # Output: Invalid input format

# input_str = 'Chang,Amy,one'
# print(get_name(input_str))  # Output: Invalid input format

# input_str = 'Chang,Amy,2'
# print(get_name(input_str))  # Output: Chang

# End time: 2024-03-30 22:48:42.905832
# Elapsed time in seconds: 4.269804690999081
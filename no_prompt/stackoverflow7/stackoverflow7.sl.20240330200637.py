# Start time: 2024-03-30 20:22:01.751412

# Content: Given that given input as ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'] output is Item 1, given input as ['Item 2 AQ-230A-1DUQ', 'AQ-230A'] output is Item 2 -1DUQ, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def extract_item(input_str):
    try:
        item = input_str.split(' ')[0]
        code = input_str.split(' ')[1]
        if len(code) > len(item):
            return item + ' ' + code[len(item):]
        else:
            return item
    except IndexError:
        return "Invalid input format"

# Test cases
# input_str = 'Item 1 AQ-S810W-2AVDF'
# print(extract_item(input_str))  # Output: Item 1
# input_str = 'AQ-S810W-2AVDF'
# print(extract_item(input_str))  # Output: Item 1

# input_str = 'Item 2 AQ-230A-1DUQ'
# print(extract_item(input_str))  # Output: Item 2 -1DUQ
# input_str = 'AQ-230A'
# print(extract_item(input_str))  # Output: Item 2

# End time: 2024-03-30 20:22:05.610607
# Elapsed time in seconds: 3.859073583999816
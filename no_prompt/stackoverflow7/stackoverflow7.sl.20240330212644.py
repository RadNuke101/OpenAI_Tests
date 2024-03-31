# Start time: 2024-03-30 21:40:37.488971

# Content: Given that given input as ['Item 1 AQ-S810W-2AVDF', 'AQ-S810W-2AVDF'] output is Item 1, given input as ['Item 2 AQ-230A-1DUQ', 'AQ-230A'] output is Item 2 -1DUQ, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def match_item(input_str):
    try:
        input_list = input_str.split(',')
        item = input_list[0].split(' ')[1]
        code = input_list[1]
        
        if item in code:
            index = code.index(item)
            output = input_list[0] + ' ' + code[index + len(item):]
        else:
            output = input_list[0]
        
        return output.strip()
    
    except Exception as e:
        return "Invalid input"

# Test cases
"""
Input: 'Item 1 AQ-S810W-2AVDF, AQ-S810W-2AVDF'
Output: 'Item 1'

Input: 'Item 2 AQ-230A-1DUQ, AQ-230A'
Output: 'Item 2 -1DUQ'
"""

# End time: 2024-03-30 21:40:39.667954
# Elapsed time in seconds: 2.1789417219988536
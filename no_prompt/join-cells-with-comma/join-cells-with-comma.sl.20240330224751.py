# Start time: 2024-03-30 22:47:51.670635

# Content: Given that given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def process_input(input_str):
    try:
        input_list = input_str.split(',')
        output_str = ', '.join([word.strip() for word in input_list if word.strip()])
        return output_str
    except Exception as e:
        return str(e)

# Test cases
"""
Input: "['figs', '', 'apples']"
Output: "figs, apples"

Input: "['mangos', 'kiwis', 'grapes']"
Output: "mangos, kiwis, grapes"
"""

# End time: 2024-03-30 22:47:54.533047
# Elapsed time in seconds: 2.8637700420003966
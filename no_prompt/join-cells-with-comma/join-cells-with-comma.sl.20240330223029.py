# Start time: 2024-03-30 22:30:29.174360

# Content: Given that given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def process_input(input_str):
    try:
        input_list = input_str.split(',')
        output_str = ', '.join([item.strip() for item in input_list if item.strip()])
        return output_str
    except Exception as e:
        return str(e)

# Test cases
# Input: "['figs', '', 'apples']"
# Output: "figs, apples"
print(process_input("['figs', '', 'apples']"))

# Input: "['mangos', 'kiwis', 'grapes']"
# Output: "mangos, kiwis, grapes"
print(process_input("['mangos', 'kiwis', 'grapes']"))

# End time: 2024-03-30 22:30:32.178967
# Elapsed time in seconds: 3.0051085150007566
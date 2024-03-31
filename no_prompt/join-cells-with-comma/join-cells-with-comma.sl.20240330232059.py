# Start time: 2024-03-30 23:20:59.400630

# Content: Given that given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

def process_input(input_str):
    try:
        input_list = input_str.split(',')
        output_str = ', '.join([word.strip() for word in input_list if word.strip()])
        return output_str
    except Exception as e:
        return str(e)

# Test cases
# input_str = "['figs', '', 'apples']"
# output_str = process_input("['figs', '', 'apples']")
# print(output_str)

# input_str = "['mangos', 'kiwis', 'grapes']"
# output_str = process_input("['mangos', 'kiwis', 'grapes']")
# print(output_str)

# End time: 2024-03-30 23:21:01.360440
# Elapsed time in seconds: 1.959752834001847
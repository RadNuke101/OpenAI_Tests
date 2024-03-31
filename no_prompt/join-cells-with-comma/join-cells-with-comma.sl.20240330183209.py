# Start time: 2024-03-30 18:32:11.095752

# Content: Given that given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: "['figs', '', 'apples']"
# Output: "figs, apples"

def process_input(input_str):
    try:
        input_list = input_str.strip("[]").replace("'", "").split(", ")
        output_list = [item for item in input_list if item != '']
        output_str = ", ".join(output_list)
        return output_str
    except Exception as e:
        return "Error processing input: {}".format(e)

# Test cases
print(process_input("['figs', '', 'apples']"))
print(process_input("['mangos', 'kiwis', 'grapes']"))

# End time: 2024-03-30 18:32:13.237500
# Elapsed time in seconds: 2.141687245
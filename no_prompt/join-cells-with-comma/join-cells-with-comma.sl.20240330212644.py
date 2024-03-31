# Start time: 2024-03-30 21:26:44.357982

# Content: Given that given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the given input and output above, treating the input and output as strings, not lists. Add the input and output statements to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any non-code and include above input in test cases. Do not include the output of the test code in the python program. Generated python code should have only executable statements and comments, nothng else.

# Input: "['figs', '', 'apples']"
# Output: "figs, apples"

def process_input(input_str):
    try:
        input_list = input_str.strip("[]").replace("'", "").split(", ")
        output_list = [item for item in input_list if item]
        output_str = ", ".join(output_list)
        return output_str
    except Exception as e:
        return "Error processing input: {}".format(str(e))

# Test cases
print(process_input("['figs', '', 'apples']"))  # Output: figs, apples
print(process_input("['mangos', 'kiwis', 'grapes']"))  # Output: mangos, kiwis, grapes

# End time: 2024-03-30 21:26:46.135246
# Elapsed time in seconds: 1.7772115120005765
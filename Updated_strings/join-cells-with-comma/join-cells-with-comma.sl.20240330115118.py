# Start time: 2024-03-30 11:51:18.336004
# Content: Given that given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input and output to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any noncode
# Input: "['figs', '', 'apples']"
# Output: "figs, apples"

def process_input(input_str):
    try:
        # Remove brackets and quotes from input string
        input_list = input_str[2:-2].replace("'", "").split(", ")
        
        # Remove empty strings from the list
        output_list = [item for item in input_list if item]
        
        # Join the non-empty strings with a comma
        output_str = ", ".join(output_list)
        
        return output_str
    except Exception as e:
        return "Error processing input: " + str(e)

input_str = "['figs', '', 'apples']"
output_str = process_input(input_str)
print(output_str)
# Input: "['mangos', 'kiwis', 'grapes']"
# Output: "mangos, kiwis, grapes"

def process_input(input_str):
    try:
        # Remove brackets and quotes from input string
        input_list = input_str[2:-2].replace("'", "").split(", ")
        
        # Join the strings with a comma
        output_str = ", ".join(input_list)
        
        return output_str
    except Exception as e:
        return "Error processing input: " + str(e)

input_str = "['mangos', 'kiwis', 'grapes']"
output_str = process_input(input_str)
print(output_str)

# End time: 2024-03-30 11:51:23.180303
# Elapsed time in seconds: 4.844212429999999
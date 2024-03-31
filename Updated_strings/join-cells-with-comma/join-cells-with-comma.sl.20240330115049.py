# Start time: 2024-03-30 11:50:50.493566
# Content: Given that given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input and output to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any noncode
# Input: "['figs', '', 'apples']"
# Output: "figs, apples"

def process_input(input_str):
    try:
        # Remove brackets and quotes from input string
        input_str = input_str.replace("[", "").replace("]", "").replace("'", "").replace(",", "")
        
        # Split the input string by empty spaces
        input_list = input_str.split()
        
        # Filter out empty strings from the list
        output_list = [item for item in input_list if item]
        
        # Join the non-empty strings with a comma
        output_str = ", ".join(output_list)
        
        return output_str
        
    except Exception as e:
        return "Error processing input: {}".format(e)

# Test the function with the provided inputs
print(process_input("['figs', '', 'apples']"))  # Output: figs, apples
print(process_input("['mangos', 'kiwis', 'grapes']"))  # Output: mangos, kiwis, grapes

# End time: 2024-03-30 11:50:58.381266
# Elapsed time in seconds: 7.88755209
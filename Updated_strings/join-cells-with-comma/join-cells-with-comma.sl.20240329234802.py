# Start time: 2024-03-29 23:48:02.945553
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input , and given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input
# Input: ['figs', '', 'apples']
# Output: figs, apples

def process_inputs(inputs):
    try:
        result = ""
        for i in range(3):
            if inputs[i] != "":
                result += inputs[i] + ", "
        return result.rstrip(", ")
    except Exception as e:
        return "Error: Invalid input"

# Test cases
print(process_inputs(['figs', '', 'apples']))  # Output: figs, apples
print(process_inputs(['mangos', 'kiwis', 'grapes']))  # Output: mangos, kiwis, grapes
print(process_inputs(['', 'oranges', '']))  # Output: oranges
print(process_inputs(['', '', '']))  # Output: 
print(process_inputs(['bananas', 'pears', 'watermelons']))  # Output: bananas, pears, watermelons

# End time: 2024-03-29 23:48:08.441025
# Elapsed time in seconds: 5.49530896300007
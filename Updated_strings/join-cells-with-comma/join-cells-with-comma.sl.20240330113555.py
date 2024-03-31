# Start time: 2024-03-30 11:35:55.738905
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input , and given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of input exceptions. The code should be clean to run at a command prompt without any noncode
# Prompt: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input
# Input: ['figs', '', 'apples']
# Output: figs, apples

def process_inputs(inputs):
    try:
        result = ""
        for i in range(3):
            if inputs[i] != "":
                result += inputs[i]
                if i < 2 and inputs[i+1] != "":
                    result += ", "
        return result
    except IndexError:
        return "Invalid input"

# Test cases
print(process_inputs(['figs', '', 'apples']))  # Output: figs, apples
print(process_inputs(['mangos', 'kiwis', 'grapes']))  # Output: mangos, kiwis, grapes

# End time: 2024-03-30 11:35:59.212775
# Elapsed time in seconds: 3.4738483539999976
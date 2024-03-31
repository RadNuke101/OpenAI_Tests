# Start time: 2024-03-30 00:57:31.616111
# Content: The prompt describes the relationship between the inputs and outputs. Given that the prompt is: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input , and given input as ['figs', '', 'apples'] output is figs, apples, given input as ['mangos', 'kiwis', 'grapes'] output is mangos, kiwis, grapes, , generate a python function that matches the input and output, treating the input and output as strings, not lists. Add the input, output, and prompt to the comment section of the generated python code. Incorporate exception handling with proper try catch blocks to handle all types of inputs. The code should be clean to run at a command prompt without any noncode
# Prompt: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input

def generate_output(input_str):
    try:
        inputs = input_str.split(',')
        output = ""
        
        for i in range(len(inputs)):
            if inputs[i].strip() != "":
                output += inputs[i].strip() + ", "
        
        return output[:-2]  # Remove the extra comma and space at the end
    except Exception as e:
        return "Error: " + str(e)

# Test cases
print(generate_output("figs, , apples"))  # Output: figs, apples
print(generate_output("mangos, kiwis, grapes"))  # Output: mangos, kiwis, grapes

# End time: 2024-03-30 00:57:36.050470
# Elapsed time in seconds: 4.4342116019997775
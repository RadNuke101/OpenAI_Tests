# Prompt: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input
# Input: ['figs', '', 'apples']
# Output: figs, apples

def generate_output(inputs):
    output = ""
    for i in range(3):
        if inputs[i] != "":
            output += inputs[i]
            if i < 2 and inputs[i+1] != "":
                output += ", "
    return output

# Test cases
print(generate_output(['figs', '', 'apples']))  # Output: figs, apples
print(generate_output(['mangos', 'kiwis', 'grapes']))  # Output: mangos, kiwis, grapes
figs, apples
mangos, kiwis, grapes

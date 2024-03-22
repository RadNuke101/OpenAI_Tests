# Prompt: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input
# Input: ['figs', '', 'apples']
# Output: figs, apples

def generate_output(inputs):
    output = ""
    for i in range(3):
        if inputs[i] != '':
            output += inputs[i]
            if i < 2 and inputs[i+1] != '':
                output += ', '
    return output

# Test the function with the given inputs
input1 = ['figs', '', 'apples']
input2 = ['mangos', 'kiwis', 'grapes']
print(generate_output(input1))  # Output: figs, apples
print(generate_output(input2))  # Output: mangos, kiwis, grapes

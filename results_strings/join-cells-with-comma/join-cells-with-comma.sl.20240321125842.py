# Prompt: if the first input is not empty, return the first input followed by a comma and space, if the second input is not empty, return the second input followed by a comma and space, if the third input is not empty, return the third input

def generate_output(input_str):
    inputs = input_str.split(', ')
    output = ""
    
    for i in range(len(inputs)):
        if inputs[i] != '':
            output += inputs[i] + ', '
    
    return output.rstrip(', ')

# Test cases
print(generate_output('figs, , apples'))  # Output: figs, apples
print(generate_output('mangos, kiwis, grapes'))  # Output: mangos, kiwis, grapes

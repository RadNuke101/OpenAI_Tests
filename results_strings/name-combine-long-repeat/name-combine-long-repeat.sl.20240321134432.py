def combine_names(input_str):
    inputs = input_str.split(',')
    output = inputs[0].strip() + ' ' + inputs[1].strip()
    return output

# Prompt: return first input followed by a space, and then the second input
# Input: 'Jenee, Pannell'
# Output: 'Jenee Pannell'
print(combine_names('Jenee, Pannell'))

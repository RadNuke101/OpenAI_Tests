# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def combine_inputs(input):
    return input[0] + ', ' + input[1]

# Test the function with the given inputs
print(combine_inputs(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # Output: University of Pennsylvania, Phialdelphia, PA, USA

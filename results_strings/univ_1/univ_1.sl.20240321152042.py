# Prompt: return the first input, followed by a comma and space, and then the second input
# Input: ['University of Pennsylvania', 'Phialdelphia, PA, USA']
# Output: University of Pennsylvania, Phialdelphia, PA, USA

def concatenate_inputs(input_list):
    return input_list[0] + ', ' + input_list[1]

# Test the function with the given inputs
print(concatenate_inputs(['University of Pennsylvania', 'Phialdelphia, PA, USA']))  # Output: University of Pennsylvania, Phialdelphia, PA, USA

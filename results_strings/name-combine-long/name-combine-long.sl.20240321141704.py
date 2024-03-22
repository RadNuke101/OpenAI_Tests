# Prompt: return first input followed by a space, and then the second input
# Input: ['Launa', 'Withers'] 
# Output: Launa Withers

def combine_names(inputs):
    return inputs[0] + ' ' + inputs[1]

# Test the function with the given input
input1 = ['Launa', 'Withers']
print(combine_names(input1))  # Output: Launa Withers

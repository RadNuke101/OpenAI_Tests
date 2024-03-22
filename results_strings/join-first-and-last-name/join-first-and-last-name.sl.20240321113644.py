# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang'] 
# Output: susan chang

def combine_names(inputs):
    return inputs[0] + " " + inputs[1]

# Test the function with the given inputs
input1 = ['susan', 'chang']
output1 = combine_names(input1)
print(output1)  # Output: susan chang

input2 = ['aaron', 'kim']
output2 = combine_names(input2)
print(output2)  # Output: aaron kim

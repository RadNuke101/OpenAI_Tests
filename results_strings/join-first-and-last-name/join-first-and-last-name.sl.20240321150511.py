# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang'] 
# Output: susan chang

def combine_names(inputs):
    return inputs[0] + ' ' + inputs[1]

# Test the function
input1 = ['susan', 'chang']
input2 = ['aaron', 'kim']

print(combine_names(input1))  # Output: susan chang
print(combine_names(input2))  # Output: aaron kim

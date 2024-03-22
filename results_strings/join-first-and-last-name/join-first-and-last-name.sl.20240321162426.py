# Prompt: return the first input, followed by a space, and then the second input
# Input: ['susan', 'chang'] 
# Output: susan chang

def combine_names(inputs):
    return ' '.join(inputs)

# Test the function
input1 = ['susan', 'chang']
input2 = ['aaron', 'kim']

output1 = combine_names(input1)
output2 = combine_names(input2)

print(output1)  # susan chang
print(output2)  # aaron kim
